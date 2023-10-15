import streamlit as st
import os

pw = st.text_input("비번을 넣으세요", type="password")
if pw == st.secrets["pw"]:    
    tab1, tab2, tab3 = st.tabs(["파일 업로드", "파일삭제", "파일 다운로드"])
    with tab1:
        # 파일 업로드
        with st.form("upload_Form"):
            st.subheader("파일 업로드")
            uploaded_file = st.file_uploader("업로드 파일을 선택하세요")
            if uploaded_file is not None:
                with open(uploaded_file.name,"wb") as f:
                    f.write(uploaded_file.getbuffer())
            submitted = st.form_submit_button("파일저장")
            if submitted:
                st.info(f'{uploaded_file.name}이 업로드 되었습니다.')
    
    with tab2:
        # 파일 삭제
        file_list = os.listdir()
        file_list_wanted = []
        for file in file_list:
            # root, extension = os.path.splitext(file)
            # if extension.replace('.','') in extList:
            if file != 'sttxtFile.py' and file[0] != '.':
                file_list_wanted.append(file)
        selected_file = st.selectbox('삭제하고 싶은 파일을 선택하세요.',file_list_wanted)
        submitted1 = st.button("삭제")
        if submitted1 and selected_file:
            os.remove(os.path.join(os.getcwd(),selected_file))
            st.warning(f'"{selected_file}" 파일이 삭제되었습니다.')
            st.info("사이트를 다시 로드하세요(재실행)")
    
    with tab3:
        #form에서는  download_button을 쓸 수 없어서 form 사용 안함
        # 다운로드
        file_list = os.listdir()
        file_list_wanted = []
        for file in file_list:
            root, extension = os.path.splitext(file)
            # if extension.replace('.','') in extList:
            if file != 'sttxtFile.py' and file[0] != '.':
                file_list_wanted.append(file)
        selected_file = st.selectbox('파일선택',file_list_wanted)
        if selected_file:
            with open(selected_file,'rb') as f:
                if st.download_button('다운로드', f, selected_file):
                    st.success(f'{selected_file} 파일이 다운로드 되었습니다.')
