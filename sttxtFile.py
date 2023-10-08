import streamlit as st
import os

uploaded_file = st.file_uploader("업로드 파일을 선택하세요",type=['txt'])
if uploaded_file is not None:
    st.write(uploaded_file)
file_list = os.listdir('./')
file_list_wanted = []
extList = ['txt']
for file in file_list:
    root, extension = os.path.splitext(file)
    if extension.replace('.','') in extList:
        if file != 'requirements.txt':
            file_list_wanted.append(file)
selected_file = st.selectbox('확인하고 싶은 파일을 선택하세요.',file_list_wanted)
submitted = st.button("파일내용확인")
if selected_file and submitted:
    try:
        with open(selected_file,'r', encoding='utf-8') as f:
            firstline = f.readline().replace("  ","{2칸}").replace("\t","{tab}")
            secondline = f.readline().strip().replace("  ","{2칸}").replace("\t","{tab}")
            dispTxt = f"""[1번째라인] {firstline}
[2번째라인] {secondline}\n
[총 라인수] {len(f.readlines())}"""
            st.success(dispTxt)
            # st.write(len(f.readlines()))
    except:
        st.warning('파일을 메모장에서 "utf-8"로 다시 저장하세요')

