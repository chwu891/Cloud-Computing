echo "Memory Test 2"
for ((i=0;i<5;i++))
do
    sysbench memory --memory_block_size=2G --time=30 run
done