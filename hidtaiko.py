import streamlit as st
import serial
import time

# Arduinoのシリアルポートを指定します
SERIAL_PORT = 'COM3'  # 実際のポートに置き換えてください
BAUD_RATE = 9600

@st.cache_resource
def get_serial_connection():
    return serial.Serial(SERIAL_PORT, BAUD_RATE)

def read_from_arduino(serial_connection):
    if serial_connection.in_waiting > 0:
        return serial_connection.readline().decode('utf-8').strip()
    return None

st.title('Arduino Serial Communication')

# シリアル接続を取得
ser = get_serial_connection()

# Arduinoに送信するメッセージを入力
message = st.text_input('Message to Arduino', '')

if st.button('Send'):
    if message:
        ser.write(message.encode('utf-8'))
        st.write('Message sent to Arduino:', message)

# Arduinoからのメッセージを表示
st.write('Message from Arduino:')
output = read_from_arduino(ser)
if output:
    st.write(output)
else:
    st.write('No new messages.')

# シリアル接続を閉じる
if st.button('Close Connection'):
    ser.close()
    st.write('Serial connection closed.')
