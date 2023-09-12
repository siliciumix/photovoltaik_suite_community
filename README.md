# Photovoltaik Logfile Downloader 

#### community editions

## Python installieren

### Windows

Bei der Installation von Python müsst ihr darauf achten das **PIP** ebenfalls installiert wird.

---
 **ACHTUNG**

Es müssen unbedingt noch weitere Module installiert werden.
Dazu in den Ordner gehen in dem der Logfile Downloader gespeichert ist und dann folgenden Befehl ausführen.

```
pip install -r requirements.txt
```

Daher ist es wichtig das ihr bei der Installation von Python ebenfalls PIP installiert.

---



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
/
```

Mit der Einstellung **Suffix** legen wir die Endung unseres Logfiles fest.

Die Einstellung **SortYear** legt fest, dass die Logfiles nach Jahren sortiert werden. Wenn bei **SortMonth** "yes" angegeben wird, werden die Logfiles zusätzlich nach Monaten sortiert.

Wenn man **Cronjob** auf "yes" setzt, wird das Startdatum übergangen, und es wird nur das Logfile des aktuellen Tages heruntergeladen. Stellt man gleichzeitig **Yester** auf "yes", wird das Logfile vom Vortag heruntergeladen.

Damit kann man beispielsweise einen Cronjob unter Linux einrichten, der jeden Tag um 0:15 Uhr startet und sicherstellt, dass man das gesamte Logfile vom Vortag erhält.

Bei **Sleep** handelt es sich um eine Kompatibilitätseinstellung. Sollte der Webserver des Speichers mal nicht hinterherkommen, führt das zu einem Fehler. Sollten mehr Fehler als unter **ErrorCount** angegeben auftreten, wird für x Sekunden gewartet und der Webserver des Speichers entlastet.




