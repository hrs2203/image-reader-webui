import streamlit as st
import os

## ======= static file locaton ============
## ========== server code =================

@st.cache
def homepage():
	st.title("Image Caption System")

	uploaded_file = st.file_uploader("Upload Files (.png and .jpg only)",type=['png','jpg'])

	# use our model here and show its caption.
	if uploaded_file is not None:
		file_details = {
			"FileName":uploaded_file.name,
			"FileType":uploaded_file.type,
			"FileDescription": "Lorem Ipsem for now."
		}
		st.image(uploaded_file, use_column_width=True)
		st.write(file_details)

