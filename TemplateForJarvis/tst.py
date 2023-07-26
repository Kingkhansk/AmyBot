# # import pyttsx3

# # engine = pyttsx3.init(driverName='espeak')

# # text = "Hello, how are you?"
# # engine.say(text)
# # engine.runAndWait()

# # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# import openai

# # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
# API_KEY = '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'
# openai.api_key = API_KEY

# def generate_text(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",  # You can use other engines like "text-davinci-002" or "text-codex-002" based on your API plan
#         prompt=prompt,
#         temperature=0.7,  # Controls the randomness of the generated text. Higher values make it more random.
#         max_tokens=100,   # Controls the length of the generated text. Adjust this value as needed.
#         stop=None         # You can specify a stop sequence to stop the text generation at a specific point.
#     )
#     return response.choices[0].text.strip()

# if __name__ == "__main__":
#     prompt = "Once upon a time in a far-off land, there was a brave knight who"
#     generated_text = generate_text(prompt)
#     print(generated_text)

# import pyaudio
# p = pyaudio.PyAudio()
# for ii in range(p.get_device_count()):
#    print(p.get_device_info_by_index(ii).get('name'))

import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")

if __name__ == "__main__":
    test_microphone()
