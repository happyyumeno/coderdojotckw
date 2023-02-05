
import streamlit as st

st.set_page_config(layout="wide")

# txt1 = '**<p style="color:#9932cc;font-size: 50px;">作品紹介ページ</p>**'
# st.write(txt1, unsafe_allow_html=True)

st.markdown(
'<p><span style = "background-color:#008080;color:#ffffff;font-size: 30px;font-family:Kosugi Maru;"> ★　作品紹介　★ </span></p>',
unsafe_allow_html=True)

st.markdown(
'**<p><span style = "color:#008080;font-size: 20px;font-family:Kosugi Maru;">2023年1月14日開催</span></p>**',
unsafe_allow_html=True)

# https://github.com/happyyumeno/coderdojotckw/blob/master/%E7%AC%AC40%E5%9B%9E/1.jpg?raw=true

for i in list(range(0,6)):
    path="https://github.com/happyyumeno/coderdojotckw/blob/master/%E7%AC%AC40%E5%9B%9E/"
    path=path+str(i+1)+".jpg?raw=true"
    st.header("NO."+str(i+1))
    st.image(f"{path}.JPG", use_column_width=True)
