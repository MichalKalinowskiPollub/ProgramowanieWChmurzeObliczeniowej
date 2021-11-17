#!/usr/bin/env python3
# Michał Kalinowski IIST 7.3/5. Laboratorium 5. Sprawozdanie 1.
# Przykladowe uzycie(bez dockera): python server.py -p 1320
# Jak widać do uruchomienia serwera potrzebujemy przekazac argument -p ktory zdefiniuje PORT na ktorym zostanie udostepniona usluga.
# Serwer zostanie odpalony na adresie localhost:PORT.
import http.server
import socketserver
from datetime import datetime
import pytz
import sys
import argparse
import json
import urllib.request


# Klasa tworzaca i nasluchujaca na HTTP socket
class IpTrackerHandler(http.server.SimpleHTTPRequestHandler):
    # Gdy uzytkownik otwiera strone, zostaje utworzona dynamicznie strona z odpowiednimi informacjami na jego temat
    def handle(self):
        # Pobieramy ip klienta z którym łączy się serwer
        clientIp = self.client_address[0]
        # Probujemy pobrac strefe czasowa http://ip-api.com/json/ dla danego adresu IP klienta jako json
        GeoIpApiUrl = 'http://ip-api.com/json/'
        requestToGeoApi = urllib.request.Request(GeoIpApiUrl + clientIp)
        responseFromGeoApi = urllib.request.urlopen(requestToGeoApi).read()
        jsonResponseFromGeoApi = json.loads(responseFromGeoApi.decode('utf-8'))

        # Jesli ip adres jest prywatny jak np. localhost to nie mozemy wywnioskowac z niego strefy czasowej
        clientDateAndTime = None
        try:
            timezone = jsonResponseFromGeoApi['timezone']
            clientDateAndTime = datetime.now(pytz.timezone(timezone)).strftime('%d-%m-%y %H:%M:%S')
        except:
            clientDateAndTime = "nie mozna uzyskac daty i godziny z ip dla prywatnego uzytku"
        # Otwieramy index.html i dynamicznie nadpisujemy jego tresc w zalesnoci od ip uzytkownika
        file = open("../index.html", "w")
        file.write(f"""<!DOCTYPE html>
<html>
<body>
<h2 title="laboratoriumTitle">Laboratorium 5, zadanie 1 - Michal Kalinowski IIST 7.3/5</h2>
<p title="IpKlienta">Ip klienta: {clientIp}</p>
<p title="DataICzas">Data i godzina u klienta: {clientDateAndTime}</p>
</body>
</html>
"""
                   )
        file.close()
        return http.server.SimpleHTTPRequestHandler.handle(self)


# Na poczatku parsujemy argumenty zeby zobaczyc czy uzytkownik zapewnil port na ktorym serwer ma byc uruchomiony
parser = argparse.ArgumentParser()
parser.add_argument("-ptcp", "--Port")
args = parser.parse_args()
if args.Port:
    # pobranie obecnej daty uruchomienia serwera, odpowiednie jej formatowanie oraz wyswietlenie
    currentTime = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    print("Data uruchomienia:", currentTime)
    # wyswietlenie autora serwera
    author = "Michal Kalinowski"
    print("Autor serwera:", author)
    # wyswietlenie portu tcp pobranego przekazana przez pierwszy argument przy wywolaniu skryptu server.py
    port = int(args.Port)
    print("Port Tcp serwera to: %d" % port)

    # stworzenie odpowiedniego socketa oraz uruchomienie serwisu
    httpd = socketserver.TCPServer(("", port), IpTrackerHandler)
    try:
        httpd.serve_forever()
    except:
        print("Zamykanie serwera!")
        httpd.server_close()
else:
    print(
        "Prosze zapewnij port na ktorym serwer ma byc uruchomiony przez przekazanie argumentu -p lub --Port przy uruchomieniu serwera"
    )
