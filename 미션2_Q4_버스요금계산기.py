#Q4. 버스요금 계산기1
def bus_fare(age,method):
        # 입력값 int 변환
        try:
                int_age=int(age)
                int_method=int(method)
        except:
                print("숫자로만 입력해야 합니다. 프로그램을 종료합니다. 다시 실행해주세요.")
                quit()
        
        # 버스요금 계산
        if int_method == 0:
                str_method = "현금"
                if int_age < 8:
                        str_method = "무료"
                        fare = "무료"
                elif int_age >= 8 and int_age < 14:
                        fare = "450원"
                elif int_age >= 14 and int_age < 20:
                        fare = "1,000원"
                elif int_age >= 20 and int_age < 75:
                        fare = "1,300원"
                else :
                        str_method = "무료"
                        fare = "무료"
        elif int_method == 1:
                str_method = "카드"
                if int_age < 8:
                        str_method = "무료"
                        fare = "무료"
                elif int_age >= 8 and int_age < 14:
                        fare = "450원"
                elif int_age >= 14 and int_age < 20:
                        fare = "720원"
                elif int_age >= 20 and int_age < 75:
                        fare = "1,200원"
                else :
                        str_method = "무료"
                        fare = "무료"
        else:
                print("지불유형 입력이 잘못되었습니다. 프로그램을 종료합니다.")
                quit()
        
        #결과 출력
        print("요금 계산결과는 아래와 같습니다.")
        print("나이: ",int_age,"세")
        print("지불유형: ",str_method)
        print("버스요금: ",fare)

print("버스요금 계산기")
age=input("나이를 입력하세요(숫자로만 입력합니다): ")
method=input("지불 방법을 택하세요(현금=0, 카드=1): ")
bus_fare(age,method)
