from quickstart import main, get_attach, get_pdf, get_msg_id, get_file_and_attach
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
  print(len(get_msg_id(tokengen)))
  for _ in get_msg_id(tokengen):
    print("MSG ID IS")
    print(_)
    get_file_and_attach(tokengen, _)
    print("FILE AND ATTACH IS")
    print(get_file_and_attach(tokengen, _))


#get msg id
#get get attach id
#get filename
