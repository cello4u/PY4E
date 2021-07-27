#Q3. 학점 변환기
def grader(name,score):
        # 점수 int 변환
        try:
                int_score=int(score)
        except:
                print("점수는 숫자로만 입력해야 합니다. 프로그램을 종료합니다. 다시 실행해주세요.")
                quit()
        
        # 학점 변환
        if int_score >= 95 and int_score <= 100 :
                grade = "A+"
        elif int_score >= 90 and int_score <= 94 :
                grade = "A"
        elif int_score >= 85 and int_score <= 89 :
                grade = "B+"
        elif int_score >= 80 and int_score <= 84 :
                grade = "B"
        elif int_score >= 75 and int_score <= 79 :
                grade = "C+"
        elif int_score >= 70 and int_score <= 74 :
                grade = "C"
        elif int_score >= 65 and int_score <= 69 :
                grade = "D+"
        elif int_score >= 60 and int_score <= 64 :
                grade = "D"
        else:
                grade = "F"
        
        #결과 출력
        print("학생이름: ", name)
        print("점수: ",int_score,"점")
        print("학점: ", grade)

name=input("학생의 이름을 입력하세요: ")
score=input("학생의 점수를 입력하세요(숫자로만 입력합니다): ")
grader(name,score)
