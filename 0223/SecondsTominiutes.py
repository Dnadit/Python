# 초를 입력하면 분과 초로 표시하는 프로그램. 예를 들어, 200초를 입력하면 3분 20초로 표현하라.

seconds = int(input("초 입력 : "));

print(f"""
입력받은 초 : {seconds}
분 초 : {seconds//60}분 {seconds%60}초
""");