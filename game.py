
print("도라에몽")
print("도라에몽이 길을가다가 퉁퉁이를 만났다.")
print("1.싸운다 2.도망간다")
number = input("숫자를 입력하세요 : ")
print("당신이 입력한 값은?", number)
# 만약에 1번이면
if number == "1":
    print("맞았다.")
# 만약에 2번이면
if number == "2":
    print("도망가다 잡혔다.")


# 밥 먹으러 간다.
print("오늘 점심은 어떤 메뉴를 먹을까?")
# 메뉴 1, 2, 3 아무거나 정해서
print("1.김치찌개 2.된장찌개 3.부대찌개")
# 먹는 메뉴를 선택해서 메뉴를 출력
menu = input("무엇을 먹겠습니까?")
if menu == "1":
    print("오늘 먹을 메뉴는 김치찌개")
if menu == "2":
    print("오늘 먹을 메뉴는 된장찌개")
if menu == "3":
    print("오늘 먹을 메뉴는 부대찌개")
else:
    print("먹지마")