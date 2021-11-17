#Michał Kalinowski IIST 7.3/5. Laboratorium 5. Sprawozdanie 1.
# Michał Kalinowski IIST 7.3/5. Laboratorium 5. Sprawozdanie 1.
# Przykladowe uzycie:
# docker build . -t zad1
# Podczas uruchomiania nalezy dodac mapowanie portu tak żeby mapował się na odpowiadający niżej TCP_PORT_ARG.
# docker run --rm -p 1107:3338 -it zad1

FROM python:latest
#argument i zmienna srodowiskowa odpowiadajaca za port na ktorym chcemy uruchomic usluge
ARG TCP_PORT_ARG=3338
ENV TCP_PORT_ENV=${TCP_PORT_ARG}
# label informujacy o authorze, żeby się dowiedzieć
LABEL author="Michal Kalinowski"
WORKDIR /server/
# dodajemy kod serwera oraz tworzymy pusty plik index.html(bedzie on nadpisywany dynamicznie przez kod serwera)
ADD server.py /server/
RUN touch index.html
# Uruchamiamy serwer z odpowiednia zmienna srodowiskowa. Nie mozemy uzyc tutaj argumentu bo nie jest dostepny w runtime
CMD pip install pytz; python server.py -ptcp ${TCP_PORT_ENV}
# Informujemy dockera ze kontener nasluchuje na odpowiednim porcie tcp.
EXPOSE ${TCP_PORT_ARG}/tcp
