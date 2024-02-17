import streamlit as st
from pathlib import Path
import os

st.title("녹화영상 다운로드")
st.write("다운로드하고 싶은 파일을 선택하세요.")

dir_path = Path(".", "/opt/openvidu/recordings")
files = [f for f in os.listdir(dir_path) if not f.startswith('.')]  

try:
    if files:
        for file in files:
            st.download_button(
                label=file,
                data=open(dir_path.joinpath(file).joinpath(file + ".mp4"), "rb"),
                file_name=file + ".mp4"
            )
    else:
        st.write("다운로드 할 파일이 존재하지 않습니다.")
except Exception as e:
    print("오류가 발생했습니다. 관리자에게 문의하세요.")
    print(e)
