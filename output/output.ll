; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %"i" = alloca i32
  %"temp" = alloca i32
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"temp")
  %".5" = load i32, i32* %"temp"
  store i32 %".5", i32* %"i"
  %".7" = load i32, i32* %"i"
  %".8" = icmp slt i32 %".7", 10
  %".9" = icmp ne i1 %".8", 0
  br i1 %".9", label %"w_body", label %"w_after"
w_body:
  %".11" = load i32, i32* %"i"
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".11")
  %".13" = load i32, i32* %"i"
  %".14" = add i32 %".13", 1
  store i32 %".14", i32* %"i"
  %".16" = load i32, i32* %"i"
  %".17" = icmp slt i32 %".16", 10
  %".18" = icmp ne i1 %".17", 0
  br i1 %".18", label %"w_body", label %"w_after"
w_after:
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 1010101001)
  %"i.1" = alloca i32
  store i32 5, i32* %"i.1"
  %".22" = load i32, i32* %"i.1"
  %".23" = icmp slt i32 %".22", 10
  %".24" = icmp ne i1 %".23", 0
  br i1 %".24", label %"w_body.1", label %"w_after.1"
w_body.1:
  %".26" = load i32, i32* %"i.1"
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".26")
  %".28" = load i32, i32* %"i.1"
  %".29" = add i32 %".28", 1
  store i32 %".29", i32* %"i.1"
  %".31" = load i32, i32* %"i.1"
  %".32" = icmp slt i32 %".31", 10
  %".33" = icmp ne i1 %".32", 0
  br i1 %".33", label %"w_body.1", label %"w_after.1"
w_after.1:
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
