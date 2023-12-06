import streamlit as st
import pickle


# loading the saved model
loaded_model = pickle.load(open('spam-detector.sav', 'rb'))
vectorizer = pickle.load(open('tfidf-vectorizer.sav', 'rb'))


def detect_spam_emails(input_data):
    """ This is a function that detects and classifies whether an email is a spam or ham. """
    
    input_data_transformed = vectorizer.transform([input_data])

    prediction = loaded_model.predict(input_data_transformed)

    if prediction[0] == 0:  # if mail is spam
        return st.error('Spam mail detected!', icon='🚩')

    else:    
        return st.success('Hakuna matata! This is a ham mail.', icon='✅')

