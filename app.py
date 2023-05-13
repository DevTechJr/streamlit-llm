import streamlit as st
import openai
from datetime import datetime
from streamlit.components.v1 import html
import pandas as pd

with st.sidebar:
    st.subheader("LLM Name Generator (Da-vinci 002)")

    st.markdown("""
    # About the project:
   A simple demonstration of Streamlit's potential when paired up with a LLM model. 
    """)
    
    st.markdown("""
    # How it works:
    Enter information into the input fields provided. Using the user input, a LLM will generate some relevant names for you!
    """)
   


input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=2:
    st.markdown("""
    # LLM Idea Generator (Da-vinci 002)
    """)
    input_text = st.text_input("Generate some names relevant to...", disabled=False, placeholder="E.g. Harry Potter")
    st.session_state['output'] = st.session_state['output'] + 1
else:
    # input_text = st.text_input("Brainstorm ideas for", disabled=True)
    st.info("Thanks for trying it out! Refresh the tab to try again!")
    st.markdown('''
    <a target="_blank" style="color: black" href="">
        <button class="btn">
            Tweet about this!
        </button>
    </a>
    <style>
    .btn{
        display: inline-flex;
        -moz-box-align: center;
        align-items: center;
        -moz-box-pack: center;
        justify-content: center;
        font-weight: 400;
        padding: 0.25rem 0.75rem;
        border-radius: 0.25rem;
        margin: 0px;
        line-height: 1.6;
        color: #fff;
        background-color: #00acee;
        width: auto;
        user-select: none;
        border: 1px solid #00acee;
        }
    .btn:hover{
        color: #00acee;
        background-color: #fff;
    }
    </style>
    ''',
    unsafe_allow_html=True
    )



if input_text:
    prompt = "Brainstorm names from the world of "+str(input_text)
    if prompt:
        openai.api_key = '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'
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
        brainstorming_output = response['choices'][0]['text']
        today = datetime.today().strftime('%Y-%m-%d')
        topic = "Brainstorming names for: "+input_text+"\n@Date: "+str(today)+"\n"+brainstorming_output
        
        st.info(brainstorming_output)
        filename = "brainstorming_"+str(today)+".txt"
        btn = st.download_button(
            label="Download txt",
            data=topic,
            file_name=filename
        )
        fields = [input_text, brainstorming_output, str(today)]
        
