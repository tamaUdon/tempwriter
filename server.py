import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(handler, "localhost", 8989):
        await asyncio.Future()  # run forever

asyncio.run(main())