from datetime import date, datetime, timedelta
import os
import time
from config_api import *
import warnings
import requests


###########################################################################
# Erstellen der URL mit der das Logfile aus dem Speicher ausgelesen
# werden kann. Diese wird gebildet aus der IP-Adresse des Speichers und
# einem Datum
# Beispiel: https://[IP SPEICHER]/Log/JJJJ/MM/TT.log
def url_logfile(datum):
    conf = config.read(os.getenv("CONFIG_FILE"))
    ip = conf["speicher"]["ip"]
    url = "https://" + ip + "/Log/" + (datum.strftime("%Y/%m/%d")) + ".log"
    return url


###########################################################################
# Abrufen des Logfiles welches unter der URL abgelegt ist.
# Sollte das Lesen des Logfiles einen Fehler verursachen wird der
# Variablen error der Wert eins zugewiesen.
def lesen_logfile(url):
    response = ""
    error = 0
    try:
        warnings.filterwarnings('ignore')
        response = requests.get(url, verify=False)  # SSL-Verifikation deaktivieren
        response = response.text.replace("\n", "")   # Entfernt ein zusätzliches Enter
        '''
        if response.status_code == 200:
        # Verarbeitung der Antwort
            print(response.text)
        else:
            print(f'Fehler beim Herunterladen der Webseite. Statuscode: {response.status_code}')
        '''
    except:
        error = 1
    return response, error


###########################################################################
# Startdatum in ein "ordentliches" Datumsformat umwandeln
def start_datum():
    conf = config.read(os.getenv("CONFIG_FILE"))
    datum_format = "%d.%m.%Y"
    begin_datum = date(
        datetime.strptime(conf["logfile"]["startDatum"], datum_format).year,
        datetime.strptime(conf["logfile"]["startDatum"], datum_format).month,
        datetime.strptime(conf["logfile"]["startDatum"], datum_format).day,
    )
    return begin_datum


###########################################################################
# Gestriges Datum yyyy-mm-tt
def gestern_datum():
    return date.today() - timedelta(1)


###########################################################################
# Heutiges Datum yyyy-mm-tt
def heute_datum():
    return date.today()


###########################################################################
# Berechnet wie viele Tage zwischen datum1 und datum2 liegen.
# Das neuste Datum muss als Erstes und das ältere Datum als zweites
# angegeben werden. Es wird +1 addiert damit auch das neuste Datum (Tag)
# mit berechnet wird.
def div_days(datum1, datum2):
    days = int((datum1 - datum2).days) + 1
    return days


###########################################################################
# Erzeugen des Dateipfads ohne Dateiname
# Beispiel: ../logfiles/2021/9/
def save_pfad(datum):
    system_pfad = ""
    conf = config.read(os.getenv("CONFIG_FILE"))
    # Entscheiden, ob die Logfiles relativ zum Skriptordner angelegt
    # werden. Releativ bedeutet, das der Ordner "Logfiles" unterhalb des
    # Ordners angelegt wird, aus dem das Skript aufgerufen wurde.
    #
    # Absolut bedeutet, das der Ordner Logfile überall im Dateisystem angelegt
    # werden kann.
    if conf["logfile"]["pfadart"] == "relativ":
        system_pfad = (
            os.path.dirname(__file__) + "/" + conf["logfile"]["pfadrelativ"] + "/"
        )
    elif conf["logfile"]["pfadart"] == "absolut":
        system_pfad = conf["logfile"]["pfadabsolut"] + "/"

    # Ist sortyear und sortmonth in der Konfigurationsdatei auf YES
    # wird der Pfad ..../yyyy/mm generiert.
    #
    # Wenn sortmonth = no ist wird ein der Pfad ..../mm generiert
    #
    # Wenn sortyear = no eingestellt ist dann wird nur der Standardpfad
    # generiert. Die Einstellung sortmonth wird dabei außeracht gelassen.
    if (conf["logfile"]["sortyear"] is True) and (conf["logfile"]["sortmonth"] is True
    ):
        datei_pfad = str(datum.year) + "/" + str(datum.month) + "/"
    else:
        datei_pfad = str(datum.year) + "/"

    if conf["logfile"]["sortyear"] is False:
        datei_pfad = ""

    logfile_pfad = system_pfad + datei_pfad
    return logfile_pfad


###########################################################################
# Erzeugen des Dateinamens
# Beispiel: 2021-09-03.txt
def dateiname(datum):
    conf = config.read(os.getenv("CONFIG_FILE"))
    datei_name = str(datum) + "." + conf["logfile"]["suffix"]
    return datei_name


###########################################################################
# Anlagen des Pfads so das alle Verzeichnisse, die in diesem Moment benötigt
# werden, angelegt werden. Es wird aber nicht die, gesamt Verzeichnisstruktur angelegt
def pfad_anlegen(log_pfad):
    if not os.path.isdir(log_pfad):
        os.makedirs(log_pfad)


###########################################################################
# Steuern dass das Logfile (herunterladen und Pfad auf Datenträger zuweisen)
# wird und in den passenden Pfad
# geschrieben wird.
def save_logfile(datum):
    conf = config.read(os.getenv("CONFIG_FILE"))
    log_pfad = save_pfad(datum)
    log_dateiname = dateiname(datum)
    url = url_logfile(datum)

    if not os.path.isfile(log_pfad + log_dateiname):
        # Datei ist nicht vorhanden und wird geschrieben
        datei_write = True
        status = "W"
    else:
        if conf["logfile"]["rewrite"] is True:
            # Datei ist vorhanden und wird überschrieben
            datei_write = True
            status = "W+"
        else:
            # Datei ist vorhanden und wird NICHT überschrieben
            datei_write = False
            status = "O"

    if datei_write:
        for fehler_durchlauf in range(0, conf["logfile"]["errorcount"]):
            html, error = lesen_logfile(url)
            if error < 1:
                pfad_anlegen(log_pfad)
                datei = open(log_pfad + log_dateiname, conf["logfile"]["writemode"])
                datei.write(html)
                datei.close()
            else:
                status = "E"
                time.sleep(conf["logfile"]["sleep"])

            print(
                "Status: "
                + status
                + " | URL: "
                + url
                + " | Datei: "
                + log_pfad
                + log_dateiname
            )
            if error < 1:
                break
