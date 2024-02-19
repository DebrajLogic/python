import time
retries = 5
wait_time = 1

while (retries > 0):
    print(f'Wait time = {wait_time}s')
    time.sleep(wait_time)
    wait_time *= 2
    retries -= 1
