## if문 연습.
d = int(input("cm단위의 길이 입력 : "))

if d < 0 :
    result = "잘못 입력하였습니다."
else :
    result = d /2.54
    
print(f"입력하신 {d}cm는 {round(result, 2)}인치 입니다.")

#
grade = int(input("학점 입력 : "))
if grade < 40 :
    result = "1학년 입니다."
elif grade < 80 :
    result = "2학년 입니다."
else :
    result = "졸업반입니다."
    
print(result)
#
time = int(input("시간 입력 : "))
dayN = int(input("am(-1) or pm(1)? : "))
timePass = int(input("How many hours ahead? "))
timePass %= 12
result = time + timePass

if result > 12:
               result -= 12
               dayN = -dayN
if dayN == 1 :
               dayNight = "pm"
else :
               dayNight = "am"
                   
print(f"New hour: {result}{dayNight}")
