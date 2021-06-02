; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %"x" = alloca i32
  store i32 10000, i32* %"x"
  %"x.1" = alloca i32
  %".5" = call i32 @"fib"(i32 9)
  store i32 %".5", i32* %"x.1"
  %".7" = load i32, i32* %"x.1"
  %".8" = bitcast [4 x i8]* @"fstr" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".7")
  %".10" = call i32 @"power"(i32 3, i32 3)
  %".11" = bitcast [4 x i8]* @"fstr" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  %".13" = call i32 @"power"(i32 3, i32 3)
  %".14" = call i32 @"fib"(i32 %".13")
  %".15" = bitcast [4 x i8]* @"fstr" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".14")
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".18" = load i32, i32* %"i"
  %".19" = icmp slt i32 %".18", 10
  %".20" = icmp ne i1 %".19", 0
  br i1 %".20", label %"w_body", label %"w_after"
w_body:
  %".22" = load i32, i32* %"i"
  %".23" = call i32 @"fib"(i32 %".22")
  %".24" = bitcast [4 x i8]* @"fstr" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".23")
  %".26" = load i32, i32* %"i"
  %".27" = add i32 %".26", 1
  store i32 %".27", i32* %"i"
  %".29" = load i32, i32* %"i"
  %".30" = icmp slt i32 %".29", 10
  %".31" = icmp ne i1 %".30", 0
  br i1 %".31", label %"w_body", label %"w_after"
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

define i32 @"fib"(i32 %".1") 
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %".4" = load i32, i32* %"n"
  %".5" = icmp sle i32 %".4", 1
  %".6" = icmp ne i1 %".5", 0
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  %".8" = load i32, i32* %"n"
  ret i32 %".8"
entry.else:
  br label %"entry.endif"
entry.endif:
  %".11" = load i32, i32* %"n"
  %".12" = sub i32 %".11", 1
  %".13" = call i32 @"fib"(i32 %".12")
  %".14" = load i32, i32* %"n"
  %".15" = sub i32 %".14", 2
  %".16" = call i32 @"fib"(i32 %".15")
  %".17" = add i32 %".13", %".16"
  ret i32 %".17"
}
