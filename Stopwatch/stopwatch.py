import time

start_time = time.time()
input("Press 'Enter' to end the timer: ")
end_time = time.time()

time_diff = end_time - start_time
print(f"Elapsed time {time_diff} seconds")