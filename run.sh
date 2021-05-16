FILE=""
if [ $# -eq 0 ]; then
    read -p "enter path to program file: " FILE
else
    FILE="$1"
fi
    
python3 main.py $FILE
llc -filetype=obj output/output.ll
gcc -no-pie output/output.o -o output/output
./output/output
