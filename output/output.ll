; ModuleID = "/home/pellizzon/Desktop/APSLogica/components/codeGen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [5 x i8]* @"fstr" to i8*
  %".3" = icmp slt i32 7, 8
  %".4" = icmp ne i1 %".3", 0
  br i1 %".4", label %"entry.if", label %"entry.else"
entry.if:
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 3)
  br label %"entry.endif"
entry.else:
  %".8" = icmp slt i32 4, 5
  %".9" = icmp ne i1 %".8", 0
  br i1 %".9", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".17" = load i32, i32* %"i"
  %".18" = icmp slt i32 %".17", 3
  %".19" = icmp ne i1 %".18", 0
  br i1 %".19", label %"w_body", label %"w_after"
entry.else.if:
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 100)
  br label %"entry.else.endif"
entry.else.else:
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 5)
  br label %"entry.else.endif"
entry.else.endif:
  br label %"entry.endif"
w_body:
  %".21" = load i32, i32* %"i"
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".21")
  %".23" = load i32, i32* %"i"
  %".24" = mul i32 %".23", 2
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".24")
  %".26" = load i32, i32* %"i"
  %".27" = add i32 %".26", 1
  store i32 %".27", i32* %"i"
  %".29" = load i32, i32* %"i"
  %".30" = icmp slt i32 %".29", 3
  %".31" = icmp ne i1 %".30", 0
  br i1 %".31", label %"w_body", label %"w_after"
w_after:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %".34" = load i32, i32* %"x"
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".34")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%d \0a\00"