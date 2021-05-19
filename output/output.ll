; ModuleID = "/home/pellizzon/Desktop/APSLogica/components/codeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %".4" = sub i32 0, 3
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".4")
  %"temp" = alloca i32
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"temp")
  %".7" = load i32, i32* %"temp"
  %".8" = mul i32 %".7", 1000
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".8")
  %"temp.1" = alloca i32
  %".10" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"temp.1")
  %".11" = load i32, i32* %"temp.1"
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".11")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"scanf"(i8* %".1", ...) 

@"tmp" = internal constant [3 x i8] c"%d\00"