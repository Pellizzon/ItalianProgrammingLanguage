; ModuleID = "LLVLITE_OUTPUT"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr" to i8*
  %".3" = bitcast [3 x i8]* @"tmp" to i8*
  %".4" = sdiv i32 100, 10
  %".5" = mul i32 %".4", 2
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".5")
  %".7" = mul i32 22, 2
  %".8" = sdiv i32 %".7", 2
  %".9" = add i32 1, %".8"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".9")
  %".11" = sdiv i32 22, 2
  %".12" = mul i32 %".11", 2
  %".13" = add i32 1, %".12"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".13")
  %".15" = sub i32 0, 3
  %".16" = sub i32 0, %".15"
  %".17" = sub i32 0, %".16"
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".17")
  %".19" = sub i32 0, 3
  %".20" = sub i32 0, %".19"
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".20")
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 123123)
  %".23" = sub i32 0, 2
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".23")
  %".25" = xor i32 1, -1
  %".26" = add i32 %".25", 1
  %".27" = icmp ne i32 %".26", 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".27")
  %".29" = xor i32 3, -1
  %".30" = add i32 %".29", 1
  %".31" = icmp ne i32 %".30", 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".31")
  %".33" = xor i32 0, -1
  %".34" = add i32 %".33", 1
  %".35" = icmp ne i32 %".34", 0
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".35")
  %".37" = icmp slt i32 3, 2
  %".38" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".37")
  %".39" = icmp sle i32 3, 2
  %".40" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".39")
  %".41" = icmp sle i32 3, 3
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".41")
  %".43" = icmp slt i32 2, 3
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".43")
  %".45" = xor i32 0, -1
  %".46" = add i32 %".45", 1
  %".47" = icmp ne i32 %".46", 0
  %".48" = xor i32 1, -1
  %".49" = add i32 %".48", 1
  %".50" = icmp ne i32 %".49", 0
  %".51" = icmp sgt i1 %".47", %".50"
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".51")
  %".53" = xor i32 0, -1
  %".54" = add i32 %".53", 1
  %".55" = icmp ne i32 %".54", 0
  %".56" = icmp sge i1 %".55", 1
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".56")
  %".58" = icmp ne i32 0, 0
  %".59" = icmp ne i32 1, 0
  %".60" = and i1 %".58", %".59"
  %".61" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".60")
  %".62" = icmp ne i32 1, 0
  %".63" = icmp ne i32 0, 0
  %".64" = and i1 %".62", %".63"
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".64")
  %".66" = icmp ne i32 0, 0
  %".67" = icmp ne i32 0, 0
  %".68" = and i1 %".66", %".67"
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".68")
  %".70" = icmp ne i32 1, 0
  %".71" = icmp ne i32 1, 0
  %".72" = and i1 %".70", %".71"
  %".73" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".72")
  %".74" = icmp ne i32 2, 0
  %".75" = icmp ne i32 3, 0
  %".76" = and i1 %".74", %".75"
  %".77" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".76")
  %".78" = icmp ne i32 0, 0
  %".79" = icmp ne i32 0, 0
  %".80" = or i1 %".78", %".79"
  %".81" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".80")
  %".82" = icmp ne i32 0, 0
  %".83" = icmp ne i32 1, 0
  %".84" = or i1 %".82", %".83"
  %".85" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".84")
  %".86" = icmp ne i32 1, 0
  %".87" = icmp ne i32 0, 0
  %".88" = or i1 %".86", %".87"
  %".89" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".88")
  %".90" = icmp ne i32 1, 0
  %".91" = icmp ne i32 1, 0
  %".92" = or i1 %".90", %".91"
  %".93" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".92")
  %".94" = icmp ne i32 2, 0
  %".95" = icmp ne i32 3, 0
  %".96" = or i1 %".94", %".95"
  %".97" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".96")
  %".98" = shl i32 2, 1
  %".99" = lshr i32 %".98", 3
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".99")
  %".101" = shl i32 2, 2
  %".102" = and i32 %".101", 1
  %".103" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".102")
  %".104" = shl i32 2, 2
  %".105" = and i32 %".104", 3
  %".106" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".105")
  %".107" = shl i32 2, 2
  %".108" = or i32 %".107", 3
  %".109" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".108")
  %".110" = shl i32 5, 2
  %".111" = icmp ne i32 3, 0
  %".112" = icmp ne i32 %".110", 0
  %".113" = or i1 %".111", %".112"
  %".114" = call i32 (i8*, ...) @"printf"(i8* %".2", i1 %".113")
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
