"""
    퀵정렬_개선[ 중복값 고려한 ]

"""
def quickSort( ary ) :
    n = len( ary )
    if n<=1 :
        return ary
    pivot = ary[ n// 2 ]                    # 1. 기준점 선정

    left , mid , right = [ ] , [ ] , [ ]  # 2. 왼쪽 , 중간 , 오른쪽
    for i in ary :
        if i < pivot :                  # 만약에 해당 데이터가 기준보다 작으면  왼쪽
            left.append( i )
        elif i > pivot :
            right.append( i )       # 만약에 해당 데이터가 기준보다 크면 오른쪽
        else:
            mid.append( i )         # 만약에 해당 데이터가 기준과 같으면 중간

    return quickSort( left ) + mid + quickSort( right )

# 정렬 전 리스트
before = [ 188 , 162 , 150 , 162 , 50 , 150 , 162 , 105 ]
print('정렬 전 : ' , before )

# 정렬 후 리스트
after =  quickSort( before )

# 정렬 실행
print('정렬 후 : ' , after )
