#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

#Inicia o reconhecedor
r = sr.Recognizer()


with sr.Microphone() as source:
    print("Ajustando sensibilidade ao ruído ambiente...")
    r.adjust_for_ambient_noise(source)
    
    print("\nOuvindo...(Pressione Crtl + C para encerrar)")

    try:
        while True:            
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language = 'pt-Br')
                print(text)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Erro no serviço de reconhecimento:",str(e))

    except KeyboardInterrupt:
        print("\nEncerrando o progama!")