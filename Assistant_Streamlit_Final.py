import os
import io
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from prompts.prompts import *

# Load environment variables from .env
load_dotenv()

# -----------------------------------------------------------------------------
# INITIAL SETUP: Initialize the OpenAI client and conversation history in session state
# -----------------------------------------------------------------------------
if 'model' not in st.session_state:
    # Instantiate the OpenAI client with your API key.
    st.session_state['model'] = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if 'conversation' not in st.session_state:
    # This list will hold the conversation messages.
    st.session_state['conversation'] = []

if 'new_conversation_flag' not in st.session_state:
    st.session_state['new_conversation_flag'] = 0

# =============================================================================
# SIDEBAR CONTROLS
# =============================================================================
st.sidebar.title('Legal Assistant Options')

# Button to start a new conversation
if st.sidebar.button("New Conversation"):
    st.session_state['conversation'] = []  # Clear conversation history
    st.session_state['new_conversation_flag'] = 0  # Reset flag

# -----------------------------------------------------------------------------
# PAGE TITLE
# -----------------------------------------------------------------------------
st.title("Legal Response Chatbot")

# Display all previous conversation messages in order (rendered as Markdown)
for msg in st.session_state['conversation']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# -----------------------------------------------------------------------------
# HELPER FUNCTION: get_legal_response
# -----------------------------------------------------------------------------
def get_legal_response(conversation):
    client = st.session_state['model']

    # Create a new thread for the conversation.
    thread = client.beta.threads.create(messages=conversation)
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=os.getenv("Full_Knowledge_Library_Assistant_ID")
    )

    # Retrieve the messages from the thread.
    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    # For simplicity, assume the first message contains the response.
    message_content = messages[0].content[0].text
    citations = []

    # Replace annotated text with citation markers and build a citations list.
    for index, annotation in enumerate(message_content.annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    # Format the output text.
    output_text = f"**Response:**\n\n{message_content.value}\n\n"
    if citations:
        output_text += "**Citations:**\n\n" + "\n".join(citations)

    return output_text

# -----------------------------------------------------------------------------
# USER INPUT AND RESPONSE HANDLING
# -----------------------------------------------------------------------------
# Get the user's legal query.
user_input = st.chat_input("Hello! How can I assist you today?:")

if user_input:
    # Append the user's message to the conversation history.
    st.session_state['conversation'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"**User:** {user_input}")

    # Retrieve and display the legal response.
    with st.chat_message("assistant"):
        response = get_legal_response(st.session_state['conversation'])
        st.markdown(f"**Assistant:** {response}", unsafe_allow_html=True)

    # Append the assistant's reply to the conversation history.
    st.session_state['conversation'].append({"role": "assistant", "content": response})

# -----------------------------------------------------------------------------
# DOWNLOAD OPTION: Allow users to download the conversation history
# -----------------------------------------------------------------------------
if st.session_state['conversation']:
    # Create a simple text transcript of the conversation.
    conversation_text = ""
    for msg in st.session_state['conversation']:
        conversation_text += f"{msg['role'].capitalize()}: {msg['content']}\n\n"

    # Create an in-memory binary buffer
    buffer = io.BytesIO()

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": markdown_to_csv_prompt},
            {
                "role": "user",
                "content": st.session_state['conversation'][-1]['content'],
            }
        ]
    )

    # Write the API response to the buffer as bytes
    # (Assuming completion.choices[0].message.content returns a string)
    buffer.write(completion.choices[0].message.content.encode("utf-8"))
    buffer.seek(0)  # Rewind the buffer so it can be read from the beginning

    st.download_button(
        label="Download Conversation",
        data=buffer,
        file_name="Output_Table.csv",  # Updated file extension to CSV
        mime="text/csv"  # Updated MIME type for CSV files
    )
