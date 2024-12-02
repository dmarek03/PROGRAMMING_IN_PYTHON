import threading

import requests
import time
urls = [
'https://images3.alphacoders.com/103/103147.jpg',
'https://images4.alphacoders.com/975/97548.jpg',
'https://images4.alphacoders.com/810/81006.jpg',
'https://images7.alphacoders.com/423/423348.jpg',
'https://images7.alphacoders.com/381/381455.jpg',
'https://images.alphacoders.com/868/86853.jpg',
'https://images5.alphacoders.com/104/1043977.jpg',
'https://images4.alphacoders.com/788/788878.jpg',
'https://images8.alphacoders.com/419/419522.jpg',
'https://images2.alphacoders.com/475/475841.jpg',
'https://images6.alphacoders.com/595/595234.jpg',
'https://images.alphacoders.com/872/872716.jpg',
'https://images2.alphacoders.com/462/462942.jpg',
'https://images4.alphacoders.com/832/83206.jpg',
'https://images2.alphacoders.com/861/861016.jpg'
]

def download(url):
    fname = url.split('/')[-1]
    print(fname, end='')
    buf = requests.get(url).content
    with open(fname, 'wb') as f:
        f.write(buf)
    print(' ok')

start = time.perf_counter()

threads = []
for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

stop = time.perf_counter()
print('time:', stop-start)