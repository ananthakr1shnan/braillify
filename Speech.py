import speech_recognition as sr

def record_text(device_index=2):  # Changed default to 2 since that worked for you
    """
    Record text with specified microphone
    """
    recognizer = sr.Recognizer()
    
    try:
        # Explicitly specify the microphone device
        microphone = sr.Microphone(device_index=device_index)
        
        with microphone as source:
            print(f"\nUsing microphone: {microphone.device_index}")
            
            # Lower threshold and adjust for noise
            recognizer.energy_threshold = 1000
            recognizer.dynamic_energy_threshold = True
            recognizer.pause_threshold = 1
            
            print("Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print(f"Energy threshold after adjustment: {recognizer.energy_threshold}")
            
            print("\nListening... (Speak now)")
            audio = recognizer.listen(source, timeout=10)
            
            print("Processing speech...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
            return text
            
    except sr.RequestError as e:
        print(f"RequestError: {str(e)}")
        return "Could not understand the audio."
    except sr.UnknownValueError as e:
        print(f"UnknownValueError: Speech was detected but couldn't be recognized")
        return "Could not understand the audio."
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error occurred: {str(e)}"

def test_specific_mic(device_index):
    print(f"\nTesting microphone at index {device_index}")
    result = record_text(device_index)
    print(f"Result: {result}")