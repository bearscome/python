cuss_list = []


def average():
    print(
        "",
        "---------------------",
        "0:종료",
        "1:학점 평균",
        "2:들어야 하는 과목들",
        "---------------------",
        "",
        sep="\n"
    )


while True:
    average()
    choice = input("실행하고자 하는 번호를 입력해주세요 >>")
    if choice == "0":
        print("프로그램을 종료합니다.")
        break
    if choice == "1":
        print("학점을 입력해 주세요",
              "A+, A, A-, B+, B, B-, ETC...",
              sep="\n")
        score = input("점수를 입력해 주세요")
        if score == "A+":
            print("4.5")
        elif score == "A":
            print("4.0")
        elif score == "B+":
            print("3.5")
        elif score == "B":
            print("3.0")
        elif score == "C+":
            print("2.5")
        elif score == "C":
            print("2.0")
        elif score == "D+":
            print("1.5")
        elif score == "D":
            print("1.0")
        elif score == "F":
            print("재수강...")
        break
