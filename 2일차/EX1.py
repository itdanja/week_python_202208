# 자료구조 : 데이터를 효율적!! 으로 저장/관리 하는 방법
"""
    1. 리스트
        1. 종류 : 1.선형리스트 2.연결리스트 3.원형 연결리스트
    선형리스트
        1. 데이터를 일정한 순서로 나열한 자료구조
        2. 입력한 순서대로 저장하는 데이터에 해당
        3. 메모리도 차례대로 저장된다.
        예) 식당 : 웨이팅   // 코로나선별소
        파이썬 : [  ]    vs  자바 : arraylist   vs C언어 : 배열
    선형리스트 구현
        # 시나리오 : 학생명 등록하고 순서대로 저장~
            # 1. 학생들을 저장할 배열( 파이썬 배열x -> 리스트 사용) 선언
            # 2. 학생 등록시 배열내 메모리 할당 [ None ]
            # 3. 만약에 배열내 중간 삽입 할경우 -> insert 구현
                        1. 해당 위치[인덱스] 입력받는다 [ position ]
                        2. 마지막 인덱스에 None 메모리 할당
                        3. 해당 position 까지 None 한칸씩 이동
"""
names = [ '유재석' , '강호동' , '신동엽'] # 1.전역변수 배열(리스트) 선언
# 1. 학생 등록 함수
def add_data( name ) :          # def 키워드 : 함수를 만들겠다는 키워드(단어)
# add_data 함수를 정의하는데 인수(=함수 안으로 들어오는 데이터) 는 name
        names.append( None )        # 2. 리스트에 None 공백 추가
        # 리스트명.append( ) : 리스트내 항목 추가
        count = len( names )            # 3. 리스트에 길이 구하기
        # len( 리스트명 )   : 해당 리스트의 길이(항목개수) 구하기
        names[ count -1 ] = name    # 4. 최근 추가된 마지막 인덱스에 인수를 대입
        # 길이 : 1 ~~   인덱스 : 0 ~                길이 -> 인덱스  : -1
# 2. 학생 등록 중간에 추가 함수   [  insert 함수 구현 하는 방식 ]
def insert_data(  position , name ) :
        names.append( None )                                    # 1. None 공백 추가  [ 메모리 효율성 때문에 ]
        count = len( names )                                    # 2. 배열의 길이 구한다. [ 마지막 인덱스 찾기 ]
        for i in range( count-1 , position , -1 ) :     # 해당 position 뒤 인덱스 데이터 한칸씩 이동
                # i는 마지막인덱스부터 입력받은 위치 미만까지 1씩 차감
                names[i] = names[i-1]
                names[i-1] = None       # None position 까지 한칸씩 이동

        names[position] = name          # 반복문 끝났으면 position 에 데이터 대입

add_data( '서장훈')
insert_data(1 , '하하')
print( ' 배열내 항목들 : ' , names )

# 알고리즘[순서도]
"""
        시나리오 
                1. 리스트 = [ 유재석 , 강호동 ]
                2. 첫번째 위치에 신동엽 추가 
        순서도 
                1. 리스트 = [ 유재석 , 강호동 , None ] 
                2. 길이 구하자 = count : 3 
                3.  position : 0         
                        반복문 
                                i  2일때         
                                        names( 2 )  = names( 2-1 )       // None = 강호동 
                                        naems(2-1) =None                        
                                                결과 : [ 유재석 , None , 강호동 ] 
                                i  1일때
                                        names( 1 )  = names( 1-1 )      // None = 유재석 
                                        names( 1-1 ) = None 
                                                결과 : [ None , 유재석 , 강호동 ] 
"""





