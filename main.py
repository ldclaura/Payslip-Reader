# importing all the required modules
import pypdf
import csv
import pandas

# creating a pdf reader object
reader = pypdf.PdfReader('payslips/document.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())
print(reader.pages[1].extract_text())

#to csv
# data = reader.pages[0].extract_text()
# pandas.DataFrame(data).to_csv("data.csv")
#


#------------------------------------------------
