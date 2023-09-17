import streamlit as st
file = open("TextFile.txt", "w")
file.write("Hello~ \n")
file.close()
file = open("TextFile.txt", "r")
a = file.readline()
st.write(a)
