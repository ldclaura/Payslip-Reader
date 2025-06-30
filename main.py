from quickstart import main, get_attach, get_pdf, get_msg_id
from payslip_reader import Worker, grab_all_files, open_file
import pandas
import csv


if __name__ == "__main__":
  tokengen = main()
  tokengen
  print("1")
  print("1")
  print("1")
  print("1")
  print(f"MSGID {get_msg_id(tokengen)}")
  get_attach(tokengen)
  print(f"GETATTACH{get_attach(tokengen)}")
  payslips = grab_all_files("payslips")
  download_payslip = True
  for _ in payslips:
    print(_)
    if get_attach(tokengen)[1] == _:
       print("you already have this file")
       download_payslip = False
    else:
       pass
  if download_payslip == True:
    print("Getting PDF")
    get_pdf(get_attach(tokengen)[0], get_attach(tokengen)[1], get_attach(tokengen)[2], get_attach(tokengen)[3])




payslips = grab_all_files("payslips")
pays =  [open_file(f"payslips/{_}") for _ in payslips]

list_of_pays = []
list_of_period_ending = []

for _ in range(0, len(pays)):
    print(_)
    text = pays[_]
    me = Worker(firstname=Worker.name(text)[0], lastname=Worker.name(text)[1], abn=Worker.ABN(text), personnel=Worker.pers_num(text), position="Mail Officer")
    list_of_pays.append(Worker.net_pay(text)[0])
    print(Worker.net_pay(text)[0])
    list_of_period_ending.append(Worker.days_worked(text)[0]["SUN"])
    print(Worker.days_worked(text)[0]["SUN"])


data_dict = {
     "pay" : list_of_pays,
     "period ending": list_of_period_ending
}

students_data = pandas.DataFrame(data_dict)
students_data.to_csv("pay.csv")

pandas.read_csv("pay.csv")