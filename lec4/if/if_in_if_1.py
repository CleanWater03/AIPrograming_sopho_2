'''
파일명 : if_in_if_1.py
'''

score = 97
if score >= 90:
    if score >= 95:
        print('성적이 "A"이면서 전액장학금 대상자입니다.')
    else:
        print('성적이 "A"이면서 반액장학금 대상자입니다.')
elif score >= 80 & score <90:
    print("B")
elif score >= 70 & score <80:
    print("C")
else:
    print("F")