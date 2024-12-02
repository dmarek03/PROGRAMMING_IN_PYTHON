import threading
class Hello(threading.Thread): # class Hthreading.Threadello()
     def run(self):
         for i in range(10):
            print('hello')
class Hi(threading.Thread): # class Hi(threading.Thread)
     def run(self):
         for i in range(10):
            print('hi')

t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
t1.join()
t2.join()
print('stop')