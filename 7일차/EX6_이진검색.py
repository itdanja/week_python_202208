"""
    * 이진(이분) 검색
"""

def binSearch( ary , fdata ) :
    pos = -1                    # 검색된 결과의 인덱스를 저장하는 변수
    start = 0                    # 시작인덱스 변수
    end = len( ary ) -1    # 끝인덱스 변수 [ -1 하는이유 ( 인덱스 0부터시작 길이 1부터시작 ) ]

    while start <= end :            # start 부터 end 까지 반복처리
        mid = (start + end) // 2      # 시작점+끝점 // 2   --> 가운데 인덱스
        if fdata == ary[mid] :      # 만약에 가운데 인덱스의 데이터와  찾는 데이터와 같으면
            return mid
        elif fdata > ary[mid] :           # 만약에 가운데 인덱스의 데이터가 찾는 데이터 보다 더 크면
            start = mid+1               # 시작점을 가운데인덱스+1 변경
        elif fdata < ary[mid] :      # 만약에 가운데 인덳의 데이터가 찾는 데이터 보다 작으면
            end = mid-1             # 끝점을 가운데인덱스 -1 변경
    return pos

# 임의의 배열 [ 정렬이 되어 있는 상태 ]
dataAry = [ 50 , 60 , 105 , 120 , 150 , 160 , 162 , 168 , 177 , 188 ]
fdata = int( input('검색할 데이터 : ') )
pos = binSearch( dataAry , fdata )
if pos == -1 :
    print( fdata,'가 없습니다. ')
else:
    print( fdata,'는 ', pos, ' 위치에 있습니다.')


'''
    순서도 
        배열 = [ 50 , 60 , 105 , 120 , 150 , 160 , 162 , 168 , 177 , 188 ]
        검색 : 162    ,   165
    
        1.
                start = 0       end = 9         mid = 4
                    배열[4] : 150     <     162
                     
        2. mid 기준에서 오른쪽 값 검색 [ start 이동 ] mid+1
                start = 5       end = 9         mid = 7
                    배열[7] : 168   > 162
                    
        3. mid 기준에서 왼쪽 값 검색 [ end 이동 ] mid -1 
                start = 5       end = 6         mid = 5
                    배열[5] : 160  < 162
        4. mid 기준에서 오른쪽 값 검색 [ start 이동 ] mid+1
                start = 6       end = 6         mid = 6
                    배열[6] : 162 ==  162  ------> return
                    배열[6] : 162  < 165    start 와 end 같으면 return

'''















