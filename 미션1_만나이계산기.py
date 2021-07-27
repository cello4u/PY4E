age=int(input('현재 한국 나이를 입력하세요: '))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))

if birth == 0:
        us_age=age-1
if birth == -1:
        us_age=age-2
print('당신의 미국 나이는',us_age,'세 입니다')
