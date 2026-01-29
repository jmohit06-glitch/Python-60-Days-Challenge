name =  input("Enter your Full Name: ")
email = input("Enter your Email Address: ")
num = input("Enter your Phone Number: ")
age = int(input("Enter your Age: "))
valid = True

if " " not in name or name[0] == " " or name[-1] == " ":
    valid = False
if "." not in email or "@" not in email or email[0] == "@":
    valid = False
if len(num) != 10 or not num.isdigit() or num[0] == "0":
    valid = False
if not(18 <= age <= 60):
    valid = False

if (valid):
    print("User profile is VALID")
else:
    print("User profile is INVALID")