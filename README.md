# Language Detector 📜
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](https://github.com/aashishops/Language-Detection-Tatoeba/tree/main#readme) 
[![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](https://language-detector.streamlit.app/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://language-detector.streamlit.app/)

## Introduction
#### Welcome to the Language Detector! 
Language detection is a tool designed to identify the language of a given text using natural language processing (NLP) techniques. That involves determining the language in which a given text is written. This provides a simple and efficient language detection system using scikit-learn pipeline to combine a TF-IDF vectorizer with a Logistic Regression classifier to detect the language of a given text. The model is trained on the Tatoeba dataset, a large corpus of parallel texts in over 220 languages.

## How it works
The model used in this project is a Pipeline object with two steps:

The TfidfVectorizer object converts the text data into a TF-IDF matrix. The TF-IDF matrix is a representation of the text data where each word is weighted based on its frequency in the text and its inverse document frequency (IDF). The IDF is a measure of how important a word is to a language.

The LogisticRegression object is then trained to predict the language of each text based on the TF-IDF matrix. The LogisticRegression object is a machine learning classifier that is trained to predict the probability of a text belonging to a certain class. In this case, the classes are the different languages in the Tatoeba dataset.

In summary, Tatoeba Language Detection works by converting text into numerical features using TF-IDF vectorization and then using a Logistic Regression classifier to predict the language based on learned patterns. This process allows the module to detect the language of input text accurately, even for languages it has not seen during training.




## Demo

 [Click here <img src="https://raw.githubusercontent.com/aashishops/Language-Detection-Tatoeba/main/images/streamlit-logo-1A3B208AE4-seeklogo.com.png" alt="Streamlit Logo" width="25">](https://language-detector.streamlit.app/) to Detect Languages

![Demo](https://raw.githubusercontent.com/aashishops/Language-Detection-Tatoeba/9039379470488dce59d57c78d6f606016e6e86dd/images/demo.gif)
