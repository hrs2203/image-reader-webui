import streamlit as st
import os

## ======= static file locaton ============

FILE_DIRECTORY = os.path.join(".","uploadedFiles")

## ========== server code =================

st.title("Image Caption System")

uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])

if uploaded_file is not None:
	# use our model here and show its caption.



	file_details = {
		"FileName":uploaded_file.name,
		"FileType":uploaded_file.type,
		"FileSize":uploaded_file.size,
		"FileDescription": "Lorem Ipsem for now."
	}
	st.image(uploaded_file, height=250, width=250)
	st.write(file_details)



