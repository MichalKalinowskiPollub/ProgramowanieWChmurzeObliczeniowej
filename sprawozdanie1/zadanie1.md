# Zadanie 1
W celu uruchomienia serwera napisanego w pythonie bez dockera nalezy wywolać w terminalu przykladowo:

```python server.py -p 1320```

Wymagane jest podanie argumentu -p ktory okresla PORT na ktorym ma zostać udostępniona usługa. Sam Serwer zostanie odpalony na adresie localhost:PORT.

# Zadanie 2/3
a) W celu zbudowania obrazu kontenera za pomocą Dockera należy wywołać

``` docker build . -t zad1 ```

b) W celu łatwego uruchomienia i sprawdzenia kontenera, należy dodac mapowanie portu tak zeby mapował się na odpowiadający z Dockerfile argument TCP_PORT_ARG(defaultowo o wartosci 3338). Przykładowe uruchomienie usługi tak żeby na hoscie dało się ją uruchomić na porcie 1107(localhost:1107) wygląda następująco:

``` docker run --rm -p 1107:3338 -it zad1 ```

c) Informacje które wygenerował serwer w trakcie uruchamiania kontenera z punktu 1a, powinny pojawić się jako logi(output) w konsoli.
d) Żeby sprawdzić ile warstw posiada zbudowany obraz można użyć polecenia:
```docker history zad1```
Żeby poznać ich dokładną liczbę bez liczenia ręcznego można użyć: ```docker history -q zad1 | wc -l ```

# Zadanie 4
W celu zbudowania obrazu wykorzystujac bezposredni link do Dockefile nalezy wykonac przykladowo polecenie:

```  docker build https://github.com/MichalKalinowskiPollub/ProgramowanieWChmurzeObliczeniowej.git#main:sprawozdanie1 ```

Po zbudowaniu obrazu, przeniesienie go na konto DockerHub, jest możliwe po uprzednim stworzeniu na nim konta i repozytorium. Po tym kroku wystarczy odpowiednio zatagować swoj obraz:

``` docker tag <existing-image> <hub-user>/<repo-name>[:<tag>] ```

Następnie należy scommitować zmiany:

``` docker commit <existing-container> <hub-user>/<repo-name>[:<tag>] ```

Następnie wystarczy zpushować obraz do rejestru wskazanego przez jego nazwę lub tag.

``` docker push <hub-user>/<repo-name>:<tag> ```

Po tych krokach nasz obraz powinnien zostać umieszczony na DockerHub.
