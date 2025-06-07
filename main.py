# importing all the required modules
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
import csv
import pandas

pay = "payslips/document.pdf"

#to csv
# data = reader.pages[0].extract_text()
# pandas.DataFrame(data).to_csv("data.csv")
#


#------------------------------------------------

#changed pay str in reader to variable
#redid venv because it stoped working for some reason?
#replaced pypdf with pdfminer.six

#-
with open(pay,'rb') as f:
    text = extract_text(f)

# print(text)


# print(text.replace('\n', ''))

# print(text.split())

#--
class Worker():
    def __init__(self):
        pass
    def payment_date():
        pass
    def fortnightly_period_ending():
        pass
    def ABN(txt):
        abn = [txt[txt.index(_) + 1] for _ in txt if _ == "ABN"]
        #ABN NUMBER (1 after ABN)
        return abn
    def personnel_number():
        pass
    def name():
        pass
    def pos():
        pass
    def num():
        pass


Worker.ABN(text.split())
print(Worker.ABN(text.split()))