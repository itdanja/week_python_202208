# : 한줄 주석 처리 [ 실행x = 컴파일x ]
"""
    여러줄 주석 [ ctrl + / ]
"""
"""
    목표  
        1. 기본 파이썬 문법 정리 
        2. 자료구조/알고리즘 정리 [ 암기X -> 블로그/노션 등 ]
        3. 문제풀이 
    자료 구조 
        1. (*효율 적인) 자료[데이터] 조직 , 관리 , 저장 
        2.  예 ) 도서관  [ 특정 기준 으로 정리된 책들  -> 찾기 편하다 ] 
    알고 리즘 [ 순서도 ]
        1. 문제 해결을 위한 정해진 절차 
        2. 예) 라면레시피 -> 컴퓨터(코드)
        * 엘레베이터 순서도  [ 20개이상 한글로 작성 ] / 신호등 순서도
"""

"""
    파이썬 문법
        파이참 실행 단축키 : ctrl+shift + f10 
        파이참 화면 확대/축소 : ctrl + 마우스휠
        1. print( '메시지')   : 출력 
        2. input('메시지')   : 입력 
        3. 변수명 = 값          : 저장[ 변수-데이터 1개를 저장할수 있는 메모리(공간) ]
            변수( 변하는 수 ) vs 상수( 고정된 수 )
              [선언] 변수명 = 데이터
              [호출] 변수명
              [수정] 변수명 = 새로운 데이터 
        4. 연산자 
            1. 산술연산자 : +더하기 -빼기 *곱하기 **거듭제곱 /나누기(실수) //나누기(정수) %나누기(나머지)
            2. 대입연산자 : 
                    = 대입( 오른쪽 데이터를 왼쪽 데이터에 대입 )
                    += -= *= **= /= //= %=      
                    변수 = 변수 + 1         vs      변수 += 1 
            3. 비교연산자 == 같다 !=같지않다[아니다/다르다] >초과 <미만 >=이상(크거나같다) <=이하(작거나같다)    
                    * 결과는 참(true) 혹은 거짓(false)
            4. 논리연산자  
                    * 비교연산자 2개 이상 일 경우의 하나의 결과 
                    and : 이면서 면서 이고 모두 그리고 [ 모두 참이면 결과 참 ]  동생이 사탕 이면서 초콜릿 
                    or : 이거나 거나 하나라도 또는 [ 하나라도 참 이면 결과 참 ]  동생이 사탕 이거나 초콜릿 
                    not : 반전 [ true -> false / false -> true ]
"""
print('내용 출력합니다.')         # 출력한다.
변수 = input('입력 : ')             # 입력받은 값을 변수에 저장한다.
print('입력한 내용 : ' , 변수 )   # 변수를 출력한다 .

변수1 = 10
변수2 = 3
print( "더하기 : " , (변수1+변수2) , "   빼기 : " , (변수1-변수2) , "  곱하기 : " , (변수1*변수2)   )
print( "나누기(실수) : " , (변수1/변수2) , "    나누기(정수) : " , (변수1//변수2) , "   나누기(나머지) : " , (변수1%변수2) )

변수1 += 2       # vs 변수1 = 변수1+2
print("변수1의 복합대입 : " , 변수1)

print(" 같다 : " , (변수1==변수2) , "  같지않다 : " , (변수1 != 변수2 )  , "   초과 :  ",  (변수1>변수2)  , "   미만  : " , (변수1<변수2) )
print(" 이상 : " , (변수1>=변수2) , "  이하 : " , (변수1<=변수2) )

변수3 = 5
print( 변수1 > 변수2 and 변수1 > 변수3 )            # true and true => true
print( 변수1 > 변수2 or 변수1<변수3 )                   # true or false => true
print(  not(변수1 > 변수2 or 변수1 < 변수3 )  )     # true or false => true    반대  false
















