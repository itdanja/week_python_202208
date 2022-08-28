"""
    배낭 문제
        [조건]
            1. 여행자의 배낭에 넣을수 있는 최대무게 = 7kg
            2. 여행 경로에 보석 4가지
                금고 6kg 13억
                수정 4kg 8억
                루비 3kg 6억
                진주 5kg 12억
            3. 배낭에 최대 가격으로 보석 담기 찾기
"""
# 1. DP로 풀이 가능한 문제 판단
#   - 특정한 조건에 반복적인 계산이 있을경우
# 2. 문제의 변수 확인
#   - 문제 내 변수의 개수 파악[ 4개 ]
# 3. 변수들의 관계식 확인 [ 표 구현  ]
# 4. 메모
# 5. 구현
def solution() :
    # 2차원의 빈배열[리스트] 생성 [ 메모이제이션 배열 = 기록 방식 ]
    array = [ [ 0 for _ in range( 최대배낭무게+1) ]  for _ in range( 보석개수+1) ]
    print('보석\kg 1k 2k 3k 4k 5k 6k 7k ')
    for 행 in range( 1 , 보석개수+1 ) :          # 보석개수 = 행
        print( 행 , '개--> ' , end =' ')
        for 열 in range( 1 , 최대배낭무게+1 ) :        # 최대배날무게 = 열
            print( "%2d " % array[행][열] , end =' ')
            # %2d : 형식[서식]문자
                #   %d : 정수     %s : 문자
                #   %숫자d : 숫자만큼 자리차지
        print( )

최대배낭무게 = 7        # 최대 배낭 남을수 있는 수 7kg
보석개수 = 4            # 보석 수 4개
보석무게 = [ 0 , 6 , 4 , 3 , 5 ]    # 0 , 금괴 , 수정 , 루비 , 진주  순으로 무게
보석가격 = [ 0 , 13 , 8 , 6 , 12 ]  # 0 , 금괴 , 수정 , 루비 , 진주 순으로 가격

최대배낭가격 = solution()
print('배낭에 담을수 있는 보석의 최대 가격 ----------->  ' , 최대배낭가격 , '억원')



"""
        2차원 배열 
                col[열] = 무게  row[행] = 보석개수
                * 관계식 : 보석의 개수가 증가할때마다 무게는 증가한다.
                
            보석개수/무게     1kg     2kg     3kg     4kg     5kg     6kg     7kg
                0개
                1개
                2개
                3개
                4개 
                
                 
        
"""


