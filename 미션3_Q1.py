#Q1. 구구단 함수: 홀 수 번째만 출력, 값 50 이하인 것만 출력
def gugudan(number):
    print(number,'단')
    for i in range(1,10):
        if i%2 == 1:
            result = number * i
            if result <=50:
                print(number,'X',i,'=',result)
    print(number,'단 홀수번째 결과 50이하 값 출력 완료!')

while True:
    try:
        x=int(input('몇 단?:'))
    except:
        print("숫자만 입력가능합니다. 재입력하세요.")
        continue
    break
gugudan(x)
