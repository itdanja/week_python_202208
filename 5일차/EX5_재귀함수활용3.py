"""
    시에르핀스키 도형
        * 삼각형
    def draw(  len , n ) :
        if n >= 1
            for i in range( 3 ) :
                t.forward( len )
                t.left(120)
                draw( len/2 , n-1 )
        * 사각형
"""
import turtle

def draw(  len , n ) :
    # len : 전체 삼각형의 길이
    # n : 재귀 횟수
    if n >= 1 :
        for i in range( 3 ) :
            t.forward( len )
            t.left(120) # 120 x3 => 360도 -> 삼각형의 세변 각도
            draw( len/2 , n-1 )#재귀

t = turtle.Turtle( )
t.speed( 10 )

draw( 300  , 5 )   # 재귀 횟수는 홀수
"""
    순서도 [알고리즘]
    1. draw( 100 , 3 ) -> true -> 100이동 -> 재귀 
        2. draw( 50 , 2 ) -> true -> 50이동 -> 재귀 
            3. draw( 25 , 1 ) -> true -> 25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
            3.  25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
            3. 25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
        2. 50 이동 -> 재귀 
            3. draw( 25 , 1 ) -> true -> 25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
            3.  25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
            3. 25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
        2. 50 이동 -> 재귀 
            3. draw( 25 , 1 ) -> true -> 25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
            3.  25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false 
            3. 25이동 -> 재귀 
                4. draw( 12.5 , 0 ) -> false  
    ~~~~~~        

"""



# # 삼각형 그리기
# for i in range(3) :
#     t.forward(100)
#     t.left( 120 )