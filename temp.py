import smtplib
import speech_recognition as sr
import pyttsx3 as tts
from email.message import EmailMessage

listener = sr.Recognizer()
engine = tts.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def speechtotext():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mukul.3381.dev@gmail.com','mukul@3382')
    email = EmailMessage()
    email['From'] = 'mukul.3381.dev@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {'m':'mukul.3381.dev@gmail.com','d':'dinesh55singhmalik@gmail.com','p':'pankajchaudhary992000@gmail.com','y':'yashjaiswal9050@gmail.com'}

def get_email_info():
    talk('Please give the email of the receiver:')
    name = speechtotext()
    receiver=email_list[name]
    print(receiver)
    talk('please tell the subject of your email:')
    subject = speechtotext()
    talk('please tell the body of the email:')
    message = speechtotext()
    send_email(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email?')
    choice = speechtotext()
    if 'yes' in choice:
        get_email_info()


get_email_info()