echo "CPU Test 1"
for ((i=0;i<5;i++))
do
    sysbench cpu --cpu_max_prime=20000 --time=30 run
done