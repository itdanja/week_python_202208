"""
    회문 찾기
        * 회문 : 앞으로 읽었을때 와 뒤로 읽었을때 동일
"""
# 1. 임의의 문자열 리스트
단어리스트 = [ 'reaver' , 'keyak' , 'borrow or rob' , '주유소의 소유주' , '살금 살금' ]
# 2. 회문 찾기 함수
def palindrome( pstr ) :
    if len(pstr) <= 1 :     # 만약에 문자열 길이가 1보다 작으면
        return True
    if pstr[0] != pstr[-1] :        # 0번째인덱스[첫글자]   -1번째인덱스[마지막글자] 와 같지 않으면
        # 같지 않으면 true 같으면 false
        return False    # 회문이 아닙니다.
    return palindrome( pstr[ 1:len(pstr)-1] )       # 재귀

# 3.실행
for str in 단어리스트 :      # 리스트내 요소(단어) 를 하나씩 str 대입
    print( str , end = ' -----> ')
    str = str.lower().replace( ' ','')  # 소문자로 변경후 ' '공백이 있으면 '' 공백제거
        # .lower() : 영문 소문자로 변환 함수
        # .replace( '기존문자' , '새로운문자' ) : 기존문자가 새로운문자로 치환[교체]
    if palindrome( str ) :  # 함수 호출
        print('회문입니다.')
    else:
        print('회문이 아닙니다. ')
"""
    알고리즘 [ 순서도 ] 
    * reaver
    1. palindrome( reaver ) -> false - > false -> return 재귀             (return) False 
        2. palindrome( eave ) -> false -> false -> return 재귀        (return) False 
            3. palindrome( av ) -> false -> true -> return False
    * 주유소의 소유주 -> 공백제거 ->   주유소의소유주
    1. palindrome(주유소의소유주) -> false -> false -> return 재귀                (return) true 
        2. palindrome( 유소의소유 ) -> false -> false -> return 재귀            (return) true 
           3. palindrome( 소의소 ) -> false -> false -> return 재귀          (return) true 
             4.palindrome( 의 ) -> true 
"""

