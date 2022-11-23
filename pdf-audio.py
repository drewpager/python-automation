import pyttsx3,PyPDF2

#Replace 'contract.pdf' with path to your PDF file (i.e. /Desktop/Contracts/contract.pdf)
pdfreader = PyPDF2.PdfFileReader(open('contract.pdf','rb'))
reader = pyttsx3.init()
for page in range(pdfreader.numPages):   
    copy = pdfreader.getPage(page).extractText()
    legible_copy = copy.strip().replace('\n',' ')
    print(legible_copy)
    reader.say(legible_copy)
    reader.save_to_file(legible_copy,'contract.mp3')
    reader.runAndWait()
reader.stop()
