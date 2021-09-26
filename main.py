import socket
import geocoder
import folium
import threading
import concurrent.futures
import colorama
from colorama import Fore

#COLORING
colorama.init()


print_lock = threading.Lock()

#INPUT
ip = input("Enter the IP to scan: ")

#GEO PLUGIN 
geo = geocoder.ip(ip)
addr = geo.latlng
print(addr)

#CREATE MAP
my_map = folium.Map(location=addr,
                    zoom_start=20)

#MARKERS
folium.CircleMarker(location=addr,
                    radius=50,
                    popup="Yorkshire").add_to(my_map)
folium.Marker(addr,
              popup="Yorkshire").add_to(my_map)

#SAVE AS
my_map.save("mymap.html ")

#SCAN
def scan(ip, port):
    scanner=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            #OUTPUTS
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + "Opened")
    except:
        pass

#SCAN [FOR]
with concurrent.futures.ThreadPoolExecutor() as executor:
    #YOU CAN CHANGE THIS VALUE
    for port in range(1000):
        executor.submit(scan, ip, port + 1)
