# 사용자로부터 양의 정수 n을 입력받아, 1부터 n까지의 자연수 중에서 3의 배수와 5의 배수의 합을 구하고, 이를 출력하는 프로그램을 작성하세요.
# 사용자로부터 입력받는 정수 n은 1 이상의 양의 정수입니다.
# 자연수 1부터 n까지의 숫자 중에서 3의 배수 또는 5의 배수인 숫자들의 합을 구합니다.
# 결과값은 정수형으로 출력합니다.

n = int(input("양의 정수 입력 : "))
plus = 0
for i in range(1, n+1):
   
    if i%3 == 0 or i%5 == 0:
        plus += i
if n < 1:
    print("1 이상의 양의 정수를 입력해주세요.") 
else:
    print(plus)
    
#사용자로부터 5개의 정수형 숫자를 입력받아, 입력받은 숫자들 중에서 최댓값과 최솟값을 찾고, 이를 출력하는 프로그램을 작성하세요.
#입력받은 숫자는 1 이상 100 이하의 자연수입니다.
#입력받은 숫자 중 중복된 숫자가 있을 수 있습니다.
max = 0
min = 101
for i in range(5):    
    n = int(input("정수 입력 :"))
    if n < 1 or n > 100:
        print("1이상 100이하의 자연수를 입력해주세요.")
    if n > max:
        max = n
    if n < min:
        min = n    
print(max, min)
