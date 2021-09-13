import PyPDF2
from PyPDF2 import PageRange
import re

f = open('cross.pdf', 'rb')

pdf = PyPDF2.PdfFileReader(f)

print(pdf.numPages)


#find the phone number
pattern = r'\d{5}'



#get all the text so that you know whats the pattern of the phone numbers
all_text = ''
for n in range(pdf.numPages):
  page = pdf.getPage(0)
  

  page_text = page.extractText()

  all_text = all_text + ' '+ page_text

#print(all_text)


#check the match
for match in re.finditer(pattern, all_text):
  print(match)


'''
for n in range(pdf.numPages):
  page = pdf.getPage(n)
  page_text = page.extractText()
  match = re.search(pattern, page_text)

  if match:
    print(match.group())
'''
