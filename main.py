import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('someone@email.com', 'pwd')
    email = EmailMessage()
    email['From'] = 'someone@email.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

 email_list = {
     put some of your email contact here
 }

 def get_email_info():
    talk('to whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    talk('what is the subject for the email')
    subject = get_info()
    talk('tell me text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('your email is sent')
    talk('do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    
get_email_info()
