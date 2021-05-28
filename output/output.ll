; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %"i" = alloca i32
  %".4" = sub i32 0, 1
  store i32 %".4", i32* %"i"
  %".6" = load i32, i32* %"i"
  %".7" = icmp slt i32 %".6", 10
  %".8" = icmp ne i1 %".7", 0
  br i1 %".8", label %"w_body", label %"w_after"
w_body:
  %".10" = load i32, i32* %"i"
  %".11" = call i32 @"factorial"(i32 %".10")
  %".12" = bitcast [4 x i8]* @"fstr" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".11")
  %".14" = load i32, i32* %"i"
  %".15" = add i32 %".14", 1
  store i32 %".15", i32* %"i"
  %".17" = load i32, i32* %"i"
  %".18" = icmp slt i32 %".17", 10
  %".19" = icmp ne i1 %".18", 0
  br i1 %".19", label %"w_body", label %"w_after"
w_after:
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"scanf"(i8* %".1", ...) 

@"tmp" = internal constant [3 x i8] c"%d\00"
define i32 @"power"(i32 %".1", i32 %".2") 
{
entry:
  %".4" = alloca i32
  %".5" = alloca i32
  store i32 1, i32* %".4"
  store i32 %".2", i32* %".5"
  %".8" = load i32, i32* %".5"
  %".9" = icmp sgt i32 %".8", 0
  br i1 %".9", label %"w_body", label %"w_after"
w_body:
  %".11" = load i32, i32* %".4"
  %".12" = mul i32 %".11", %".1"
  store i32 %".12", i32* %".4"
  %".14" = load i32, i32* %".5"
  %".15" = sub i32 %".14", 1
  store i32 %".15", i32* %".5"
  %".17" = icmp sgt i32 %".15", 0
  br i1 %".17", label %"w_body", label %"w_after"
w_after:
  %".19" = load i32, i32* %".4"
  ret i32 %".19"
}

define i32 @"factorial"(i32 %".1") 
{
entry:
  %"x" = alloca i32
  store i32 %".1", i32* %"x"
  %".4" = load i32, i32* %"x"
  %".5" = icmp slt i32 %".4", 0
  %".6" = icmp ne i1 %".5", 0
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  ret i32 0
entry.else:
  br label %"entry.endif"
entry.endif:
  %".10" = load i32, i32* %"x"
  %".11" = icmp eq i32 %".10", 0
  %".12" = icmp ne i1 %".11", 0
  br i1 %".12", label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  ret i32 1
entry.endif.else:
  %".15" = load i32, i32* %"x"
  %".16" = icmp eq i32 %".15", 1
  %".17" = icmp ne i1 %".16", 0
  br i1 %".17", label %"entry.endif.else.if", label %"entry.endif.else.else"
entry.endif.endif:
  %".22" = load i32, i32* %"x"
  %".23" = load i32, i32* %"x"
  %".24" = sub i32 %".23", 1
  %".25" = call i32 @"factorial"(i32 %".24")
  %".26" = mul i32 %".22", %".25"
  ret i32 %".26"
entry.endif.else.if:
  ret i32 1
entry.endif.else.else:
  br label %"entry.endif.else.endif"
entry.endif.else.endif:
  br label %"entry.endif.endif"
}
