# importing all the required modules
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
import csv
import pandas
from datetime import datetime

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
with open(pay2,'rb') as f:
    text = extract_text(f)

print(text.split())


# print(text.replace('\n', ''))

# print(text.split())

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
        dates = [txt[txt.index("ROSTERED") - x] for x in range(1, 15)]
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




me = Worker(firstname=Worker.name(text.split())[0], lastname=Worker.name(text.split())[1], abn=Worker.ABN(text.split()), personnel=Worker.pers_num(text.split()), position="Mail Officer")
print(me.position)

print(Worker.name(text.split()))
print(Worker.amount(text.split()))
print(Worker.net_pay(text.split()))
print(Worker.days_worked(text.split()))
print(Worker.time_worked(text.split()))
# print(text.split()[len(text.split()) - 1])