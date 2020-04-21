num = 2
num_p = 0

print("31 게임")
print("1~3 사이 숫자 하나 입력\n")
print("시작\n")

print("2")

while(True):
    num_p = int(input("숫자 입력: "))
    
    if num_p>3 or num_p<1:
        print("1~3 사이 숫자 입력")

    else:
        num += num_p
        print("당신 : "+str(num))

        num += 4-num_p
        print("컴퓨터 : "+str(num) + "\n")

        if num == 30:
            break

print("지셨습니다")
