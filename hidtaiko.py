import streamlit as st

# HTMLテンプレートの定義
html_template = """
<!DOCTYPE html>
<html>
  <head>
    <title>WebUSB Console</title>
  </head>
  <body>
    <h1>WebUSB Console</h1>
    <button id="connect">Connect</button>
    <textarea id="output" rows="10" cols="50"></textarea>
    <input id="input" type="text" />
    <button id="send">Send</button>
    
    <script>
      let device;
      document.getElementById('connect').addEventListener('click', async () => {
        try {
          device = await navigator.usb.requestDevice({ filters: [{ vendorId: 0x2341 }] });
          await device.open();
          await device.selectConfiguration(1);
          await device.claimInterface(2);
          console.log('Connected to device:', device);
          readLoop();
        } catch (error) {
          console.error('There was an error:', error);
        }
      });

      document.getElementById('send').addEventListener('click', async () => {
        let input = document.getElementById('input').value;
        let encoder = new TextEncoder();
        let data = encoder.encode(input);
        await device.transferOut(4, data);
      });

      async function readLoop() {
        while (true) {
          try {
            const result = await device.transferIn(5, 64);
            let decoder = new TextDecoder();
            document.getElementById('output').value += decoder.decode(result.data);
          } catch (error) {
            console.error('There was an error:', error);
            break;
          }
        }
      }
    </script>
  </body>
</html>
"""

st.set_page_config(page_title="WebUSB with Streamlit")

st.title('WebUSB with Streamlit')

# HTMLコードを埋め込む
st.markdown(html_template, unsafe_allow_html=True)
