"""
    함수 : 함[상자] 수[숫자]
        * 상자 안에 들어있는 수 -> 상자에 미리 넣어둔 수  -> 미리 정의된 수[코드]
        * 목적 :
               *1. 코드의 재활용성[ 반복적으로 사용되는 코드를 미리 만들어서 재사용 ]
             **2. 메모리의 효율성 [ 함수 안에서 선언된 메모리는 return 제외만 모두 사라짐[초기화] ]
                3. 인수에 따른 서로 다른 결과물

        x=3 y=1       1. 인수[매개변수]           x = 3   y = 1
        --   ----
        |            |
        |   x+y   |      2. 함수[ 정의된 코드 ]    x+y
        |            |
        ---    --
             return     3. 반환[결과/리턴]        return 4

    재귀 : 자기 자신을 참조
    재귀함수 : 함수 안에서 현재함수를 다시 호출
        * 자기 자신을 불러내기
        * 최대 재귀 호출횟수 : 996회
"""
# 재귀함수 구현1
# def openBox()       : # 함수 정의
#     global i  # 전역변수 [ 함수 밖에 있는 변수를 호출 ]
#     i += 1 # 1씩 증가
#     print(' 상자를 열기 실행횟수 : ' , i )
#     openBox() # 함수내에서 현재 함수 호출[ 자기 자신을 호출 ] = 재귀
# i = 0
# openBox()

# 재귀함수 구현2
def openBox2( ) :   # 함수 정의
    global count
    print(' 상자 열기 ')
    count -= 1
    if count == 0 :
        print(' 선물 넣기 ')
        return
    openBox2( )
    print(' 상자 닫기 ')

count = 3
openBox2( )
# 순서도 [알고리즘]
"""
        openBox2 함수 호출 
            count = 3     상자열기      count -=1       count = 2       False
                                                                                            openBox2( ) 함수호출 
                                                                                            count = 2   상자 열기  count -=1  count = 1   False 
                                                                                                                                                              openBox2( ) 함수 호출 
                                                                                                                                                              count = 1 상자열기 count -= 1  count = 0  TRUE  선물넣기 return
                                                                                            상자닫기
            상자닫기                                                                               
"""
# 재귀함수 구현3
def plusmethod( num ) :
    if num <= 1 :# 만약에 numd이 보다 작으면 함수 종료
        return 1
    return num + plusmethod( num-1 )

num = int( input('재귀함수에 넣을 수 '))
print( '(재귀를 이용한) 1~3까지 누적합계 : ' , plusmethod( num ) )
# 순서도 [알고리즘]
"""
    1. plusmethod(3) -> num = 3 -> false -> return  3 + 재귀                            (return)3 = 6
        2. plusmethod(2) -> num = 2 -> false -> return 2 + 재귀                      (return) 1 = 3 
            3. plusmethod( 1 ) -> num = 1 -> true -> return 1                    
"""
# 재귀함수 구현4 : 팩토리얼 함수 구현
def factorial( num ) :
    if num <= 1 :
        print('[종료] 1반환 ')
        return 1
    print('%d * %d 호출 ' % ( num , num-1 ) )     # %d : 형식문자  [ 정수 형식 문자]
        # ' %d  %d'  %(값1,값2)
    val = factorial( num -1 )
    print('%d * %d = %d 반환 ' %(num , num-1 , val ))
    return num * val

num = int( input('재귀함수에 넣을 수 '))
print( '팩토리얼 결과 : ' , factorial( num ) )
"""
    1. factorial( 3 ) ->  num = 3 -> false -> return 3 * 재귀                      (return) 2 =>  2* 3  = 6 
        2.  factorial( 2 ) -> num = 2 -> false -> return 2 * 재귀             (return) 1 =>  2* 1  = 2 
            3. factorial( 1 ) -> num = 1 -> true -> return 1
"""


























