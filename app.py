# import urllib.request
import time
from xml.etree.ElementTree import parse

candidates = []
office_lat = 41.980262




# def update():  
#     u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
#     data = u.read()
#     f = open('rt22.xml', 'wb')
#     f.write(data)
#     f.close()

def get_data():
    doc = parse('rt22.xml')
    for bus in doc.findall('bus'):
        lat = float(bus.findtext('lat'))
        if lat >= office_lat:
            busid = bus.findtext('id')
            direction = bus.findtext('d')
            if direction.startswith('North'):
                print(busid, direction, lat)
                candidates.append(busid)

def distance(lat1, lat2):
    'Return distance in miles beetween two latitudes'
    return 69*abs(lat1 - lat2)

def monitor():
    doc = parse('rt22.xml')
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, office_lat)
            print(busid, dis, "miles")

            
while True:
    # update()
    get_data()
    print('---------------how far???------------\n')
    monitor()
    print('---------------updating data...------\n')
    for n in range(0,5):
        print('.')
        time.sleep(1)
    
    
