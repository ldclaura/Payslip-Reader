# importing all the required modules
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
import csv
import pandas

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
with open(pay,'rb') as f:
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
        lastname = [txt[txt.index(_) + 1] for _ in txt if _ == "Number:"]
        firstname = [txt[txt.index(_) + 3] for _ in txt if _ == "Number:"]

        return firstname, lastname
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
    def amount():
        pass
    def tax():
        pass
    def year_to_date():
        pass
    def period_ending():
        pass
    def net_pay():
        #just amount - tax
        pass
    def days_worked(txt):
        dates = []
        for x in range(-14, 0):
            worked = [txt[txt.index(_) + x] for _ in txt if _ == "ROSTERED"]
            dates.append(worked)
        wk1 = {"SUN":dates[0], "MON":dates[1], "TUE":dates[2], "WED":dates[3], "THU":dates[4], "FRI":dates[5], "SAT":dates[6]}
        wk2 = {"SUN":dates[7], "MON":dates[8], "TUE":dates[9], "WED":dates[10], "THU":dates[11], "FRI":dates[12], "SAT":dates[13]}
        return wk1, wk2



Worker.ABN(text.split())
print(f"ABN: {Worker.ABN(text.split())}")
print(f"Name: {Worker.name(text.split())}")
print(f"Payment Date: {Worker.payment_date(text.split())}")
print(f"Fortnightly Period Ending: {Worker.fortnight(text.split())}")
print(f"Personnnel Number: {Worker.pers_num(text.split())}")
print(type(Worker.ABN(text.split())))
print(type(Worker.name(text.split())))

#to string
# myabn = str(Worker.ABN(text.split())).strip('[]')
# print(myabn)
# print(type(myabn))

#str join
# myname = " ".join(Worker.name(text.split()))
# print(myname)

# firstname, lastname, abn, personnel, position
me = Worker(firstname=Worker.name(text.split())[0], lastname=Worker.name(text.split())[1], abn=Worker.ABN(text.split()), personnel=Worker.pers_num(text.split()), position="Mail Officer")
print(me.position)
print(me.firstname)
print(me.lastname)

print(f"days worked: {Worker.days_worked(text.split())}")
