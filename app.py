import streamlit as st
import pickle
import pandas as pd
import joblib
st.set_page_config(page_title='Language Detection')

st.title("LANGUAGE DETECTION :scroll:")
st.subheader("This is a Language Detector.")
st.write("Type a sentence in the below box to identify the Language.")
text = st.text_area("Enter the sentence to identify")
mod = joblib.dump('language_model.pkl')
prediction = mod.predict([text])[0]
prediction = ''.join(prediction)
df = pd.read_csv(r'lang_abr.csv')
abr = df[(df["lang"]==prediction)]

if st.button("Detect"):
    st.write('The Detected Language is ',abr['abr'].item(),'.')
    
