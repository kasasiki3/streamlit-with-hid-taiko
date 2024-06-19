import streamlit as st
import asyncio
import websockets

async def get_ports():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("list_ports")
        ports = await websocket.recv()
        return ports

async def connect_to_port(port_name):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(f"connect:{port_name}")
        response = await websocket.recv()
        st.write(response)

st.title("Serial Port Selector")

if st.button("Get Ports"):
    ports = asyncio.run(get_ports())
    st.write(ports)

port_name = st.text_input("Enter port name")

if st.button("Connect"):
    asyncio.run(connect_to_port(port_name))
