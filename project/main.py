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
              "4.5, 4, 3.5, 3, 2.5, 2      ETC...",
              sep="\n")
        score = input("점수를 입력해 주세요")
        grade.push(score)
        print(score)
        break

    if choice == "2":
        subjects = ['프로그래밍','python','C','C++','C#']
        print("들어야 하는 과목을 보여드립니다.", subjects,
              sep="\n")
        subject = input("들었던 과목을 넣어주세요.종료는 0번 입니다.")

        while True:
            subjects.remove(subject)
            print(subjects)
            break
           

            # for subject in subjects:
            # while True:
            # if subject =="프로그래밍":
            #     subjects.remove('프로그래밍')
            #     print(subjects)
            #     break