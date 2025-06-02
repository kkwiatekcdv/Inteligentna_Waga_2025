import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=smart-scale-iothub.azure-devices.net;DeviceId=smart-scale-device;SharedAccessKey=qCkF4Nsge+Zk3UG3h0CpZFUt0P52nOKsp0HKwo8RcyI="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

while True:
    weight = round(random.uniform(50, 100), 2)
    message = Message(f'{{"weight": {weight}}}')
    client.send_message(message)
    print(f"Wysłano dane: {weight} kg")
    time.sleep(10)