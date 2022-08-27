"""
    순차검색[ 중복 검색이 가능한 ]
"""
def seqSearch( ary , fdata ) :
    poslist = [ ]   # 검색된 인덱스를 여러개 저장하기 위한 배열 선언
    size = len( ary )
    for i in range( size ) :
        if ary[i] == fdata :
        # 만약에 i번째 인덱스의 데이터가 검색할데이터 와 같으면
        # poslist에 찾은 데이터의 인덱스 저장
            poslist.append( i )
    return poslist # 함수 종료시 poslist 반환

# 임의의 배열[ 중복값이 존재하는 리스트]
dataAry = [ 188 , 50 , 168 , 50 , 105 , 120 , 177 , 50 ]
# 검색 데이터 입력받기
finddata = int( input('검색할 데이터 : ') )
poslist = seqSearch( dataAry , finddata )
if poslist == [ ] : # 만약에 postlist 배열이 비어 있으면
    print( finddata,'가 없습니다.')
else :
    print( finddata,'는 ', poslist, '위치에 있음')
