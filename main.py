import speech_recognition as sr
import webbrowser as wb

# Initialize recognizers
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

# Listen for the initial command
with sr.Microphone() as source:
    print('search youtube')
    print('speak now')
    audio = r3.listen(source)

try:
    command = r3.recognize_google(audio)
    if 'youtube' in command.lower():
        url = 'https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            print('search for a video')
            audio = r2.listen(source)
            try:
                query = r2.recognize_google(audio)
                print(f'Searching for: {query}')
                wb.open_new(url + query.replace(" ", "+"))
            except sr.UnknownValueError:
                print('Could not understand the audio')
            except sr.RequestError as e:
                print(f'Failed to request results; {e}')
except sr.UnknownValueError:
    print('Could not understand the audio command')
except sr.RequestError as e:
    print(f'Failed to request results; {e}')
