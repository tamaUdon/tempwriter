import asyncio
import websockets

# ここでhand-gestureを認識して

def recognize():


def _recognize_gu():

def _recognize_choki():

def _recognize_pa():

# メッセージとして送る



async def handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(handler, "localhost", 8989):
        await asyncio.Future()  # run forever

asyncio.run(main())