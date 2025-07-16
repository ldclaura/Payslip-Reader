
import pandas

from quickstart2 import Payslips
from payslip_reader2 import Payslip_Data


if __name__ == "__main__":
  p = Payslips()       # Create an instance
  p.gen_server()
  
  p.get_msg_id()  # Call the method on the instance
  p.get_all_payslips_data()

  payslips = p.check_folder()

  for filename in p.check_downloadable_files(payslips):
      filename_dict = p.all_payslips_data[filename]
      for msg_id, att_id in filename_dict.items():
          p.get_pdf(filename, msg_id, att_id)



 
#--------------------------------------------------------------------------------
# print(p.service) # Access the msg_id attribute of that instance
# print("all payslips data filename:msg_id:attachment_id")



objs = [Payslip_Data(p.open_file(f"payslips/{payslips[i]}"), payslips[i]) for i in range(len(p.all_payslips_data) + 1)]
pay = []
period_ending = []
for obj in objs:
  pay.append(obj.net_pay())
  period_ending.append(obj.period_ending())
data_dict = {
    "pay" : pay,
    "period ending": period_ending
}

print(data_dict)
pays_data = pandas.DataFrame(data_dict)
pays_data.to_csv("pay.csv")

#note
#create code that creates .env file? asking user what the pdf password is beforehand and adding to env?
