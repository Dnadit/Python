#다음과 같은 게임 프로그램을 작성하라.
#플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 맞추면 $9을 따고 틀리면 $10을 잃는다.
#플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
#동전을 던져서 나오는 수는 다음 문장을 이용하라.
#from random import randint
#coin = randint(1,2) #1 또는 2를 임의로 발생
import random

money = 50

while True:
    coin = random.randint(1,2)
    guess = int(input("예상 앞면(1), 뒷면(2) : "))
    if guess == coin:
        money += 9
        print(f"맞췄습니다. 남은 돈 :{money}")
    else:
        money -= 10
        print(f"틀렸습니다. 남은 돈 :{money}")
    if money <= 0:
        print("돈을 다 잃었습니다.")
        break
    if money >= 100:
        print(f"돈이 $100가 넘었습니다. 남은 돈 :{money}")
        break
