#Q1. 가위바위보 수행함수
def rsp(my):
        #내가 선택한 것 변환
        if my == "0" or my == "가위":
                my = "가위"
        elif my == "1" or my == "바위":
                my = "바위"
        elif my == "2" or my == "보":
                my = "보"
        
        #컴퓨터가 낼 것 선정.
        import random
        com=random.randint(0,2)

        #가위바위보 결과
        if my == "가위":
                print("나: ",my)
                if com == 0:
                        print("컴퓨터: 가위")
                        print("비겼습니다!")
                elif com == 1:
                        print("컴퓨터: 바위")
                        print("컴퓨터 승리!")
                else: 
                        print("컴퓨터: 보")
                        print("당신 승리!") 
        if my == "바위":
                print("나: ",my)
                if com == 0:
                        print("컴퓨터: 가위")
                        print("당신 승리!")
                elif com == 1:
                        print("컴퓨터: 바위")
                        print("비겼습니다!")
                else: 
                        print("컴퓨터: 보")
                        print("컴퓨터 승리!") 
        if my == "보":
                print("나: ",my)
                if com == 0:
                        print("컴퓨터: 가위")
                        print("컴퓨터 승리!")
                elif com == 1:
                        print("컴퓨터: 바위")
                        print("당신 승리!")
                else: 
                        print("컴퓨터: 보")
                        print("비겼습니다!") 

x=input("내가 낼 것은(0~2 또는 가위,바위,보 중 선택)?: ")
rsp(x)
