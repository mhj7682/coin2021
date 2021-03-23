#밥무러 간다
#메뉴 1,2,3, 아무꺼나 정해서 먹자
for i in range(1, 4):
    print("밥무러 가자")
    print("뭐물까")
    print("1.s 2.d 3.f")
    menu = input(str(i) + " .입력 : ")
    if menu == '1':
        print("1")
    if menu == '2':
        print("2")
    if menu == '3':
        print("3")
    