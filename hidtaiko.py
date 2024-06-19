import streamlit as st
import serial
from serial.tools import list_ports

def list_serial_ports():
    return [port.device for port in list_ports.comports()] #シリアルポートのリスト取得

port_name = st.selectbox("Select PORT", list_serial_ports()) #シリアルポート選択メニュー表示

if st.button('Connect'):# シリアルポートに接続
    if not port_name:
        st.error("No port selected. Please select a port.") #
    else:
        try:
            
            serialPort = serial.Serial(port=port_name, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
            st.success(f"Connected to {port_name}")

            # シリアルデータ送信
            serialPort.write(b'hello') 

            # しりあるデータ受信（例）
            if serialPort.in_waiting > 0:
                serialData = serialPort.readline()
                st.write(serialData.decode('Ascii'))

            # シリアルポートを閉じる
            serialPort.close()
        except serial.SerialException as e:
            st.error(f"SerialException: {e}")
        except PermissionError as e:
            st.error(f"PermissionError: {e.strerror}. You might need to run this application with higher privileges.")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

