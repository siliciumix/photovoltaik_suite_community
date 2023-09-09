# Photovoltaik Logfile Downloader 

#### community editions


## Konfiguration anpassen

Im Bereich "Speicher" muss die IP-Adresse des Speichers angegeben werden. Es darf kein "HTTP" oder "HTTPS" oder ähnliches davor angegeben werden, da dies automatisch durch das Skript erfolgt. Ebenso darf auch kein Pfad zu den Logfiles angegeben werden, denn auch das geschieht automatisch durch das Skript.

Der Bereich "Logfiles" bezieht sich ausschließlich auf den Logfile Downloader, da diese Konfigurationsdatei auch für weitere Skripte verwendet wird. Hier sollte das "startDatum" angepasst werden, um festzulegen, ab welchem Tag die Logfiles heruntergeladen werden sollen. Bei der ersten Verwendung ist das idealerweise das Inbetriebnahme Datum.

Mit der Einstellung "pfardart" legt man fest, wo die Logfiles gespeichert werden sollen. Dies geschieht relativ zum gerade ausgeführten Skript, welches "logfile.py" ist. Wenn wir "pfardart" mit "../logfiles" festlegen, bedeutet das, dass die Logfiles in einem Unterverzeichnis namens "logfiles" geschrieben werden, welches eine Ebene höher liegt.

```
├ logfile_downloader
├── config_api
├── logfile_api
       ├── __init__.py
       ├── logfile.py
├── config_api
├── logfiles
├── config.yaml 
├── ////////////////////
```

Mit der Einstellung **suffix** legen wir die Endung unseres Logfiles fest.




