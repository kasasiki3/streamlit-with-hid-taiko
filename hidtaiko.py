import streamlit as st
import usb.core
import usb.backend.libusb1

# USB Vendor IDとProduct IDを設定します
VENDOR_ID = 0x0f0d  # ここにデバイスのVendor IDを入力してください
PRODUCT_ID = 0x0092  # ここにデバイスのProduct IDを入力してください

# USBデバイスに接続する関数
def connect_to_usb_device():
    # Vendor IDとProduct IDを指定してUSBデバイスを検索します
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
    
    if dev is None:
        st.write("デバイスが見つかりませんでした")
    else:
        st.write("デバイスが見つかりました")
        # デバイスに対して操作を行うコードをここに追加します

# Streamlitアプリケーションの設定
st.title('WebUSBを使用するアプリケーション')

# デバイスに接続するボタンを追加します
if st.button('デバイスに接続'):
    connect_to_usb_device()
