from llvmlite import ir, binding


class CodeGen:
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_scanf_function()

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
        the host CPU.  The engine is reusable for an arbitrary number of
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
        # Declare argument list
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
        self.printf = (printf, printf_fmt_arg)

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

        self.scanf = (scanf, scanf_fmt_arg)

    def _compile_ir(self):
        """
        Compile the LLVM IR string with the given engine.
        The compiled module object is returned.
        """
        # Create a LLVM module object from the IR
        self.builder.ret_void()
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()
        # Now add the module and make sure it is ready for execution
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    def create_ir(self):
        self._compile_ir()

    def save_ir(self, filename):
        with open(filename, "w") as output_file:
            output_file.write(str(self.module))