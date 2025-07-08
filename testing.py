# from quickstart import main, get_attach, get_pdf, get_msg_id, get_file_and_attach
# from payslip_reader import Worker, grab_all_files, open_file
# import pandas
# import csv


# if __name__ == "__main__":
#   tokengen = main()
#   tokengen
#   print("1")
#   print("1")
#   print("1")
#   print("1")
#   print(f"MSGID {get_msg_id(tokengen)}")
#   print(len(get_msg_id(tokengen)))
#   for _ in get_msg_id(tokengen):
#     print("MSG ID IS")
#     print(_)
#     get_file_and_attach(tokengen, _)
#     print("FILE AND ATTACH IS")
#     print(get_file_and_attach(tokengen, _))


#get msg id
#get get attach id
#get filename
# files = grab_all_files("payslips")
# print(files)
files = "11161601_20230211_EMAIL.pdf"
files2 = files.split("_")#11161601_20230211_EMAIL.pdf
print(files2[1]) #20230211
thing = files2[1]


n = 2
splitthing = [thing[i:i+n] for i in range(0, len(thing), n)]
yeardatemonth = splitthing[0] + splitthing[1] + "-" + splitthing[2] + "-" + splitthing[3]