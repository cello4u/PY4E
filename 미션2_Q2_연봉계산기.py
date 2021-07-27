#Q2. 연봉계산기
def y_pay(m_pay):
        # 월급 int 변환
        try:
                int_mpay=int(m_pay)
        except:
                print("만원단위의 숫자로만 입력해야 합니다. 프로그램을 종료합니다")
                quit()
        # 세전연봉 구하기
        pt_ypay = int_mpay * 12
        # 세후 연봉 구하기
        if pt_ypay <= 1200:
                at_ypay = pt_ypay * (1-0.06)
        elif pt_ypay <= 4600:
                at_ypay = pt_ypay * (1-0.15)
        elif pt_ypay <= 8800:
                at_ypay = pt_ypay * (1-0.24)
        elif pt_ypay <= 15000:
                at_ypay = pt_ypay * (1-0.35)         
        elif pt_ypay <= 30000:
                at_ypay = pt_ypay * (1-0.38)
        elif pt_ypay <= 50000:
                at_ypay = pt_ypay * (1-0.40)
        elif pt_ypay > 50000:
                at_ypay = pt_ypay * (1-0.42)

        #결과 출력
        print("세전 연봉: ", pt_ypay,"만원")
        print("세후 연봉: ",at_ypay,"만원")

x=input("당신의 월급은?(만원 단위로 입력하세요): ")
y_pay(x)
