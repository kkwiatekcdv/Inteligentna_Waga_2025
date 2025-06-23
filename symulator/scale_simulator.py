import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# TUTAJ CONNECTION STRING
CONNECTION_STRING = "TwojConnectionStringTutaj"

# Szablon wiadomości w formacie JSON
SZABLON_WIADOMOSCI = '{{"waga": {waga}, "tluszcz": {tluszcz}, "woda": {woda}}}'

# Tworzenie klienta IoT
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("Symulator inteligentnej wagi uruchomiony (tryb testowy: 10 pomiarów)...")

try:
    for i in range(10):
        # Generowanie losowych danych pomiarowych
        waga = round(random.uniform(60.0, 100.0), 1)  # kg
        tluszcz = round(random.uniform(10.0, 35.0), 1)  # %
        woda = round(random.uniform(45.0, 70.0), 1)  # %

        # Tworzenie wiadomości JSON
        wiadomosc_tekst = SZABLON_WIADOMOSCI.format(waga=waga, tluszcz=tluszcz, woda=woda)
        wiadomosc = Message(wiadomosc_tekst)

        # Wysyłanie wiadomości do IoT Hub
        print(f"[{i+1}/10] Wysyłam: {wiadomosc_tekst}")
        client.send_message(wiadomosc)

        # Czekaj 5 sekund przed kolejnym pomiarem
        time.sleep(5)

except Exception as e:
    print(f"Wystąpił błąd: {e}")

finally:
    client.disconnect()
    print("Symulator zakończył pracę (tryb testowy)")
