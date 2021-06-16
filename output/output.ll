; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %".4" = add i32 7, 8
  %".5" = call i32 @"piu"(i32 %".4", i32 5)
  %".6" = bitcast [4 x i8]* @"fstr" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  %".8" = call i32 @"aaaaaaaaaaaaaaaaaaaaaaa"(i32 1, i32 2, i32 3)
  %".9" = bitcast [4 x i8]* @"fstr" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
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

define i32 @"piu"(i32 %".1", i32 %".2") 
{
entry:
  %"x" = alloca i32
  store i32 %".1", i32* %"x"
  %"y" = alloca i32
  store i32 %".2", i32* %"y"
  %".6" = load i32, i32* %"x"
  %".7" = load i32, i32* %"y"
  %".8" = add i32 %".6", %".7"
  ret i32 %".8"
}

define i32 @"aaaaaaaaaaaaaaaaaaaaaaa"(i32 %".1", i32 %".2", i32 %".3") 
{
entry:
  %"x" = alloca i32
  store i32 %".1", i32* %"x"
  %"y" = alloca i32
  store i32 %".2", i32* %"y"
  %"z" = alloca i32
  store i32 %".3", i32* %"z"
  %".8" = load i32, i32* %"x"
  %".9" = load i32, i32* %"y"
  %".10" = add i32 %".8", %".9"
  %".11" = load i32, i32* %"z"
  %".12" = add i32 %".10", %".11"
  %".13" = call i32 @"power"(i32 %".12", i32 2)
  ret i32 %".13"
}
