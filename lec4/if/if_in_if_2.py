'''
파일명 : if_in_if_2.py
'''

score = 83
if score >= 90:
    if score >= 95:
        print("A+")
    else:
        print("A0")
elif score >= 80:
    if score >= 85:
        print("B+")
    else:
        print("B0")
elif score >= 70:
    if score >= 75:
        print("C+")
    else:
        print("C0")
else:
    print("F")