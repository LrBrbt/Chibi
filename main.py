from vosk import Model, KaldiRecognizer
import speech_recognition
import pyttsx3
import wave
import json
import os 
import datetime

class User:
    name = "Валерия"
    surname = "Погодина"
    age = 19
    date_birth = "13.01.2005"

class VoiceAssistant:
    name = "Чиби"
    sex = "male"
    speech_language = "ru"
    recognition_language = "ru"

    def setup_assistant_voice():
        voices = ttsEngine.getProperty("voices")
        ttsEngine.setProperty("voice", voices[0].id)
    def play_voice_assistant_speech(text_to_speech):
        ttsEngine.say(str(text_to_speech))
        ttsEngine.runAndWait()
    def record_and_recognize_audio(*args: tuple):
        with microphone:
            reconized_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)
            try:
                print("Я слушаю...")
                audio = recognizer.listen(microphone,5,5)

                with open("microphone-results.wav", "wb") as file:
                    file.write(audio.get_wav_data())
            except speech_recognition.WaitTimeoutError:
                print("Проверьте, пожалуйста, микрофон")
                return
            
            try:
                print("...")
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            except speech_recognition.UnknownValueError:
                pass
        return recognized_data

if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Чиби"
    assistant.sex = "male"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию
    VoiceAssistant.setup_assistant_voice()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = VoiceAssistant.record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]

        if command == "дата":            
            VoiceAssistant.play_voice_assistant_speech("Сегодня" + str(datetime.date.today))
        if command == "привет":            
            VoiceAssistant.play_voice_assistant_speech("Привет" + User.name)