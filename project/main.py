import sys

# 맨 처음 보이는 화면
def messege():
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

# 과목 수
def subJect_Nums():
    subJect_Nums = int(input("수강한 과목의 수를 입력해주세요: "))
    return subJect_Nums
 
# 과목 수 for함수
def Sum_Scores(Subject_Nums):
 
    Sum_Score = 0
    for i in range(Subject_Nums):
        message = str(i+1) + "번째 과목의 점수를 입력하세요: "
        score = int(input(message))
        Sum_Score = Sum_Score + score
    return Sum_Score
 
# 점수 학점 치환
def Exam_Score(Score):
    grade = 'F'
    if Score >=4.5:
        grade = 'A+'
    elif Score >= 4.0:
        grade = 'A'
    elif Score >= 3.5:
        grade = 'B+'
    elif Score >= 3.0:
        grade = 'B'
    elif Score >= 2.5:
        grade = 'C+'
    elif Score >= 2.0:
        grade = 'C'
    elif Score >= 1.5:
        grade = 'D+'
    elif Score >= 1.0:
        grade = 'D'
    else:
        grade ='F'
    print(grade)
 
# 전체 나누기 스코어
def get_average_score(Score, Subject_Nums):
    result = float(Score) / Subject_Nums 
    return result
 
 
# 메인함수
def main():
    messege()
    choice = input("실행하고자 하는 번호를 입력해주세요 >>")
    if choice == "0":
        print("프로그램을 종료합니다.")
    
    if choice == "1":
        number_of_subjects = subJect_Nums()
        total_score = Sum_Scores(number_of_subjects)
        average_score = get_average_score(total_score, number_of_subjects)
        Exam_Score(average_score)
    if choice == "2":
        subjects = ['프로그래밍','python','C','C++','C#']
        print(
            "",
            '----------------------',
            '1 : 수강 과목 입력',
            '2 : 수강 과목 삭제',
            '3 : 수강 중인 과목',
            '4 : 하나씩 과목 삭제',
            '----------------------',
            '',
            sep = '\n'
        )
        sub_choice = input('실행 할 번호를 입력해 주세요')
        if sub_choice == '1' :
            in_subject = input('리스트 안에 넣을 과목을 입력해주세요')
            subjects.append(in_subject)
        elif sub_choice == '2':
            del_subject = input('삭제할 과목을 입력해 주세요')
            subjects.remove(del_subject)
        elif sub_choice == '3':
            print(subjects)
        elif sub_choice == '4':
            print("들어야 하는 과목을 보여드립니다.", subjects,
              sep="\n")
            i = 0
            while i < len(subjects):
                fir_Subject = input("들었던 과목을 넣어주세요.")
                subjects.remove(fir_Subject)
                print(subjects)
                print(len(subjects))

                if i == len(subjects):
                    print("모든 과목을 수강하셨습니다.")
                    break

if __name__ == '__main__':
    main()