# 두 주사위를 던졌을 때, 합이 7이 되면 이김, 그렇지 않으면 지는 주사위 게임.
import random

while True:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    if num1 + num2 == 7:
        print("이김")
        break
    else:
        print("짐")
        continue