student_id = input().strip()
email = input().strip()
password = input().strip()
referral = input().strip()

id_ok = False
if len(student_id) == 7:
    if student_id[:3] == "CSE":
        if student_id[3] == "-":
            if student_id[4:7].isdigit() :
                id_ok = True

email_ok = False
if "@" in email and "." in email:
    if email[0] != "@" and email[-1] != "@":
        if email[-4:] == ".edu":
            email_ok = True

pass_ok = False
digit_found = ( "0" in password or "1" in password or "2" in password or
                "3" in password or "4" in password or "5" in password or
                "6" in password or "7" in password or "8" in password or "9" in password)

if len(password) >= 8:
    if password[0].isupper():
        if digit_found:
            pass_ok = True

ref_ok = False
if len(referral) == 6:
    if referral[:3] == "REF":
        if referral[3:5].isdigit() :
            if referral[5] == "@":
                ref_ok = True

if id_ok and email_ok and pass_ok and ref_ok:
    print("APPROVED")
else:
    print("REJECTED")