from quickstart import main, get_attach, get_pdf, get_msg_id
from payslip_reader import Worker, grab_all_files, open_file
import pandas
import csv
from quickstart2 import Payslips
from payslip_reader2 import Payslip_Data


if __name__ == "__main__":
  p = Payslips()       # Create an instance
  p.gen_server()
  
  p.get_msg_id()  # Call the method on the instance
  p.get_all_payslips_data()

  files = p.check_folder()

  for filename in p.check_downloadable_files(files):
      filename_dict = p.all_payslips_data[filename]
      for msg_id, att_id in filename_dict.items():
          p.get_pdf(filename, msg_id, att_id)

  payslips = p.grab_all_files("payslips")
  pays = {_:p.open_file(f"payslips/{_}") for _ in payslips}
  print(f"pays {pays}")


    # payslips = grab_all_files("payslips")
    # pays = {_:open_file(f"payslips/{_}") for _ in payslips} #new_dict = {_:open_file(f"payslips/{_}") for _ in payslips}
#--------------------------------------------------------------------------------
print(p.service) # Access the msg_id attribute of that instance
print("all payslips data filename:msg_id:attachment_id")
print(p.all_payslips_data) #filenames

print("dicks2")
for _  in p.all_payslips_data["11161601_20230128_EMAIL.pdf"]: #msg_id
    print(_) #msg_id
    print(p.all_payslips_data["11161601_20230128_EMAIL.pdf"][_]) #attachment_id

# for key, value in p.all_payslips_data.items():
#   print(key)
print("dicks3")
print(p.all_payslips_data)

objs = [Payslip_Data(open_file(f"payslips/{payslips[i]}")) for i in range(len(p.all_payslips_data))]
for obj in objs:
  data_dict = {
      "pay" : obj.net_pay(),
      "period ending": obj.period_ending("11161601_20230128_EMAIL.pdf") #maybe put filename in obj self.
  }


  print(data_dict)
# print("new_dict = {new_key:new_value for item in list}")
# #CONDITIONAL DICTIONARY COMPREHENSION
# print("new_dict = {new_key:new_value for (key, value) in dict.items() if test}")
#-------------------------------------------------------------------------------------

# data_dict = {
#      "pay" : list_of_pays,
#      "period ending": list_of_period_ending
# }

# pays_data = pandas.DataFrame(data_dict)
# pays_data.to_csv("pay.csv")

# pandas.read_csv("pay.csv")


# objs = [MyClass() for i in range(10)]
# for obj in objs:
#     other_object.add(obj)

# objs[0].do_sth()

#grab data



# payslips = grab_all_files("payslips")
# pays =  [open_file(f"payslips/{_}") for _ in payslips]

# list_of_pays = []
# list_of_period_ending = []

# for _ in range(0, len(pays)):
#     text = pays[_]
#     me = Worker(firstname=Worker.name(text)[0], lastname=Worker.name(text)[1], abn=Worker.ABN(text), personnel=Worker.pers_num(text), position="Mail Officer")
#     list_of_pays.append(Worker.net_pay(text))
#     list_of_period_ending.append(Worker.days_worked(text)[0]["SUN"])




# print("BAD")
# print(open_file("payslips/11161601_20240127_EMAIL.pdf"))
# print(open_file("payslips/11161601_20230923_EMAIL.pdf"))
# print("GOOD")
# print(open_file("payslips/11161601_20240224_EMAIL.pdf"))
# print(open_file("payslips/11161601_20230729_EMAIL.pdf"))

