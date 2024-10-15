import PyPDF2
import pyttsx3

print("Which PDF do you want me to read? ")
name = input()



try:
    checkStream = open(name,'rb')
    checkStream.close()
except FileNotFoundError:
    print("Sorry, that file was not found.")
    exit(1)

book = open(name,'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.pages
numPages = len(pages)


print("Which starting page do you want me to read? Write 0 to start from the beginning ")
start = int(input())
while start < 0 or start > numPages:
    print("This number of pages doesn't exist. Please try again.")
    start = int(input())

print("Until which page do you want me to read? Write END to read until the end")
end = int(input())
while end < 0 or end > numPages:
    print("This number of pages doesn't exist. Please try again.")
    end = int(input())

print(pages)
speaker = pyttsx3.init()
for i in range(start,end):
    page = pdfReader.pages[i]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()


def modify_voice():
    engine = pyttsx3.init()  # object creation

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 125)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    engine.say("Hello World!")
    engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
