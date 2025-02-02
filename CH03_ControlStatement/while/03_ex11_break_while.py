# while문 탈출
# while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다.
# 따라서 강제로 while문을 탈출하기 위해 break문을 사용한다.

coffee = 10
money = 300
while money:
    print("커피를 내립니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d 개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
# money가 300으로 고정되어 있으므로 while money:에서 money는 0이 아니므로 항상 참
# 따라서 무한 루프를 수행하게됨
# 하지만 루프를 수행 중 커피가 계속 1씩 줄어 0이 되면 break문이 호출되어 while문을 탈출한다.


coffee = 15
while True:
    money = int(input("돈을 넣어 주세요. : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
# 콘솔에서 money를 입력받아 coffee를 판매하는 예제