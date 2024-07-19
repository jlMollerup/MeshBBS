import meshtastic
import meshtastic.serial_interface
import time
from pubsub import pub

import pprint

# By default will try to find a meshtastic device,
# otherwise provide a device path like /dev/ttyUSB0
interface = meshtastic.serial_interface.SerialInterface()
# or something like this
# interface = meshtastic.serial_interface.SerialInterface(devPath='/dev/cu.usbmodem53230050571')

# or sendData to send binary data, see documentations for other options.
# interface.sendText("hello mesh")
print(interface.getMyUser())


# interface.localNode.setOwner('hackBBS','BBS')
# # update a value
# print('Changing a preference...')
# ourNode.localConfig.position.gps_update_interval = 60

# print(f'Our node preferences now:{ourNode.localConfig}')
# ourNode.writeConfig("position")




def onReceive(packet, interface): # called when a packet arrives
    # print(f"Received: {packet}")
    pprint.pprint(packet)

    print(f"{packet['decoded']} er fra {packet['from']}")

    interface.sendText('davs',packet['from'])
    


def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    # interface.sendText("hello mesh")
    pass

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")

while True:
    time.sleep(1000)
interface.close()