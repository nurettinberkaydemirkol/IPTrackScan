import socket
import geocoder
import folium
import threading
import concurrent.futures
import colorama
from colorama import Fore


colorama.init()


print_lock = threading.Lock()

ip = input("Enter the IP to scan: ")
geo = geocoder.ip(ip)


addr = geo.latlng
print(addr)

my_map = folium.Map(location=addr,
                    zoom_start=20)

folium.CircleMarker(location=addr,
                    radius=50,
                    popup="Yorkshire").add_to(my_map)
folium.Marker(addr,
              popup="Yorkshire").add_to(my_map)

my_map.save("mymap.html ")

def scan(ip, port):
    scanner=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + "Opened")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)