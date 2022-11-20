emp_details = {"eden":["orisa LLC ",10],"nathan":["ins vodafone",15],"gloire":["spectrum",20],"mohit":["verizon",25]}

employee = input("enter name: ")

for names, details in emp_details.items():
    if employee in names:
        company = emp_details[0]
        leave = emp_details[1]
print("his name is {} , his company was {} and he left {} days ago".format())