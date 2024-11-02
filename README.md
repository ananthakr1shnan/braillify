<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Braillify 🎯


## Basic Details
### Team Name: TechDAWGS


### Team Members
- Team Lead: Akshay KV - College of Engineering, Trivandrum
- Member 2: Ananthakrishnan K - College of Engineering, Trivandrum
- Member 3: Rishikesh - College of Engineering, Trivandrum

### Project Description
Our project, Braillify, is an AI-powered voice assistant that "helps" blind users get responses displayed in Braille—perfect for users who have zero vision but still want to enjoy some "top-quality" sarcasm in Braille!

### The Problem (that doesn't exist)
Blind users often rely on speech output or tactile solutions, yet visual Braille display offers an amusing alternative, presenting an unexpected challenge for accessibility tools.

### The Solution (that nobody asked for)
Our AI assistant allows users to ask any question and receive responses in Braille displayed on-screen. This innovative approach combines voice recognition and Braille, enhancing accessibility while providing an engaging user experience.

## Technical Details
### Technologies/Components Used
For Software:
Languages Used:
- Python

Frameworks Used:
- Streamlit

Libraries Used:
- `dotenv`: For loading environment variables.
- `logging`: For application logging.
- `speech_recognition`: For converting spoken input into text.
- `groq`: For interacting with the Groq API.
- `pySerial`: For Arduino communication.

Tools Used:
- Arduino: For hardware interaction.
- Code editor: VS Code

For Hardware:
Main Components:
- Arduino Board (Arduino Uno)
- Breadboard (for circuit assembly)
- Push button (for voice input activation)
- Wires (for connections)
- Led bulbs (To show button state)

Specifications:
- Arduino Board
- Connectivity: Serial communication via USB

Tools Required:
- Arduino IDE: For writing and uploading the Arduino code
- Breadboard and Wires: For circuit connections
- USB cable: For connecting Arduino to the computer

### Implementation
For Software:
####Installation
To get started with the project, follow these commands to install the necessary dependencies:
First clone this repository and move to project directory
Then install the required packages using command below
pip install streamlit python-dotenv pyserial SpeechRecognition groq

#### Run
streamlit run app.py

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Braille1](https://github.com/user-attachments/assets/8bdb9791-edff-422c-9a6c-e0f8f0750e4c)
This is the starting page

![Braille2](https://github.com/user-attachments/assets/cc025f05-57af-4090-bbb2-dc4c03de9363)
This shows the query and response in braille

![Braille3](https://github.com/user-attachments/assets/12fcfbd8-44d5-4e2f-adff-1aeb9d4f4cef)
We included orginal conversation in side bar, just to make sure that correct responses are recieved(Just for testing)

# Diagrams
![softwareworkflow](https://github.com/user-attachments/assets/4f1c84aa-d69f-4174-8f51-8b9245e3377e)

For Hardware:

# Schematic & Circuit
![circuit](https://github.com/user-attachments/assets/7544351c-b78e-4da5-b059-903a3865d022)
This circuit module generates a trigger based on the input switch and uses the red and green LEDs to display the button's state. The green LED likely indicates an "active" or "pressed" state, while the red LED might show an "inactive" or "not pressed" state. When the button is clicked, the LEDs provide a visual indication of the button's status, and Arduino provides the button state as input to the program.

# Build Photos
![hardware](https://github.com/user-attachments/assets/eaf7941c-eb92-4334-8da8-d3578d9c2219)
implementation


![componbraille](https://github.com/user-attachments/assets/0aded6ef-3dc1-40b4-997f-7b8fcbd663e8)
components

Button Detection:
The button is connected to pin D9 of the Arduino, which reads its state as HIGH (pressed) or LOW (not pressed).
This input serves as the trigger to control the LEDs and provide a digital signal based on the button's state.
LED State Indicators:

The red LED (D1) is connected to pin D8 with a 1k-ohm resistor and turns on when the button is not pressed, indicating an "inactive" state.
The green LED (D2) is connected to pin D7 with a 1k-ohm resistor and turns on when the button is pressed, showing an "active" state.
The Arduino program continuously checks the button’s state and switches the LEDs accordingly.
Trigger Generation:

When the button is pressed, the Arduino can use this as a trigger to perform specific actions, such as logging the event, activating another component, or sending a signal to an external system.
The LEDs provide an immediate visual confirmation of the button state, while the trigger can be used in the Arduino program for further functionality.

### Project Demo
# Video

https://github.com/user-attachments/assets/70d3794b-9edf-4426-87df-8feca6b91ff6


The demo video shows the working of the trigger and response generation in braille
When button is pressed, speech recognition input is activated.Led also changes from red to green indicating state change
After listening to the prompt, it recognizes and converts to text. The text input is given as prompt to llama 3.1 model and output is recieved.
Both the prompt and response are converted to braille and it is printed.

We have also implemented an additional function (given in sidebar) to show that correct responses are being generated for each prompt(Basically used for testing)

# Additional Demos


https://github.com/user-attachments/assets/34529900-b1f5-4fd3-8459-097fe1ea2c6e

A screen recording of interface.


## Team Contributions
- Akshay KV: Implemented various python functions for speech recognition, braille conversion, text generation
- Ananthakrishnan K: Implemented Streamlit interface, added function modules, connected Arduino with streamlit
- Rishikesh: Constructed the circuit, programmed the arduino 

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



