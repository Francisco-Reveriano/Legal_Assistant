# Legal Response Chatbot

A Streamlit-based legal assistant chatbot that leverages OpenAI's API to provide legal responses and citations. This application uses conversation history stored in Streamlit's session state and integrates with OpenAI's beta threads to generate and format legal responses.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Interactive Chat Interface:** Uses Streamlit's chat components to display conversation history.
- **Legal Response Generation:** Integrates with OpenAI’s API to generate legal responses.
- **Citation Support:** Automatically inserts citation markers and lists corresponding legal document references.
- **Session State Management:** Remembers the conversation history across interactions.
- **Sidebar Controls:** Offers a "New Conversation" button to reset the chat.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [OpenAI Python Client](https://github.com/openai/openai-python)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/legal-response-chatbot.git
   cd legal-response-chatbot
