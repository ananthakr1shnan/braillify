import os
from groq import Groq
from dotenv import load_dotenv

conversation_history = []
load_dotenv()
api_key = os.getenv("api_key")


def generate_answer(text):
    # Define the user and system message format as dictionaries
    user_message = {"role": "user", "content": text}
    conversation_history.append(user_message)

    # Initialize the Groq client
    client = Groq(api_key=api_key)

    # Create chat completion using the client
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=conversation_history,
        temperature=0,  # Move temperature to the create method
    )

    # Extract the response content
    model_response = response.choices[0].message.content

    # Append the model's response to the conversation history
    system_message = {"role": "system", "content": model_response}
    conversation_history.append(system_message)

    return model_response
