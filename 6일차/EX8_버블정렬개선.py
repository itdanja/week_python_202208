
"""
    개선된 버블정렬
         특정 스캔 회차에서  교환이 한번도 없을경우 정렬 종료
"""
def bubbleSort( ary ) :
    n = len( ary )
    for i in range( n-1 , 0 , -1 ) :
        changeCheck = False     # 교환 여부 확인 저장 변수
        print( i , "스캔---> " , ary )
        ################# 버블 정렬 #################
        for k in range( 0 , i ) :
            if ary[k] > ary[k+1] :
                ary[k] , ary[k+1] = ary[k+1] , ary[k]
                changeCheck = True  # 만약에 교환했으면 true 변경
        #########################################
        # 버블정렬 특징 : 특정 스캔에서 자리 변경이  한번도 없을경우 정렬 완료~~~~
        if changeCheck == False : # 만약에 changeCheck false이면 한번도 교환 안했다.
            break # 정렬되어 있는 상태 이므로 반복문 종료
    return ary # 함수 종료

# 정렬 전 리스트
before = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
print('정렬 전 : ' , before )

# 정렬 후 리스트
after = bubbleSort( before )

# 정렬 실행
print('정렬 후 : ' , after )
