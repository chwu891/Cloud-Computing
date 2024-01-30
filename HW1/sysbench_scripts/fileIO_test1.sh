echo "FileIO Test 1"
for ((i=0;i<5;i++))
do
    sysbench fileio --file_test_mode=seqwr --time=30 run
done