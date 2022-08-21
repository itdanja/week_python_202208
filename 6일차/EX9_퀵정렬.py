"""
    퀵정렬 구현

    순서도[알고리즘]
    1.quickSort(   [ 188 , 162 , 168 , 120 , 50 ] )
        1. pivot = 168
        2. left = [ 162 , 120 , 50 ]  -> 재귀

            2. quickSort(  [ 162 , 120 , 50 ]  )
                pivot = 120
                left = [ 50 ]   -> 재귀 ->  return  [50]
                right = [ 162 ] -> 재귀 -> return [162]

             [ 50 120 162 ]

            right = [ 188  ] -> 재귀 -> return -> [ 188 ]

      [ 50 120 162 188 ]
----------------------------------------------
    기준 : 8//2 -> [4] -> 50
     188 , 162 , 168 , 120 , 50 , 150 , 177 , 105

                            50
           left                                 right
                                            188 , 168 , 120 , 150 , 177 , 105

                                                                150

                                        left                                        right
                               120  , 105                                     188 , 168 , 177 ,

                                105                                                     168
                    left                    right                          left                 right
                                                120                                                 188 , 177

                                                                                                    177
                                                                                        left                right
                                                                                                                    188


























"""
def quickSort( ary ) :
    n = len( ary )          # 1.배열의 길이
    if n<=1 :                       # 만약에 배열에 요소 1개 있으면
        return ary                # 정렬할 필요가 없음
    pivot = ary[ n//2 ]   # 2. 기준 [ 중간에 있는 값으로 선정 ]
            # 0 1 2         -> 3//2   -> 1
            # 0 1 2 3 4   ->  5// 2   -> 2.5 -> 2
            # 0 1 2 3 4 5  -> 6//2   -> 3
    left = [ ]      # 기준보다 작은 데이터들
    right = [ ]     # 기준보다 큰 데이터들

    for i in ary :      # 배열에 요소 하나씩 꺼내오기
        if i< pivot :       # 해당 데이터가 기준보다 작으면
            left.append( i )           # 왼쪽 배치
        elif i > pivot :   # 해당 데이터가 기준보다 크면
            right.append( i )       # 오른쪽 배치
    # * 중요~~~ [ 재귀함수 이용 ]
    return quickSort( left ) + [ pivot ] + quickSort( right )

# 정렬 전 리스트
before = [ 188 , 162 , 150 , 162 , 50 , 150 , 162 , 105 ]
print('정렬 전 : ' , before )

# 정렬 후 리스트
after =  quickSort( before )

# 정렬 실행
print('정렬 후 : ' , after )
