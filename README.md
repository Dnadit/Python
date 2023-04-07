# Python
- 파이썬 수업내용 중 필기

## Python의 기본
- Primitive Type이 존재하지 않음. 모두 다 Object Type.

## list
- list와 str의 차이 (mutable, immutable)
- list는 모든 타입이 다 들어갈 수 있다.
- 튜플과 str은 immutable하다.
- mutable 한 것은 조심스럽게 써야함.
- .split() 함수의 return값은 list임.

## 튜플
- immutable.
- 배열에서 쓰는 함수 모두 사용 가능.

## Sequence
```shell
for s in [sequence]:
    pass

print('a' in 'abc') # True

s = 'abc'
print(list(s))  # [a, b, c]
t = (a, b, c)
print(list(t))  # [a, b, c]

# 출력이 되지 않는 Sequence를 출력하는 방법
print(tuple(range(3)))  # (0, 1, 2)
```
