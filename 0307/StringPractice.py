data = input("문자 입력 : ")
print(len(data))
print(data * 10)
print(data[0])
print(data[:3])
print(data[-3:])
print(data[::-1])
if len(data) >= 7:
    print(data[6])
else:
    print("문자가 없습니다.")
print(data[1:-1])
print(data.upper())
print(data.lower())
print(data.replace("a","e"))