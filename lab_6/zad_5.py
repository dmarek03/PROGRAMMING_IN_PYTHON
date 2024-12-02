import os
import time
import threading
def ping(ip):
     pingaling = os.popen("ping -n 1 "+ip,"r")
     while True:
         line = pingaling.readline()
         if not line:
             break
         if line.find('Average')>0:
            print(ip)

threads = []
start = time.perf_counter()
for host in range(1,20):
    ip = "192.168.1." + str(host)
    thread = threading.Thread(target=ping, args=(ip,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

stop = time.perf_counter()
print('time:',stop-start)
