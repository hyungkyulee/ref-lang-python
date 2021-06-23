import socket
import urllib
import urllib.request

socket_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_handle.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
socket_handle.send(cmd)

while True:
    data = socket_handle.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
socket_handle.close()

# scraping website
url = 'http://data.pr4e.org/intro-short.txt'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')