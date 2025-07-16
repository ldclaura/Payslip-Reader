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

#to csv
# data = reader.pages[0].extract_text()
# pandas.DataFrame(data).to_csv("data.csv")
#


#------------------------------------------------

#changed pay str in reader to variable
#redid venv because it stoped working for some reason?
#replaced pypdf with pdfminer.six

class Payslip_Data:
    def __init__(self, txt, filename):
        self.txt = txt
        self.filename = filename
    def net_pay(self):
        """finds net pay
        saves as self.pay"""
        txt = self.txt
        #just amount - tax
        num = [txt[txt.index(_) + 1] for _ in txt if _ == "Services"]
        for _ in num:
            if _ == "TOTAL":
                num = [txt[txt.index(_) - 1] for _ in txt if _ == "Messages"]
        #if num greater than 4000
        #num = [txt[txt.index(_) - 2] for _ in txt if _ == "Messages"]
        num = float(num[0].replace(',', ''))
        if num > 4000:
            num = float([txt[txt.index(_) - 2] for _ in txt if _ == "Messages"][0].replace(',', ''))
        self.pay = num            
        return num
    def period_ending(self):
        """finds period ending of pdf from pdf name
        saves as self.period_end"""
        # files = "11161601_20230211_EMAIL.pdf"
        splitfilename = self.filename.split("_")#11161601_20230211_EMAIL.pdf
        # print(files2[1]) #20230211
        period_end = splitfilename[1]
        #-
        n = 2
        split_period_end = [period_end[i:i+n] for i in range(0, len(period_end), n)]
        yeardatemonth = split_period_end[0] + split_period_end[1] + "-" + split_period_end[2] + "-" + split_period_end[3]
        self.period_end = yeardatemonth
        return yeardatemonth

#----------------------------------------------------------------------------------
#unfinished do not use
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
    def days_worked(txt):
        year = [txt[txt.index(_) + 1] for _ in txt if _ == "Date:"][0][-4:]
        dates = [
            datetime.strptime(f"{txt[txt.index('ROSTERED') - x]}-{year}", "%d-%b-%Y")
            for x in range(1, 15)
        ] #assumes year is 2024, to include leap year.
        #changed it to 2025 but need to make it auto detect year
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



# me = Worker(firstname=Worker.name(text)[0], lastname=Worker.name(text)[1], abn=Worker.ABN(text), personnel=Worker.pers_num(text), position="Mail Officer")
# print(me.position)

# print("name:")
# print(Worker.name(text))
# print("amount:")
# print(Worker.amount(text))
# print("pay:")
# print(Worker.net_pay(text))
# print("time:")
# print(Worker.time_worked(text))
# print("days worked:")
# print([text[text.index("ROSTERED") - x] for x in range(1, 15)])
# print(Worker.days_worked(text))
# print(Worker.days_worked(text)[0]["SUN"])
# print(Worker.days_worked(text)[1]["SUN"])
# one = Worker.days_worked(text)[0]["SUN"]
# two = Worker.days_worked(text)[1]["SUN"]
# if one > two:
#     print(f"{one} is greater than {two}")
# else:
#     print(f"{two} is greater than {one}")
# # print(text[len(text) - 1])


# payslips = grab_all_files("payslips")
# # pays =  [open_file(f"payslips/{_}") for _ in payslips]
# pays = {_:open_file(f"payslips/{_}") for _ in payslips} #new_dict = {_:open_file(f"payslips/{_}") for _ in payslips}
# print(f"pays {pays}")
# list_of_pays = []
# list_of_period_ending = []
# for _ in range(0, len(pays)):
#     print(_)
#     text = list(pays.values())[_]
#     me = Worker(firstname=Worker.name(text)[0], lastname=Worker.name(text)[1], abn=Worker.ABN(text), personnel=Worker.pers_num(text), position="Mail Officer")
#     list_of_pays.append(Worker.net_pay(text))
#     # list_of_period_ending.append(Worker.days_worked(text)[0]["SUN"]) #!!!
#     list_of_period_ending.append(Worker.period_ending(list(pays.keys())[list(pays.values()).index(text)]))
# data_dict = {
#      "pay" : list_of_pays,
#      "period ending": list_of_period_ending
# }
# students_data = pandas.DataFrame(data_dict)
# print(students_data)
# students_data.to_csv("pay.csv")




# pays = open_file(f"payslips/11161601_20250628_EMAIL.pdf")
# print(f"pays {pays}")
# print(Worker.net_pay(pays))

#7/4/2025
#notes
#some net pays are too high, comes up with either total pay of year or before tax
#e.g. 20240615
#should change it so the fortnightly period ending is just taken from pdf name instead of reading the file
#because that'll be accurate 100 percent of the time