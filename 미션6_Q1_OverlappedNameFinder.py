# Define function1
def Inputchecker(names):
    names = names.strip()
    # Check whether number of king's names is too small
    if len(names.split(",")) <= 3:
        print("Input error! Enter at least three kings name!")
        re = input("Enter king's names again(divide names by ','): ")
        Inputchecker(re)
    # Check whether names are divided by ","
    if "," not in names:
        print("Input error! Divide names with ','")
        re = input("Enter king's names again(divide names by ','): ")
        Inputchecker(re)
    return names

# Define function2
def OverlappedKingFinder(korea,chosun):
    # make king name list of korea and chosun each.
    ko_kings_lst = korea.split(",")
    cho_kings_lst = chosun.split(",")
    kings_dic = dict()
    # First, make dictionary of korea kings.
    for ko_king in ko_kings_lst:
        kings_dic[ko_king] = kings_dic.get(ko_king,0) + 1
    # Combine Chosun kings with Korea kings
    for cho_king in cho_kings_lst:
        kings_dic[cho_king] = kings_dic.get(cho_king,0) + 1

    # Check and print out the overlapped names
    count = 0
    for k , v in kings_dic.items():
        if v >= 2:
            print(f"King's name Belong to both Korea and Chosun:{k}")
            count = count + 1
    print(f"Number of King's names Belong to both Korea and Chosun:{count}")

#-----------------Main-----------------
print("--------------- Overlapped King's name Finder ---------------")
# Korea kings: 태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕
Korea_kings = Inputchecker(input("Enter all the king's name of Korea Dynasty(divide names by ','): "))
# Chosun kings: 태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종
Chosun_kings = Inputchecker(input("Enter all the king's name of Chosun Dynasty(divide names by ','): "))
print("----------------- The result of calcaulation ----------------")
OverlappedKingFinder(Korea_kings,Chosun_kings)
