#두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성 예: 2, 4 => ****
#                                                                                           ****
list1 = []
list2 = []
def prob1(n, m):    
    for i in range(n):
        for j in range(m):
            print("*", end='')
        print()
prob1(2,4)
#하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성 예: 123 => 1+2+3 = 6
def prob2(n):
    result = 0
    for i in str(n):
        result += int(i)
    print(result)
prob2(123)
#두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
def prob3(str1, str2):
    if (str1 == str2):
        return -1
    for i in str(str1):
        for j in str(str2):
            if i != j:
                print(i, j)
                return
prob3("apple", "aoa")
#문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
str1 = input("문자열 : ")
str2 = input("하나의 문자 : ")
lst = []
def prob4(str1, str2):
    for i in str1:
        if i==str2:
            lst.append(i)
    return lst
prob4(str1, str2)
result = str1.find()
print(result)
#재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램


