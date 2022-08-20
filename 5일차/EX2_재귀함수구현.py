# 재귀함수 : 함수내에서 본인의 함수를 재호출
# 1. 재귀함수 구현1 : 카운트 다운 구현
import random   # 난수 관련된 메소드 제공
import time # 시간 관련된 메소드 제공

print("------------------ 카운트 다운 구현--------------------")
def countDown( n ) :
    if n == 0 :
        print('시작')
        return
    else :
        print( n , '초' )
        time.sleep( 1 ) # 1초간 정지
        # time.sleep( 초 ) : 해당 초 만큼 일시정지
        countDown( n-1 )

countDown( 5 )
""" 
    1. countDown( 3 ) -> n = 3 -> false -> 3초 -> 1초정지 -> 재귀
        2. countDown( 2 ) -> n =2 -> false -> 2초 -> 1초정지 -> 재귀 
            3. countDown( 1 ) -> n=1 -> false -> 1초 -> 1초정지 -> 재귀
                4. countDown(0) -> n=0 -> true -> 시작 -> return
"""
print("----------------- 별 출력 ----------------------")
def startprint( n ) :
    if n > 0 :
        startprint( n-1 )
        print( '★' * n )

startprint( 5 )
"""
    1. startprint( 3 ) -> true -> 재귀                             -> print( '★★★')
        2. startprint( 2 ) -> true -> 재귀                    -> print( '★★')
            3. startprint( 1 ) -> true -> 재귀            -> print( '★')
                4. startprint( 1 ) false 
"""
print("----------------- 별 출력2 ----------------------")
"""
      ★
   ★★
★★★
"""
print("----------------- 구구단  ----------------------")

"""
    print 에서 사용되는 형식( 모양=포멧) 문자 = 형식문자 = format( ) 
        %d : 10진수       %2d : 2칸 자리 차지 [ 해당 자릿수에 수가 없으면 공백처리  ]
                                %0d : 2칸 자리 차지 [ 해당 자릿수에 수가 없으면 0 으로 처리 ] 
        %f : 실수 
        %s : 문자열  
"""

def gugudan( dan , gob ) :
    print(' %2d X %2d = %02d ' %( dan , gob , dan*gob ) , end = ' ' )
    if dan < 9 :
        gugudan( dan+1 , gob ) # 재귀

for gob in range( 1 , 10 ) :
    gugudan( 2 , gob )
    print( )

"""
    gob 1일때 
    1. gugudan( 2 , 1 ) -> 2*1 -> true -> 재귀 
        2. gugudan( 3 , 1 ) -> 3*1 -> true -> 재귀 
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                gugudan( 9 , 1 ) -> 9*1 -> false 
    ~~~~~~~
    gob 9일때
    
"""
print("-----------------  배열의 총합계   ----------------------")
def arysum( arr , n ) :
    if n <= 0 :
        return arr[0]
    return arysum( arr , n-1 ) + arr[n]

# 배열내  10 ~ 20 정도의 난수 값( 0~500)을 저장하는 배열
ary = [ random.randint( 0 , 500 ) for _ in range(random.randint(10,20) ) ]

print('배열내 요소들 ' , ary )
print('배열의 총합계 : ' , arysum( ary , len(ary)-1  ) )

print("-----------------    피보나치  수열    --------------------")
# 피보나치 수열 : 어떤 값이 앞에 있는 두 값을 더한 값 같았을때 수열
"""
    1    1     2     3      5      8 
       +
             =  2
             +
                   =  3
                   +      =  5
                            +     =   8 
"""
def fibo( n ) :
    if n == 0 :
        return  0
    elif n == 1 :
        return 1
    else :
        return fibo( n-2 ) + fibo( n-1 )
        # 앞앞 항  + 앞 항  => 현재 항
print( '피보나치 수열 => ' , end = ' ')
for i in  range( 2 , 20 ) :
    print( fibo(i) , end= ' ')






















