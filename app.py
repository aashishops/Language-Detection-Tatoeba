import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title='Language Detection')
st.title("LANGUAGE DETECTION :scroll:")
st.subheader("This is a Language Detector.")
st.write("Type a sentence in the below box to identify the Language.")
text = st.text_area("Enter the sentence to identify")
with open('lang_model.pkl','rb')as f:
    mod= pickle.load(f)
prediction = mod.predict([text])[0]
prediction = ''.join(prediction)
df = pd.read_csv(r'lang_abr.csv')
abr = df[(df["lang"]==prediction)]
if st.button("Detect"):
    st.write('The Detected Language is ',abr['abr'].item(),'.')
    
