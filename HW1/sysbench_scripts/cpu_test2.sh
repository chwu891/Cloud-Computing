echo "CPU Test 2"
for ((i=0;i<5;i++))
do
    sysbench cpu --cpu_max_prime=40000 --time=30 run
done