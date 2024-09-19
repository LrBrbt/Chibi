from vosk import Model, KaldiRecognizer
import speech_recognition
import pyttsx3
import wave
import json
import os 
import datetime
from sound import Sound

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
    



def execute_command_with_name(command_name: str):
    for key in commands.keys():
        if command_name in key:
            commands[key]()
        else:
            pass  # print("Command not found")    
def play_greetings():        
    VoiceAssistant.play_voice_assistant_speech("Привет" + User.name)

def make_system_volume_up():          
    VoiceAssistant.play_voice_assistant_speech("Хорошо! Громкость увеличена")
    Sound.volume_up()

def make_system_volume_down():       
    VoiceAssistant.play_voice_assistant_speech("Хорошо! Понижаю громкость")
    Sound.volume_down()

def call_the_assistent():            
    VoiceAssistant.play_voice_assistant_speech("Это я!")
    VoiceAssistant.play_voice_assistant_speech("Сегодня" + str(datetime.date.today))    

if __name__ == "__main__":


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


        commands = {
                        ("здравствуй","привет", "хай", "здарова", "ку"): play_greetings,
                        ("громче", "увеличь", "погромче"): make_system_volume_up,
                        ("тише", "понизь", "потише"): make_system_volume_down,
                        ("чиби"): call_the_assistent
        }        


        #command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        execute_command_with_name(command)

     