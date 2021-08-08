import pyttsx3
import PyPDF2
# Variable containing the file name
book = open('py.pdf','rb')
# Variable so that the Variable containing the file name can read the file
pdfReader = PyPDF2.PdfFileReader(book)
# Variable to calculate the number of pages
pages = pdfReader.numPages
print(pages)

# To speak
speaker = pyttsx3.init()
# Variable so that a particular page is being read
page = pdfReader.getPage(1)
text = page.extractText()
# Add the text here
speaker.say(text)
speaker.runAndWait()