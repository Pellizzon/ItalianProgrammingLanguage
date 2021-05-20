; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %".4" = icmp slt i32 7, 8
  %".5" = icmp ne i1 %".4", 0
  br i1 %".5", label %"entry.if", label %"entry.else"
entry.if:
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 3)
  br label %"entry.endif"
entry.else:
  %".9" = icmp slt i32 4, 5
  %".10" = icmp ne i1 %".9", 0
  br i1 %".10", label %"entry.else.if", label %"entry.else.else"
entry.endif:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %".18" = load i32, i32* %"i"
  %".19" = icmp slt i32 %".18", 3
  %".20" = icmp ne i1 %".19", 0
  br i1 %".20", label %"w_body", label %"w_after"
entry.else.if:
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 100)
  br label %"entry.else.endif"
entry.else.else:
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 5)
  br label %"entry.else.endif"
entry.else.endif:
  br label %"entry.endif"
w_body:
  %".22" = load i32, i32* %"i"
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".22")
  %".24" = load i32, i32* %"i"
  %".25" = mul i32 %".24", 2
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".25")
  %".27" = load i32, i32* %"i"
  %".28" = add i32 %".27", 1
  store i32 %".28", i32* %"i"
  %".30" = load i32, i32* %"i"
  %".31" = icmp slt i32 %".30", 3
  %".32" = icmp ne i1 %".31", 0
  br i1 %".32", label %"w_body", label %"w_after"
w_after:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %".35" = load i32, i32* %"x"
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".35")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [4 x i8] c"%d\0a\00"
declare i32 @"scanf"(i8* %".1", ...) 

@"tmp" = internal constant [3 x i8] c"%d\00"