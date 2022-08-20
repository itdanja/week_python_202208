
# rod1, rod2, rod3 : 각 위치에 있는 장대의 번호
def hanoi(n, rod1,  rod3 ,  rod2 ):
    ## base case
    # 원판이 하나일 떄는 그냥 rod1 -> rod3으로 옮기면 끝난다.
    if n == 1:
        print(rod1, rod3)

    ## recursion
    else:
        # 1. 원판 n-1개를 rod1에서 rod2로 옮긴다. (rod3를 보조 기둥으로)
        hanoi(n - 1, rod1, rod2, rod3)

        # 2. n번째 원반 = 제일 밑에 있는 원판을 목적지(rod3)로 이동
        print(rod1, rod3)

        # 3. rod2(가운데 장대)에 있는 원반 n-1개를 목적지(rod3)로 이동 (rod1를 보조 기둥으로)
        hanoi(n - 1, rod2, rod3, rod1)


# 테스트
hanoi(3, 1, 3, 2)