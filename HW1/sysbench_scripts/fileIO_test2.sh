echo "FileIO Test 2"
sysbench fileio --file_test_mode=rndrd --time=30 prepare
for ((i=0;i<5;i++))
do
    sysbench fileio --file_test_mode=rndrd --time=30 run
    sudo -i
    echo 3 > /proc/sys/vm/drop_caches
    exit
done