from llvmlite import ir, binding
import llvmlite.binding as llvm


class CodeGen:
    def __init__(self):
        self.builtInFunctions = {}
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_scanf_function()
        self._declare_pow_function()

    def _config_llvm(self):
        # Config LLVM
        self.module = ir.Module(name="LLVLITE_OUTPUT")
        self.module.triple = self.binding.get_default_triple()
        func_type = ir.FunctionType(ir.VoidType(), [], False)
        base_func = ir.Function(self.module, func_type, name="main")
        block = base_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def _create_execution_engine(self):
        """
        Create an ExecutionEngine suitable for JIT code generation on
        the host CPU. The engine is reusable for an arbitrary number of
        modules.
        """
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        # And an execution engine with an empty backing module
        backing_mod = binding.parse_assembly("")
        engine = binding.create_mcjit_compiler(backing_mod, target_machine)
        self.engine = engine

    def _declare_print_scanf_function(self):

        # Declare Printf function
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")

        printf_fmt = "%d\n\0"
        c_printf_fmt = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(printf_fmt)),
            bytearray(printf_fmt.encode("utf8")),
        )
        printf_global_fmt = ir.GlobalVariable(
            self.module, c_printf_fmt.type, name="fstr"
        )
        printf_global_fmt.linkage = "internal"
        printf_global_fmt.global_constant = True
        printf_global_fmt.initializer = c_printf_fmt
        printf_fmt_arg = self.builder.bitcast(printf_global_fmt, voidptr_ty)

        self.builtInFunctions["printf"] = (printf, printf_global_fmt, voidptr_ty)

        # Declare scanf function
        scanf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        scanf = ir.Function(self.module, scanf_ty, name="scanf")
        scanf_fmt = "%d\00"
        c_scanf_fmt = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(scanf_fmt)),
            bytearray(scanf_fmt.encode("utf8")),
        )
        global_scanf_fmt = ir.GlobalVariable(self.module, c_scanf_fmt.type, name="tmp")
        global_scanf_fmt.linkage = "internal"
        global_scanf_fmt.global_constant = True
        global_scanf_fmt.initializer = c_scanf_fmt
        scanf_fmt_arg = self.builder.bitcast(global_scanf_fmt, voidptr_ty)

        self.builtInFunctions["scanf"] = (scanf, global_scanf_fmt, voidptr_ty)

    def _declare_pow_function(self):
        i32 = ir.IntType(32)
        pow_ty = ir.FunctionType(i32, [i32, i32])
        power_func = ir.Function(self.module, pow_ty, name="power")
        block = power_func.append_basic_block("entry")
        builder = ir.IRBuilder(block)
        # def power(n, m):
        #     i = 1
        #     while m > 0:
        #         i = i * n
        #         m = m - 1
        #     return i
        n, m = power_func.args
        i_address = builder.alloca(i32)

        m_address = builder.alloca(i32)
        # i = 1
        builder.store(ir.Constant(i32, 1), i_address)
        # m = m_arg
        builder.store(m, m_address)

        w_body_block = builder.append_basic_block("w_body")
        w_after_block = builder.append_basic_block("w_after")

        constant0 = ir.Constant(ir.IntType(32), 0)
        constant1 = ir.Constant(ir.IntType(32), 1)

        # m > 0
        m = builder.load(m_address)
        condition = builder.icmp_signed(">", m, constant0)

        builder.cbranch(condition, w_body_block, w_after_block)

        # body
        builder.position_at_start(w_body_block)

        # i * n
        i = builder.load(i_address)
        i = builder.mul(i, n)
        builder.store(i, i_address)
        # m - 1
        m = builder.load(m_address)
        m = builder.sub(m, constant1)
        builder.store(m, m_address)
        # m > 0 to check while condition again
        condition = builder.icmp_signed(">", m, constant0)
        builder.cbranch(condition, w_body_block, w_after_block)
        builder.position_at_start(w_after_block)

        final_i = builder.load(i_address)
        builder.ret(final_i)

        self.builtInFunctions["pow"] = power_func

    def _compile_ir(self, optimize):
        """
        Compile the LLVM IR string with the given engine.
        The compiled module object is returned.
        """
        # Create a LLVM module object from the IR
        self.builder.ret_void()
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        if optimize:
            pmb = llvm.create_pass_manager_builder()
            pmb.opt_level = 2
            pm = llvm.create_module_pass_manager()
            pmb.populate(pm)
            pm.run(mod)
        mod.verify()
        # add the module and make sure it is ready for execution
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    def create_ir(self, ast, symbolTable, optimize=True):
        ast.Evaluate(symbolTable, self.builder, self.builtInFunctions, self.module)
        self._compile_ir(optimize)

    def save_ir(self, filename):
        with open(filename, "w") as output_file:
            output_file.write(str(self.module))