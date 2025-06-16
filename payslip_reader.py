# importing all the required modules
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
import pikepdf
import csv
import pandas
from datetime import datetime
import os
from os import listdir, getenv
from os.path import isfile, join

pay = "payslips/document.pdf"
pay2 = "payslips/document2.pdf"
pay3 = "payslips/document3.pdf"
#to csv
# data = reader.pages[0].extract_text()
# pandas.DataFrame(data).to_csv("data.csv")
#


#------------------------------------------------

#changed pay str in reader to variable
#redid venv because it stoped working for some reason?
#replaced pypdf with pdfminer.six

#-
def gmail_download():
    """ https://stackoverflow.com/questions/68466624/downloading-password-protected-pdfs-using-gmail-api-in-python 
    https://developers.google.com/workspace/gmail/api/guides/filtering
    """
    pass
def grab_all_files(folder):
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    return files

def open_file(payslip):
    try:
        with open(payslip,'rb') as f:
            text = extract_text(f)
            txt = text.split()
    except:
        files = [f for f in listdir('.') if isfile(f)]
        for f in files:
            print(f)
            if f.endswith(".pdf"):
                pdf = pikepdf.open(f,allow_overwriting_input=True, password=os.getenv('PDF_PASSWORD'))
                pdf.save(f)
                text = extract_text(f)
                txt = text.split()
    return txt

payslips = grab_all_files("payslips")
pays =  [open_file(f"payslips/{_}") for _ in payslips]
print(pays)
text = pays[0]

#--
class Worker():
    def __init__(self, firstname, lastname, abn, personnel, position):
        self.firstname = firstname
        self.lastname = lastname
        self.abn = abn
        self.personnel = personnel
        self.position = position
    def name(txt):
        # fullname = [txt[txt.index("Number:") + x] for x in range(1, 4, 2)]
        fullname = [txt[txt.index("Mail") - x] for x in range(1,4,2)]
        return fullname
    def payment_date(txt):
        date = [txt[txt.index(_) + 1] for _ in txt if _ == "Date:"]
        #returns twice?
        return date
    def fortnight(txt):
        fort = [txt[txt.index(_) + 2] for _ in txt if _ == "Ending"]
        #returns twice?
        return fort
    def ABN(txt):
        abn = [txt[txt.index(_) + 1] for _ in txt if _ == "ABN"]
        #ABN NUMBER (1 after ABN)
        return abn
    def pers_num(txt):
        num = [txt[txt.index(_) + 1] for _ in txt if _ == "2"]
        #returns 4 personnel numbers
        return num
    def from_date():
        pass
    def to_date():
        pass
    def description():
        pass
    def pay_scale():
        pass
    def hours_min():
        pass
    def hourly_rate():
        pass
    def amount(txt):
        num = [txt[txt.index(_) + 2] for _ in txt if _ == "Taxable"]
        return num
    def tax():
        pass
    def year_to_date():
        pass
    def period_ending():
        pass
    def net_pay(txt):
        #just amount - tax
        num = [txt[txt.index(_) + 1] for _ in txt if _ == "Services"]
        return num
    def days_worked(txt):
        #dates[0].strftime("%d-%b")
        dates = [datetime.strptime(txt[txt.index("ROSTERED") - x], "%d-%b") for x in range(1, 15)]
        wk1 = {"SUN":dates[0], "MON":dates[1], "TUE":dates[2], "WED":dates[3], "THU":dates[4], "FRI":dates[5], "SAT":dates[6]}
        wk2 = {"SUN":dates[7], "MON":dates[8], "TUE":dates[9], "WED":dates[10], "THU":dates[11], "FRI":dates[12], "SAT":dates[13]}
        return wk1, wk2
    def time_worked(txt):
        #NOTE NEED TO FIX
        #NOTE its in reverse
        end = len(txt) - txt.index("SUMMARY")
        times = [txt[len(txt) - x] for x in range(1, end)]
        times2 = [_.split(":") for _ in times]
        return times




me = Worker(firstname=Worker.name(text)[0], lastname=Worker.name(text)[1], abn=Worker.ABN(text), personnel=Worker.pers_num(text), position="Mail Officer")
print(me.position)

print(Worker.name(text))
print(Worker.amount(text))
print(Worker.net_pay(text))
print(Worker.days_worked(text))
print(Worker.time_worked(text))
print(Worker.days_worked(text)[0]["SUN"])
print(Worker.days_worked(text)[1]["SUN"])
one = Worker.days_worked(text)[0]["SUN"]
two = Worker.days_worked(text)[1]["SUN"]
if one > two:
    print(f"{one} is greater than {two}")
else:
    print(f"{two} is greater than {one}")
# print(text[len(text) - 1])
print(open_file(""))