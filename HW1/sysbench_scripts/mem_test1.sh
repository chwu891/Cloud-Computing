echo "Memory Test 1"
for ((i=0;i<5;i++))
do
    sysbench memory --memory_block_size=1G --time=30 run
done