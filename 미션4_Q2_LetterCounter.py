# 2021.08.10. Tuesday. 23:40.

# 시간관계상, 정답코드를 참고하였습니다만.. 머리가 굳어있는 제가 처음에 생각하기에는 어려운 논리네요 ㅠㅠ.
# 그래도 확실한건, 정답 예시 코드의 논리를 이해해두면, 도움은 될 것 같습니다!
# 제가, 만약 제대로 풀 시간이 있었다면,
# 저는, line.find해서, 문자열을 찾고, 해당 인덱스에서 길이 만큼까지의 문자열을 날리고,
# 같은 라인의 이후에서도, line.find의 결과로 -1 이 있는게 아닌지 하는 식으로 count를 단순 무식하게 했을 것 같은데요..
# 혹시 그렇게 풀면 이슈가 있을지, 생각나는게 있으면 말씀 부탁드립니다!


def count_word(text, word):
    # 문자열을 텍스트 파일로 저장
    text_save = open("text.txt", "w", encoding="UTF8")
    text_save.write(text)
    text_save.close()

    count = 0  # word를 세는 변수
    word_save = ""  # 문자의 길이만큼만 저장

    f_1 = open("text.txt")  # 텍스트 파일 읽어오기
    for line in f_1:  # 한 줄씩 불러오기
        if word in line:  # 우리가 찾는 문자가 현재 문장에 있다면
            for s in line:
                word_save = word_save + s  # 한 글자씩 word_save에 저장
                if word_save == word:  # word_save와 word를 비교해서 같으면
                    count += 1  # count +1
                if len(word_save) == len(word):  # 다음 문자 저장을 위해 1칸씩 앞으로 이동
                    word_save = word_save[1:]

    print("파일에 '" + word + "' 문자가 얼마나 있냐면은요!")
    print(str(count)+"개")  # word수 출력


if __name__ == '__main__':
    input_str = """
    울랄울랄라
    파이썬은, 신기하면서도, 이상한 언어 같아요아요.
    이번 학습을 통해,
    프로그래밍 입문자가, 파이썬으로 시작을 하는 이유에 대해서 충분히 납득이 되었고,
    프로그래밍 알고리즘 문제를 풀 때 확실히 유리한 문법들이 보이는 거 같네요.
    그렇지만, 아직도, 파이썬의 문법에서 배워야 할 게 많이 남아 있는 거 같아요.
    생각해보면, 자바는, 너무 코드가 주절주절 길어서, 가독성이 떨어진다 생각했었는데,
    파이썬은 오히려 너무 간결해서, 자바보다도 가독성이 더 떨어지는 거 같네요...
    아무튼, 새로운 언어를 배운다는 건 재밌는 것 같아요.
    열정있는 팀원분들과 함께해서 리프레쉬되고 자극도 많이 받네요!
    울랄울랄라울랄라
    """

    count_word(input_str, "울랄라")