
"""
    삽입정렬

    before= [ 188 , 162 , 168 , 120 ]
    after = [ ]

        i = 0 일때
            data = 188  -> findinsertIdx( after , 188 )
            after = [ ]        -> findIdx = -1
                return 0        ->  after.insert( 0 , 188 )
        i = 1 일때
            data = 162  -> findinsertIdx( after , 162 )
            after = [ 188 ] -> findIdx = 0
                :return 0       -> after.insert( 0 , 162 )

        i = 2 일때
             data = 168  -> findinsertIdx( after , 168 )
             after = [ 162 ,  188 ]     -> finidx = 1
                return 1        ->  after.insert( 1  , 168  )

        i = 3 일때
             data = 120  -> findinsertIdx( after , 120 )
            after = [ 162 ,  168 , 188 ] ->   findIdx = 0
                return 0  ->  after.insert( 0 , 120  )

          after = [ 120 ,162 ,  168 , 188 ]




"""
# 1. 삽입할 데이터의 위치를 찾는 함수
def findinsertIdx( ary , data ) :       # 1. 인수 : 새로운 배열 , 삽입할 데이터
    findIdx = -1                                # 2. 삽입할 데이터의 인덱스 저장하는 변수
    for i in range( 0 , len(ary) ) :       # 3. i는 0부터 새오운 배열의 길이까지 1씩 반복 증가
        if ary[i] > data :                      # 4. i번째 인덱스의 데이터보다 삽입할 데이터가 더 작으면
            findIdx = i                          # 5. 해당 인덱스를 저장
            break                                 # 6. 반복문 종료
    if findIdx == -1 :                         # 7. 만약에 -1 이면 [ 못찾음 ] -> 가장 뒤에 삽입 -> 배열의 길이 -> 마지막인덱스
        return len( ary )
    else:                                           # 8. 아니면  찾은 인덱스 반환
        return findIdx

# 정렬 전 리스트
before = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
print('정렬 전 : ' , before )

after = [ ]

# 정렬 실행
for i in range( len(before) ) :                 # 1. i는 0 부터 기존 배열 길이만큼 1씩증가 반복
    data = before[i]                                 # 2. i번째 인덱스의 데이터를 저장
    inpos = findinsertIdx( after , data )   # 3. 삽입할 데이터의 위치 찾기 [ 인수 : 새로운배열 , 찾고자하는 데이터 ]
    after.insert( inpos , data )                 # 4. 새로운 배열에 찾은 인덱스위치에 데이터 삽입

# 정렬 후
print('정렬 후 : ' , after )