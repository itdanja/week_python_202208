"""
    선형리스트를 이용한 활용
    구현프로그램 시나리오
        1. 이름 과 나이 를 입력받아 나이순 정렬 출력
        2. 메뉴 [ 1.등록 2.삽입 3.삭제 4.명단[정렬] 5.종료 ]
"""
# 1. 회원 등록 함수  [ 인수 : 이름 , 나이 ]
def add_data( name , age ) :
    memberlist.append(None) # 1. 마지막 인덱스에 None 추가한다.
    count = len(memberlist)     # 2. 배열의 길이
    memberlist[ count - 1 ] = ( name , age ) # 3. 마지막 인덱스의 데이터 추가
    print( "등록후 명단 : " , memberlist) # 결과
    return
# 2. 회원 삽입 함수 [ 인수 : 위치 , 이름 , 나이 ]
def insert_data( pos , name , age ) :
    memberlist.append(None)
    count = len(memberlist)
    for i in range( count-1 , pos , -1 ) :
        memberlist[i] = memberlist[i-1]
        memberlist[i-1] = None
    memberlist[pos] = ( name , age )
    print("삽입후 명단 : " , memberlist )
    return
# 3. 회원 삭제 함수
def delete_data( pos ) :
    memberlist[pos] = None
    count = len(memberlist)
    for i in range( pos+1 , count ) :
        memberlist[ i-1 ] = memberlist[ i ]
        memberlist[ i ] = None
    del( memberlist[count-1] )
    print("삭제후 명단 : ", memberlist)
    return
# 4. 정렬(나이순) 함수
def sort_data( ) :

    return

# 5. 프로그램 실행 함수
def member_start( ) :
    while True : # 무한반복 [ 종료조건 : 5 입력했을때  ]
        print("-------------------------")
        select = int( input( "메뉴 : 1.등록 2.삽입 3.삭제 4.명단 5.종료" ) )    # input( ) : 입력받기 함수   # int( 데이터 ) : int정수형 변환
        if select == 1 :        # 만약에 입력값이 1이면
            # 1. 이름 과 나이를 입력 받는다 .
            name = input("등록할 이름 : ")
            age = int( input("등록할 나이 : "))
            add_data(  name , age   ) # 2.함수의 인수 전달
        elif select == 2 :  # 만약에 입력값이 2 이면
            pos = int( input('삽입할 위치 : ') )
            name = input('삽입할 이름 : ')
            age = int( input('삽입할 나이 : ') )
            insert_data( pos , name , age  )
        elif select == 3 :  # 만약에 입력값이 3 이면
            pos = int( input("삭제할 위치 : "))
            delete_data(  pos )
        elif select == 4 :  # 만약에 입력값이 4 이면
            sort_data( )
        elif select == 5 :  # 만약에 입력값이 5 이면
            print(" 안내) 프로그램 종료 합니다. ")
            return
        else:
            print(" 안내 ) 알수 없는 번호 입니다. ")
# 6. 실행
memberlist = [  ] # 회원명단 저장할 배열[리스트] 선언
member_start()  # 프로그램 시작 함수 실행


