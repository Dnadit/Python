#다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
# 예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가 '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환.
# Hint: dict([['a','b'], ['c', 'd']])  {'a': 'b', 'c': 'd'}

str = 'led=on&motor=off&switch=off'
def StrToDict(str):
    lst = str.split('&')
    lst1 = []
    for i in lst:
        lst1.append(i.split('='))
    return dict(lst1)

print(StrToDict(str))