# 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라. 
# 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(), '3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.

def sum(n, m):
    return n + m

def sub(n, m):
    return n - m

def mul(n, m):
    return n * m

def div(n, m):
    return n / m

table = {'1':sum, '2':sub, '3':mul, '4':div}

data = input("숫자 입력 : ")
func = table[data]
print(func(2,3))