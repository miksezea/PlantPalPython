from socket import *
import time
import json
from datetime import datetime
from miflora.miflora_poller import MiFloraPoller, MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from btlewrap import GatttoolBackend


serverName = '255.255.255.255'
serverPort = 7000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
counter = 1

while counter < 21:
        poller = MiFloraPoller(mac='C4:7C:8D:64:3F:25', backend=GatttoolBackend)

        if counter == 1:
                print('Battery: ', poller.parameter_value(MI_BATTERY))

        now = datetime.now()

        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        tid = now.strftime("%H:%M:%S")
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        obj = {
          "DateTime": date_time,
          "Temperature": poller.parameter_value(MI_TEMPERATURE),
          "Moisture": poller.parameter_value(MI_MOISTURE),
          "Light": poller.parameter_value(MI_LIGHT),
          "Conductivity": poller.parameter_value(MI_CONDUCTIVITY)
        }

        message = json.dumps(obj)
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        print('Data sent...', counter )
        counter += 1
        time.sleep(5)

clientSocket.close()
