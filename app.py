import streamlit as st
import os
from dotenv import load_dotenv
import logging
from Speech import record_text
from groq_api import generate_answer
from braille import text_to_braille
import serial
import time

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s"
)


class VoiceSearchApp:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("api_key")

        # Initialize Arduino connection on COM7
        try:
            self.ser = serial.Serial("COM7", 9600, timeout=1)
        except serial.SerialException as e:
            st.error(f"Failed to connect to Arduino: {e}")
            self.ser = None

        # Initialize session state variables
        if "conversation" not in st.session_state:
            st.session_state.conversation = []
        if "original_conversation" not in st.session_state:
            st.session_state.original_conversation = []

    def check_arduino(self):
        """Check Arduino button state"""
        if self.ser and self.ser.is_open:
            data = self.ser.readline()
            if data:
                value = int(data[0]) - 48
                return value == 1
        return False

    def handle_voice_input(self):
        """Handle voice recording and processing"""
        try:
            with st.spinner("🎧 Listening... Please speak your question clearly"):
                user_text = record_text(device_index=2)

                if user_text and user_text != "Could not understand the audio.":
                    st.success(f"Recognized Text: {user_text}")

                    try:
                        with st.spinner("Generating response..."):
                            response = generate_answer(user_text)
                            braille_response = text_to_braille(response)
                            braille_question = text_to_braille(user_text)

                            # Store both braille and original text
                            st.session_state.conversation.append(
                                {
                                    "question": braille_question,
                                    "answer": braille_response,
                                }
                            )

                            # Store original text
                            st.session_state.original_conversation.append(
                                {"question": user_text, "answer": response}
                            )
                            return True

                    except Exception as api_error:
                        st.error(f"Error generating response: {api_error}")
                else:
                    st.warning("⚠️ Could not understand. Please try again.")

        except Exception as voice_error:
            st.error(f"Voice Recognition Error: {voice_error}")

        return False

    def run(self):
        st.set_page_config(page_title="Voice Search AI", page_icon="🎤", layout="wide")

        # Add sidebar for original conversations
        with st.sidebar:
            st.title("Original Conversations")
            if st.session_state.original_conversation:
                for item in st.session_state.original_conversation:
                    st.markdown("**User:**")
                    st.write(item["question"])
                    st.markdown("**Assistant:**")
                    st.write(item["answer"])
                    st.markdown("---")

        st.title("🎤 Braillify")

        # Custom CSS for styling
        st.markdown(
            """
            <style>
            .user-message {
                background-color: #7f7d80; /* Light green */
                border-radius: 10px;
                padding: 10px;
                margin: 10px 0;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                font-family: Arial, sans-serif;
                font-size: 16px;
            }
            .assistant-message {
                background-color: #7f7d80; /* Light red */
                border-radius: 10px;
                padding: 10px;
                margin: 10px 0;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                font-family: Arial, sans-serif;
                font-size: 16px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns([4, 1])
        with col2:
            if st.button("🗑️ Clear History", use_container_width=True):
                try:
                    if hasattr(self, "ser") and self.ser.is_open:
                        self.ser.close()
                except Exception as e:
                    st.error(f"Error closing port: {e}")

                # Clear both conversations
                st.session_state.conversation = []
                st.session_state.original_conversation = []

                time.sleep(0.5)
                st.rerun()

        # Display braille conversation history
        if st.session_state.conversation:
            for item in st.session_state.conversation:
                with st.container():
                    # User message
                    st.markdown(
                        f"""
                        <div class="user-message">
                            <strong>User:</strong> {item['question']}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    # Assistant message
                    st.markdown(
                        f"""
                        <div class="assistant-message">
                            <strong>Assistant:</strong> {item['answer']}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
        else:
            st.info("Press the Arduino button to start speaking!")

        # Wait for button press in a loop
        while not self.check_arduino():
            print("Waiting for button press...")
        if self.check_arduino():
            # Button is pressed, handle voice input
            success = self.handle_voice_input()
            if success:
                st.rerun()
        time.sleep(0.1)

    def __del__(self):
        if hasattr(self, "ser") and self.ser and self.ser.is_open:
            self.ser.close()


def main():
    app = VoiceSearchApp()
    app.run()


if __name__ == "__main__":
    main()
