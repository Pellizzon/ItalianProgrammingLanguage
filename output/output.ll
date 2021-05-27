; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %".4" = sub i32 0, 3
  %".5" = bitcast [4 x i8]* @"fstr" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".4")
  %".7" = icmp ne i32 5, 0
  %".8" = icmp ne i32 5, 0
  %".9" = and i1 %".7", %".8"
  %".10" = icmp ne i32 5, 0
  %".11" = icmp ne i32 3, 0
  %".12" = and i1 %".10", %".11"
  %".13" = icmp ne i1 %".9", 0
  %".14" = icmp ne i1 %".12", 0
  %".15" = or i1 %".13", %".14"
  %".16" = bitcast [4 x i8]* @"fstr" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i1 %".15")
  %".18" = srem i32 16, 7
  %".19" = bitcast [4 x i8]* @"fstr" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %".18")
  %".21" = srem i32 3, 2
  %".22" = bitcast [4 x i8]* @"fstr" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %".21")
  %".24" = bitcast [3 x i8]* @"tmp" to i8*
  %"temp" = alloca i32
  %".25" = call i32 (i8*, ...) @"scanf"(i8* %".24", i32* %"temp")
  %".26" = load i32, i32* %"temp"
  %".27" = mul i32 %".26", 1000
  %".28" = bitcast [4 x i8]* @"fstr" to i8*
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".28", i32 %".27")
  %".30" = bitcast [3 x i8]* @"tmp" to i8*
  %"temp.1" = alloca i32
  %".31" = call i32 (i8*, ...) @"scanf"(i8* %".30", i32* %"temp.1")
  %".32" = load i32, i32* %"temp.1"
  %".33" = bitcast [4 x i8]* @"fstr" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i32 %".32")
  %".35" = icmp ne i32 5, 0
  %".36" = icmp ne i32 3, 0
  %".37" = and i1 %".35", %".36"
  %".38" = bitcast [4 x i8]* @"fstr" to i8*
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".38", i1 %".37")
  %".40" = and i32 5, 3
  %".41" = bitcast [4 x i8]* @"fstr" to i8*
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".41", i32 %".40")
  %".43" = call i32 @"power"(i32 4, i32 10)
  %".44" = bitcast [4 x i8]* @"fstr" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44", i32 %".43")
  %".46" = add i32 1, 2
  %".47" = call i32 @"power"(i32 3, i32 %".46")
  %".48" = bitcast [4 x i8]* @"fstr" to i8*
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".48", i32 %".47")
  %".50" = add i32 1, 3
  %".51" = mul i32 1, 2
  %".52" = add i32 1, %".51"
  %".53" = call i32 @"power"(i32 %".50", i32 %".52")
  %".54" = bitcast [4 x i8]* @"fstr" to i8*
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54", i32 %".53")
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
