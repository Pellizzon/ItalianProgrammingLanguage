; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %"x" = alloca i32
  store i32 3, i32* %"x"
  %".5" = load i32, i32* %"x"
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".5")
  %".7" = load i32, i32* %"x"
  %".8" = add i32 3, %".7"
  store i32 %".8", i32* %"x"
  %".10" = load i32, i32* %"x"
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".10")
  store i32 3, i32* %"x"
  %".13" = load i32, i32* %"x"
  %".14" = icmp ne i32 %".13", 0
  br i1 %".14", label %"entry.if", label %"entry.else"
entry.if:
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 4)
  br label %"entry.endif"
entry.else:
  %".18" = load i32, i32* %"x"
  %".19" = icmp sle i32 %".18", 3
  %".20" = icmp ne i1 %".19", 0
  br i1 %".20", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  %".27" = load i32, i32* %"x"
  %".28" = icmp ne i32 %".27", 0
  br i1 %".28", label %"w_body", label %"w_after"
entry.else.if:
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 9)
  br label %"entry.else.endif"
entry.else.else:
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 3)
  br label %"entry.else.endif"
entry.else.endif:
  br label %"entry.endif"
w_body:
  %".30" = load i32, i32* %"x"
  %".31" = sub i32 %".30", 1
  store i32 %".31", i32* %"x"
  %".33" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 1000)
  %".34" = load i32, i32* %"x"
  %".35" = icmp ne i32 %".34", 0
  br i1 %".35", label %"w_body", label %"w_after"
w_after:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".38" = load i32, i32* %"i"
  %".39" = icmp slt i32 %".38", 5
  %".40" = icmp ne i1 %".39", 0
  br i1 %".40", label %"w_body.1", label %"w_after.1"
w_body.1:
  %".42" = load i32, i32* %"i"
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".42")
  %".44" = load i32, i32* %"i"
  %".45" = add i32 %".44", 1
  store i32 %".45", i32* %"i"
  %".47" = load i32, i32* %"i"
  %".48" = icmp slt i32 %".47", 5
  %".49" = icmp ne i1 %".48", 0
  br i1 %".49", label %"w_body.1", label %"w_after.1"
w_after.1:
  store i32 5, i32* %"i"
  %".52" = load i32, i32* %"i"
  %".53" = icmp sgt i32 %".52", 0
  %".54" = icmp ne i1 %".53", 0
  br i1 %".54", label %"w_body.2", label %"w_after.2"
w_body.2:
  %".56" = load i32, i32* %"i"
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".56")
  %".58" = load i32, i32* %"i"
  %".59" = sub i32 %".58", 1
  store i32 %".59", i32* %"i"
  %".61" = load i32, i32* %"i"
  %".62" = icmp sgt i32 %".61", 0
  %".63" = icmp ne i1 %".62", 0
  br i1 %".63", label %"w_body.2", label %"w_after.2"
w_after.2:
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
