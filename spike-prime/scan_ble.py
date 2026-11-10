import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover(timeout=5)
    for device in devices:
        print(device.name, device.address)

asyncio.run(main())