"""
    선택 정렬 : 가장 작은 값을 찾아서 새로운곳에 배치


    188 , 162 , 168 , 120
    [ 0 ]   [ 1 ]  [ 2 ]  [ 3 ]

    minIdx = 0    [ 188 ]
        [ 188 ] > [162]  o
    minIdx = 1
        [162] >  [168]   x
        [162] >  [120]   o
    minIdx = 3

"""
# * 최소값 위치 찾는 함수 구현
def findMinIdx( ary ) :                 # 1.함수 정의 [ 인수로 배열 받기 ]
    minIdx = 0                              # 2. 가장 작은 데이터의 인덱스를 저장하는 변수
    for i in range( 1, len(ary) ) :   # 3. i는 배열내 인덱스 만큼 1씩증가반복
        if ary[minIdx] > ary[i] :      # 4. 만약에 가장작은 데이터의 인덱스보다  i번째 인덱스의 데이터가 더 작으면
            # >:오름차순    /    <:내림차순
            minIdx = i                      # 5. 해당 인덱스를 가작 작은 데이터의 인덱스로 저장
    return minIdx                         # 6. 반복문 종료후 가장 작은 인덱스 반환

# 정렬 전 리스트
before = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]

# 정렬 후 리스트
after = [ ]

print('정렬 전 : ' , before )

# 정렬 실행
for _ in range( len(before) ) :                 # 1. 배열 길이만큼 반복문 [ 반복변수 X ]
    minpos = findMinIdx( before )           # 2. before 배열에서 가장 작은 데이터의 인덱스 찾기
    after.append(  before[minpos] )        # 3. 찾은 가작 작은 인덱스를 새로운 배열에 저장
    del( before[minpos] )                        # 4. befor 배열에서 가장 작은 데이터의 인덱스를 제거
print('정렬 후 : ' , after )



