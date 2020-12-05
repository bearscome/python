import sys

# 맨 처음 보이는 화면
def messege():
    """
    처음 보여지는 설명 글
    """
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
def SubJect_Nums():
    SubJect_Nums = int(input("수강한 과목의 수를 입력해주세요: "))
    print('4.5점이 만점입니다.')
    return SubJect_Nums
 
# 과목 수 for함수
def Sum_Scores(Subject_Nums):
    Sum_Score = 0
    for i in range(Subject_Nums):
        message = str(i+1) + "번째 과목의 점수를 입력하세요: "
        score = float(input(message))
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
def Get_Average(Score, Subject_Nums):
    result = float(Score) / Subject_Nums 
    return result
 
 #과목 저장 수정 삭제
def Subject():
    Subjects = ['프로그래밍','python','C','C++','C#']
    print(
            "",
            '----------------------',
            '1 : 수강 과목 입력',
            '2 : 수강 과목 삭제',
            '3 : 수강 중인 과목',
            '----------------------',
            '',
            sep = '\n'
    )
    sub_choice = int(input('실행 할 번호를 입력해 주세요'))
    if sub_choice == 1 :
        file = open('subjects.txt','a',encoding='UTF8')
        in_subject = input('리스트 안에 넣을 과목을 입력해주세요')
        Subjects_txt = file.write('\n' + in_subject)
        file.close()
    elif sub_choice == 2:
        file = open('subjects.txt','r',encoding='UTF8')
        Subjects_txt = file.readlines()
        index = 0
        for lx in Subjects_txt:
            print("[{}]".format(index), lx, end="")
            index += 1

        del_subject = int(input('\n 삭제 할 과목의 인덱스 값을 입력해 주세요'))
        del Subjects_txt[del_subject]
        file = open('subjects.txt','w',encoding='UTF8')
        file.writelines(Subjects_txt) 
        file.close()

    elif sub_choice == 3:
        file = open('subjects.txt','r',encoding='UTF8')
        Subjects_txt = file.read()
        print(Subjects_txt)
        file.close()

 
# 메인함수
def main():
    while True:
        messege()
        choice = int(input("실행하고자 하는 번호를 입력해주세요 "))
        if choice == 0:
            print("프로그램을 종료합니다.")
            break
        if choice == 1:
            Get_Subjects = SubJect_Nums()
            Total_Score = Sum_Scores(Get_Subjects)
            Average_Score = Get_Average(Total_Score, Get_Subjects)
            Exam_Score(Average_Score)
        if choice == 2:
            Subject()
           
                   

#함수 실행
if __name__ == '__main__':
    main()