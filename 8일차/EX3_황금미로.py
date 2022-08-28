"""
    황금 미로 문제
        [조건]
            1. 왼쪽 상단[시작 행/열 ] 출발해서 오른쪽 하단[마지막행,마지막열]
            2. 시작부터 출구까지 지나가면서 최대 얻을수 있는 황금 개수 세기
            3. 대각선 이동불가
        [미로]

            --->  입구      1개    4개   4개   2개   2개
                                  1개    3개   3개   0개   5개
                                  1개    2개   4개   3개   0개
                                  3개    3개   0개   4개   2개
                                  1개    3개   4개   5개   3개  ----> 출구
"""

def printMaze( arr ) : # # 2차원의 메모이제이션 출력 함수
        for row in range( ROW ) :
                for col in range( COL ) :
                       print( "%3s"  % arr[row][col] ,  end = ' ' )
                print()
        print()

def solution() :
        # 2차원의 메모이제이션
        memo = [ [ 0 for _ in range( COL ) ]  for _ in range(ROW) ]

        ###################
        # 가로의 누적합계
        rowsum = memo[0][0]                             # 1. 첫번째 값을 누적변수에 넣는다.
        for i in range( 1 , ROW ) :                            # 2. 두번째 행부터 마지막 행까지 반복
                rowsum += goldMaze[0][i]                       # 3. 미로에 있는 [0][i]번째 골드 누적 더하기
                memo[0][i] = rowsum                                     # 4. 메모에 누적 골드 대입

        # 세로의 누적합계
        colsum = memo[0][0]
        for i in range( 1 , COL ):
                colsum += goldMaze[i][0]
                memo[i][0] = colsum

        # * 행/열 비교[ 현재위치에서 아래 값과 오른쪽 값 비교 하기 ]

        count = 0 # 이동횟수

        for row in range( 1 , ROW ) :           #  행 : 1부터 4까지 반복
                for col in range( 1 , COL ):            # 열 : 1부터 4까지 반복

                        if memo[row][col-1] > memo[row-1][col] :  # 아래 방향이 더 크면
                                memo[row][col] = memo[row][col-1] + goldMaze[row][col]  # 아래방향 골드 + 기존 골드
                        else :     # 오른쪽이 더 크면
                                memo[row][col] = memo[row-1][col] + goldMaze[row][col]  # 오른쪽방향 골드 + 기존 골드

                        count += 1  # 이동횟수 증가

        # 2차원의 메모이제이션 출력
        print("------------ 메모이제이션 출력 ------------")
        printMaze( memo )

        print('------------ 지나온 경로 출력 ---------------')
        row = ROW-1             # 마지막 행 인덱스
        col = COL-1                     # 마지막 열 인덱스
        memo[row][col] = '*'    # 마지막 칸에 * 출력

        while row !=0 or col != 0 :          # 행이 0이 아니 거나 열이 0이 아닐때 반복 [ row 와 col 0 이 종료 ]
                if row -1 >= 0 and col-1>= 0 :
                        if memo[row-1][col] > memo[row][col-1] :
                                # 위쪽 방향이 더 크면  -> 오른쪽 경로
                                row -= 1
                        else:
                                # 왼쪽  방향이 더 크면  -> 아래쪽 경로
                                col -= 1
                elif row-1 < 0 and col-1 >= 0 : # 만약에 위쪽 방향에 인덱스가 0보다 작으면
                        col -= 1        # 왼쪽 방향
                else: # 만약에 왼쪽 방향에 인덱스가 0보다 작으면
                        row -= 1
                memo[row][col] = '*'
        print("------------ 메모이제이션 출력 ------------")
        printMaze(memo)


ROW , COL = 5 , 5 # 미로 칸수
goldMaze = [
        [ 1 , 4 , 4 , 2 , 2],
        [ 1 , 3 , 3 , 0 , 5],
        [ 1 , 2 , 4 , 3 , 0],
        [ 3 , 3 , 0 , 4 , 2],
        [ 1 , 3 , 4 , 5 , 3],
]
print(' 최대 황금 미로 에서 얻을 수 있는 황금 개수 : ' , solution() )

