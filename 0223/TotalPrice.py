# 사과의 개수와 가격 부가세율을 입력받아서 총 가격을 출력.
num = int(input("개수 입력 : "));
price = int(input("가격 입력 : "));
rate = float(input("부가세율 입력 : "));

rate1 = round(rate);

result1 = f'''
총 가격 : 개수{num} * 가격{price} + 부가세율{rate1}% = {num*price+num*price*rate1/100:.2f}
'''

result2 = f'''
총 가격 : 개수{num} * 가격{price} + 부가세율{rate:.0f}% = {int(num*price+num*price*rate/100)}
'''

print(result1);
print(result2);