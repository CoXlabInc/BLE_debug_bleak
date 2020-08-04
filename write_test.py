import asyncio
import sys
from bleak import BleakScanner
from bleak import BleakClient

if len(sys.argv) <= 4:
    print("Insufficient argument!")
    sys.exit()

SERVICE_UUID = sys.argv[1]
CHARACTERISTIC_UUID = sys.argv[2]
WRITE_STR = sys.argv[3]
NEED_RESPONSE = sys.argv[4]



found = 0
mac_addr = ""
async def run():
    global found, mac_addr
    devices = await BleakScanner.discover()
    print("found [%d] devices!" % len(devices))
    for d in devices:
        if (d.name == "Coxlab, Inc."):
            found = 1
            mac_addr = d.address

async def print_services(mac_addr: str, loop: asyncio.AbstractEventLoop):
    service_flag = 0
    char_flag = 0
    try:
        async with BleakClient(mac_addr, loop=loop, timeout=5.0) as client:
            svcs = client.services
            for service in svcs:
                if (service.uuid == SERVICE_UUID):
                    print("Service Found!")
                    service_flag = 1
                    for char in service.characteristics:
                        if (char.uuid == CHARACTERISTIC_UUID):
                            print("Characteristic Found! Write Start")
                            char_flag = 1
                            await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray(WRITE_STR.encode()), NEED_RESPONSE)
                            break
    except:
        print("not connected T.T")
    if ( (not service_flag) and connect_flag):
        print("There is No Service : " + SERVICE_UUID)
    if ( (not char_flag) and connect_flag):
        print("There is No CHARACTERISTIC_UUID : " + CHARACTERISTIC_UUID)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

if (found) :
    print("Find! Connect start : " + mac_addr)
    loop2 = asyncio.new_event_loop()
    loop2.run_until_complete(print_services(mac_addr,loop2))
else:
    print("Sorry, There is No Coxlab, Inc.")
