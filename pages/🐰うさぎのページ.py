
import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
'<p><span style = "background-color:#ffb6c1;color:#ffffff;font-size: 30px;font-family:Kosugi Maru;"> ★　うさぎのページ　★ </span></p>',
unsafe_allow_html=True)

# path=".//main/もち.jpg"
path="https://github.com/happyyumeno/coderdojotckw/blob/master/main/%E3%82%82%E3%81%A1.JPG?raw=true"
st.image(f"{path}", use_column_width=True)

