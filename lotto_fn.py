import random

def makeNums():
    balls = [ i for i in range(1,46)]
    random.shuffle(balls)
    return balls[0:6]

def input_display():
    money = int(input("금액을 입력하세요"))
    if money % 1000 != 0:
        print("1000원 단위로 다시")
        return input_display()
    else:
        return money / 1000

def main():
    print("hhhhhhhhhhhhhhhh")
    print("hhhhhhhhhhhhhhhh")
    print("hhhhhhhhhhhhhhhh")
    print("hhhhhhhhhhhhhhhh")

    count = input_display()
    for x in range(int(count)):
        nums = makeNums()
        print(sorted(nums))
    print("--------------------------------------")


if __name__ == "__main__":
    main()