from openai import OpenAI
import streamlit as st
import os
import time
from dotenv import load_dotenv
from src.prompts import *

# Load environment variables from .env
load_dotenv()
New_Conversation = 0
# =============================================================================
# INITIAL SETUP & SESSION STATE
# =============================================================================
if 'model' not in st.session_state:
    # Initialize the client with your API key (make sure OPENAI_API_KEY is set)
    st.session_state['model'] = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []  # List of messages: each is a dict with keys "role" and "content"

if 'legal_mode' not in st.session_state:
    st.session_state['legal_mode'] = False


# =============================================================================
# SIDEBAR CONTROLS
# =============================================================================
st.sidebar.title('Legal Assistant Options')
# Checkbox to select the mode. If checked, legal mode is activated.
legal_mode = st.sidebar.checkbox("Legal Interpretation Mode", value=False)
st.session_state['legal_mode'] = legal_mode

# Button to start a new conversation (i.e. a new thread in legal mode)
if st.sidebar.button("New Conversation"):
    st.session_state['conversation'] = []
    # When starting in legal mode, automatically begin with the instruction prompt.
    if st.session_state['legal_mode']:
        st.session_state['conversation'].append({
            "role": "user",
            "content": instruction_prompt
        })

# =============================================================================
# PAGE TITLE AND CURRENT CONVERSATION DISPLAY
# =============================================================================
st.title('OpenAI ChatGPT')

# Display all previous conversation messages in order (rendered as Markdown)
for msg in st.session_state['conversation']:
    print((len(st.session_state("New Conversation")) >1))
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])


# =============================================================================
# HELPER FUNCTIONS FOR OBTAINING RESPONSES
# =============================================================================
def get_legal_response(conversation, initial_flag=0):
    client = st.session_state['model']

    # Create Initial Message
    print(conversation)
    combined_conversations = st.session_state['conversation'] + conversation
    print(combined_conversations)

    print(combined_conversations)
    thread = client.beta.threads.create(messages=combined_conversations)
    run = client.beta.threads.runs.create_and_poll(thread_id=thread.id,
                                          assistant_id=os.getenv("Full_Knowledge_Library_Assistant_ID"))

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    output_text = f"**Response:**\n\n{message_content.value}\n\n"
    if citations:
        output_text += "**Citations:**\n\n" + "\n".join(citations)

    return output_text



def get_general_response(conversation, temperature=0.7, max_tokens=1024, stream=True):
    """
    Use the general ChatGPT chat API (streaming response) with the conversation history.
    """
    client = st.session_state['model']
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=conversation,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True
    )
    # Here we assume st.write_stream() handles the streaming display and returns the final text.
    response_text = st.write_stream(stream)

# =============================================================================
# CHAT INPUT AND RESPONSE HANDLING
# =============================================================================
user_input = st.chat_input("Enter your query")
if user_input:
    # Append the user's message to the conversation history.
    st.session_state['conversation'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Depending on the mode, get the response using the appropriate function.
    if st.session_state['legal_mode']:
        response = get_legal_response(st.session_state['conversation'])
        with st.chat_message("assistant"):
            st.markdown(response)
    else:
        with st.chat_message("assistant"):
            response = get_general_response(st.session_state['conversation'])

    # Display the assistant's response.
    #with st.chat_message("assistant"):
    #    st.markdown(response)

    # Append the assistant’s reply to the conversation history.
    st.session_state['conversation'].append({"role": "assistant", "content": response})
