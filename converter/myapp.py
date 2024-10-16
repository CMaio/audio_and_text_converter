"""This module is used to read out loud a PDF submited"""
import sys
import PyPDF2
import pyttsx3


engine = pyttsx3.init()

class Converter:
    """Class used to read the PDF"""
    def __init__(self):
        print("Which PDF do you want me to read? ")
        name = input()
        book_name = format_file(name)
        try:
            with open(book_name,'rb') as check_stream:
                check_stream.close()
        except FileNotFoundError:
            print("Sorry, that file was not found.")
            sys.exit()

        with open(book_name,'rb') as book:
            pdf_reader = PyPDF2.PdfReader(book)
            pages = pdf_reader.pages

        pages_contain_text = len(pages)

        print("Which starting page do you want me to read? Write 0 to start from the beginning ")
        start = int(input())
        while not check_validity_start_range_to_read(start,pages_contain_text):
            print("This number of pages doesn't exist. Please try again.")
            start = int(input())

        print("Until which page do you want me to read? Write END to read until the end")
        end = input()
        end_pages = format_number_end_pages(end,pages_contain_text)

        while not check_validity_range_to_read(start,end_pages,pages_contain_text):
            print("This number of pages doesn't exist. Please try again.")
            end = input()
            end_pages = format_number_end_pages(end,pages_contain_text)


        for i in range(start,end_pages):
            page = pdf_reader.pages[i]
            text = page.extract_text()
            engine.say(text)
            engine.runAndWait()

def format_file(title) -> str:
    """Format a PDF file."""
    location_assets = "Assets/"
    return location_assets + title + ".pdf" if ".pdf" not in title else location_assets + title

def format_number_end_pages(end_pages,pages_contain_text) -> int:
    """Format the end pages number to be a correct number."""
    return int(end_pages) if end_pages != "END" else pages_contain_text

def check_validity_start_range_to_read(page,pages_contain_text) -> bool:
    """Check of a correct starting page to read"""
    return 0 <= page < pages_contain_text


def check_validity_range_to_read(start_reading,page,pages_contain_text) -> bool:
    """Check of a correct range of pages to read"""
    return start_reading <= page <= pages_contain_text


def modify_voice() -> None:
    """Modify the voice of the text."""
    #RATE
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    #engine.setProperty('rate', 125)  # setting up new voice rate

    #VOLUME
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    #VOICE
    voices = engine.getProperty('voices')  # getting details of current voice

    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female

    engine.say("Hello World!")
    engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()



    #Saving Voice to a file
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    # engine.save_to_file('Hello World', 'test.mp3')
    # engine.runAndWait()


class PDFConverter:
    """Class of build"""
    def build(self):
        """Method of build"""
        return Converter()

if __name__ == "__main__":
    modify_voice()
    Converter()
