"""
    선택정렬 [ 교환 정렬 방식 ]

    컴퓨터에서 교환[ swap ]이란???
        두 변수간 데이터를 바꾸기
        ?? 컴퓨터는 한번에 두개이상 처리 X

        A변수                 B변수
            3                      10


                        tmp

        [  문제발생  ]
        a변수 = b변수  [ a =10 , b = 10 ]
        b변수 = a변수  [ b = 10 , a = 10 ]
        [ 문제 해결 ]
        tmp = a변수 [ a = 3 , b = 10 , tmp = 3 ]
        a변수 = b변수 [ a = 10 , b = 10 tmp = 3 ]
        b변수 = tmp [ a = 10 , b = 3 , temp = 3 ]
    -------------------------------------------------
    [ 순서도 ] : 알고리즘

    188 , 162 , 168 , 120
    [0]    [ 1 ]   [ 2]   [ 3 ]

    i = 0 일때
        k = 1일때
            188 > 162       minInx = 1
        k = 2일때
            162 > 168       minInx = 1
        k = 3일때
            162 > 120       minInx = 3
        [ swap ]
         120 , 162 , 168 , 188

    i = 1 일때
        k = 2일때
            162 > 168       minInx = 0
        k = 3일때
            162 > 188       minInx = 0
        [ swap ]
         120 , 162 , 168 , 188

    i = 2 일때
        k = 3일때
            168 > 188       minInx = 0
        [ swap ]
         120 , 162 , 168 , 188

    i = 3 일때
        x

"""
def selectionSort( ary ) :              #1. 함수 정의 [ 인수로 배열 받기 ]
    n = len( ary )                              # 2. 배열의 길이 변수
    for i in range( 0  , n-1 ) :           # 3. i는 0 부터 마지막인덱스까지
        minInx = i                                # 4. 가장 작은 인덱스 = i
        for k in range( i+1 , n ) :         # 5. 가장 작은 인덱스 다음 인덱스부터 마지막인덱스까지
            if ary[minInx] > ary[k] :       # 6. 비교 작은 인덱스 데이터보다 해당 인덱스의 데이터가 더 작으면
                minInx = k                         # 7. 가장 작은 인덱스 = k

        # 교환[ swap ]
        tmp = ary[i]
        ary[i] = ary[minInx]
        ary[minInx] = tmp

    return ary

# 정렬 전 리스트
before = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
print('정렬 전 : ' , before )

# 정렬 후 리스트
after = selectionSort( before )
# 정렬 실행
print('정렬 후 : ' , after )
