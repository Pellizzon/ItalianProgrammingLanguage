; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %".4" = sub i32 0, 3
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".4")
  %".6" = and i32 5, 5
  %".7" = and i32 5, 3
  %".8" = or i32 %".6", %".7"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".8")
  %".10" = srem i32 16, 7
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".10")
  %".12" = srem i32 3, 2
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".12")
  %"temp" = alloca i32
  %".14" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"temp")
  %".15" = load i32, i32* %"temp"
  %".16" = mul i32 %".15", 1000
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".16")
  %"temp.1" = alloca i32
  %".18" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"temp.1")
  %".19" = load i32, i32* %"temp.1"
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".19")
  %".21" = and i32 5, 3
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".21")
  %".23" = and i32 5, 3
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".23")
  %".25" = call i32 @"power"(i32 4, i32 10)
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".25")
  %".27" = add i32 1, 2
  %".28" = call i32 @"power"(i32 3, i32 %".27")
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".28")
  %".30" = add i32 1, 3
  %".31" = mul i32 1, 2
  %".32" = add i32 1, %".31"
  %".33" = call i32 @"power"(i32 %".30", i32 %".32")
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".33")
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
