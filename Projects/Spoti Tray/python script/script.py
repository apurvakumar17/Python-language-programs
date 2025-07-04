import asyncio
import threading
import websockets
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

clients = set()
ws_loop = None  # to hold the asyncio loop for messaging

def create_image():
    # Simple icon: dark green play circle on a green background
    # Background green (e.g., a brighter green)
    img = Image.new('RGB', (64, 64), (0, 255, 0))
    draw = ImageDraw.Draw(img)
    # Dark green for the polygon
    draw.polygon([(25, 20), (45, 32), (25, 44)], fill=(0, 100, 0))
    return img

async def handler(websocket):
    clients.add(websocket)
    try:
        async for _ in websocket:
            pass
    finally:
        clients.remove(websocket)

def run_ws_server():
    global ws_loop
    ws_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(ws_loop)

    async def start():
        async with websockets.serve(handler, "localhost", 6969):
            print("WebSocket server running on ws://localhost:6969")
            await asyncio.Future()  # run forever

    ws_loop.run_until_complete(start())

def toggle_play_pause(icon, item):
    for ws in clients.copy():
        try:
            asyncio.run_coroutine_threadsafe(ws.send("toggle"), ws_loop)
        except:
            clients.discard(ws)

# Tray icon setup
icon = Icon("SpotifyControl")
icon.icon = create_image()
icon.menu = Menu(MenuItem("Play/Pause Spotify", toggle_play_pause), MenuItem("Quit", lambda i: icon.stop()))

# Start WebSocket server in background
threading.Thread(target=run_ws_server, daemon=True).start()

# Run tray icon
icon.run()
