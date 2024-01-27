from mails.detect import detect_spam_emails
import streamlit as st
import numpy as np
import pickle


def main():
    """ This is a function used to design the default webpage.  """
    
    st.set_page_config(
        page_title='SpamSlayer',
        page_icon=':envelope:',
        layout='centered'
    )

    # loading custom css file
    with open('static/css/styles.css') as stylesheet:
        st.markdown(f'<style>{stylesheet.read()}</style>', unsafe_allow_html=True)

    st.title(':envelope: :blue[Spam]Slayer')
    st.subheader('This is a web-based spam mail detector')
    st.divider()
    
    
    with st.form('emails_forms'):
        email_msg = st.text_area(
            label='Email',
            placeholder='Type an email text here ...'
        )

        submitted = st.form_submit_button('Submit')

        if submitted:       # if button is clicked
            if email_msg:   # if text area is not blank
                message = detect_spam_emails(email_msg)
                return message
            else:
                st.warning('Please enter an email', icon='⚠️')


if __name__ == '__main__':
    main()