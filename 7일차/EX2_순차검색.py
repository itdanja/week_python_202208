"""
    순차검색 : 정렬이 안되어 있는 상태에서 검색[찾기/탐색]
"""
# 순차검색 구현 [ for문 이용한 ] : 중복검색 불가능
def seqSearch( ary , fdata ) :  # 인수 : 배열 , 검색할데이터
    pos = -1                                # 검색 성공시 의 찾은 인덱스 위치를 저장할 변수 [ -1 : 인덱스 없다 -> 검색X ]
    size = len( ary )                   # 배열의 길이
    for i in range( size ) :        # 배열의 길이만큼 반복
        if ary[i] == fdata :          # 만약에 i번째 인덱스의 데이터가 검색할 데이터와 같으면
            pos = i                         # 해당 인덱스를 pos 변수에 저장
            break                       # 찾았으면 반복문 종료
    return pos                      # 함수 종료시 찾은 pos변수를 반환

# 임의의 배열[리스트]
dataAry = [ 188 , 150 , 168 , 162 , 105 , 120 , 177 , 50 ]
# 검색 데이터 입력
finddata =  int( input("검색할 데이터: ") )
pos =  seqSearch( dataAry , finddata )
if pos == -1 : # 만약에 -1 이면 인덱스 없다
    print( finddata , '가 없습니다. ')
else :
    print( finddata , '는 ' , pos , '위치에 있음 ')






