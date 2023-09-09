import yaml
import sys
from dotenv import load_dotenv

###########################################################################
# Umgebungsvariablen lesen
load_dotenv()

###########################################################################
# Laden der YAML Konfigurationsdatei.
# Es werden alle Parameter der Konfiguration zurückgegeben
def read(config_file):
    try:
        with open(config_file) as fileStream:
            loaded = yaml.safe_load(fileStream)
    except FileNotFoundError:
        print(f"Konnte Konfigurationsdatei '{config_file}' nicht finden")
        sys.exit(1)
    except yaml.YAMLError as exception:
        print(f"Fehler beim Laden der Konfigurationsdatei '{config_file}': {exception}")
        sys.exit(1)
    
    if loaded:
        return loaded
    else:
        print(f"Konnte Konfigurationsdatei '{config_file}' nicht laden")
        sys.exit(1)

# Beispielaufruf:
# config_data = read("config.yaml")
# if config_data:
#     print(config_data)
