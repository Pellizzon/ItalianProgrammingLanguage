; ModuleID = "/home/pellizzon/Desktop/APSLogica/components/codeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %"i" = alloca i32
  store i32 100, i32* %"i"
  %".4" = load i32, i32* %"i"
  %".5" = icmp slt i32 %".4", 10
  %".6" = icmp ne i1 %".5", 0
  br i1 %".6", label %"w_body", label %"w_after"
w_body:
  %".8" = load i32, i32* %"i"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".8")
  %".10" = load i32, i32* %"i"
  %".11" = add i32 %".10", 1
  store i32 %".11", i32* %"i"
  %".13" = load i32, i32* %"i"
  %".14" = icmp slt i32 %".13", 10
  %".15" = icmp ne i1 %".14", 0
  br i1 %".15", label %"w_body", label %"w_after"
w_after:
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 1010101001)
  %"i.1" = alloca i32
  store i32 5, i32* %"i.1"
  %".19" = load i32, i32* %"i.1"
  %".20" = icmp slt i32 %".19", 10
  %".21" = icmp ne i1 %".20", 0
  br i1 %".21", label %"w_body.1", label %"w_after.1"
w_body.1:
  %".23" = load i32, i32* %"i.1"
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".23")
  %".25" = load i32, i32* %"i.1"
  %".26" = add i32 %".25", 1
  store i32 %".26", i32* %"i.1"
  %".28" = load i32, i32* %"i.1"
  %".29" = icmp slt i32 %".28", 10
  %".30" = icmp ne i1 %".29", 0
  br i1 %".30", label %"w_body.1", label %"w_after.1"
w_after.1:
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%d \0a\00"