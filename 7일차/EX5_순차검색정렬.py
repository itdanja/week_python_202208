"""
    순차검색 [ 정렬이 되어 있는 상태 ]
"""
def seqSearch( ary , fdata ) :
    postlist = [ ]
    for i in range( len(ary) ) :
        if ary[i] == fdata :
            #만약에 i번째 인덱스의 데이터가 검색데이터와 같으면
            postlist.append( i ) # 배열[리스트] 추가
        elif ary[i] > fdata :   # 만약에 i번째 인덱스의 데이터가 검색데이터보다 크면
            break # 검색종료
            # [ 정렬이 되어 있는상태에서 검색데이터가 i번째 데이터보다 작으면   ]
    return postlist

# 임의의 배열
dataAry = [188,50,168,50,105,120,177,50]
# 검색 입력받기
fdata = int( input('검색 데이터 : ') )
# 정렬[ 파이썬에서 제공하는 정렬 함수 사용 ]
dataAry.sort( )      # 오름차순

poslist = seqSearch( dataAry , fdata )
if poslist == [] :
    print( fdata , '가 없습니다. ')
else:
    print( fdata ,'는 ' ,poslist,'위치에 있습니다. ')

'''
    50 50 50 105 120 168 177 188
    검색 : 120
        50 == 120
        50 == 120
        50 == 120
        105 == 120
        120 == 120  [ 찾음 ] 
        168 == 120  ~~~~~~~~~ 불필요한 코드 
        177 == 120
        188 == 120
'''


