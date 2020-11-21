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
        grade = []
        print("학점을 입력해 주세요",
              "A+, A, B+, B, C+ C, D+, D, F",
              "4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, Fail      ETC...",
              sep="\n")

      
        score_Aplus = input("점수를 입력해 주세요")
        print(score_Aplus)
        score_A = input("점수를 입력해 주세요")
        print(score_A)
        score_Bplus = input("점수를 입력해 주세요")
        print(score_Bplus)
        score_B = input("점수를 입력해 주세요")
        print(score_B)
        score_Cplus = input("점수를 입력해 주세요")
        print(score_Cplus)
        score_Dplus = input("점수를 입력해 주세요")
        print(score_Dplus)
        score_D = input("점수를 입력해 주세요")
        print(score_D)
        score_F = input("점수를 입력해 주세요")
        print(score_F)
        grade.push(score)
        print(score)

        if score_Aplus == "A+":
            score = 4.5
            print(score_Aplus)
        elif score_A == "A":
            score = 4
            print(score_A)
        elif score_Bplus == "B+":
            score = 3.5
            print(score_Bplus)
        elif score_B == "B":
            score = 3
            print(score_B)
        elif score_Cplus == "C+":
            score = 2.5
            print(score_Cplus)
        elif score_C == "C":
            score = 2
            print(score_C)
        elif score_F == "F":
            score = 'Fail'
            print(score_F)

        break

    if choice == "2":
        subjects = ['프로그래밍','python','C','C++','C#']
        print("들어야 하는 과목을 보여드립니다.", subjects,
              sep="\n")

        i = 0
        while i < 5:
            i = i + 1
            fir_Subject = input("들었던 과목을 넣어주세요.종료는 0번 입니다.")
            subjects.remove(fir_Subject)
            print(subjects)

            if i == 5:
                print("모든 과목을 수강하셨습니다.")
                break


