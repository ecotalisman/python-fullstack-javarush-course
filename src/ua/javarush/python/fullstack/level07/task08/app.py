import time

def perform_task():
    start_time = time.time()
    while time.time() - start_time < 600:  # Runs for 10 minutes
        # Simulating CPU load
        sum(i * i for i in range(10000))
        # Simulating memory usage
        data = [x for x in range(100000)]
        time.sleep(0.5)  # Reducing the load between intervals

perform_task()