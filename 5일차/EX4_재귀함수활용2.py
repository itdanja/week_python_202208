# 프랙탈[ fractal ] : 일부 작은 조각이 전체와 비슷한 형태
    # 나무줄기 , 번개 , 나뭇잎 등

import turtle   # 터틀[거북이] : 파이썬 그리기 GUI[그래픽]

def tree( len ) :       # len 이동길이
    if len > 5 :
        t.forward( len )        # len 만큼 앞으로 이동
        t.right( 20 )               # 오른쪽으로 20도 회전
        tree( len-15 )          # 재귀 [ len -15 ]
        t.left( 40 )                # 왼쪽으로 40도 회전
        tree( len-15 )          # 재귀 [ len - 15 ]
        t.right( 20 )               # 오른쪽으로 20도 회전
        t.backward( len )       # 이동[forward] 한 만큼 되돌아오기

t = turtle.Turtle() # 터틀 객체 생성
t.left( 90 )            # 90도 왼쪽 회전
t.color( 'red')     # 터틀 선 색상  설정
t.speed( 10 )        # 터틀 속도 설정 [ 1 = 가장 느리게 ]

tree( 120 )

"""
    알고리즘[순서도]
    1. tree( 30 ) -> true - > 30이동 -> 오20회전 -> 재귀 
        2. tree( 15 ) -> true -> 15이동 -> 오20회전 -> 재귀 
            3.tree( 0 ) -> false 
        2. -> 왼40회전 -> 재귀 
            3.tree( 0 ) -> false 
        2. -> 오20회전 -> 되돌아오기 
    1. -> 왼 40회전 -> 재귀 
        2. tree( 15 ) -> true -> 15이동 -> 오 20회전 -> 재귀 
            3.tree( 0 ) -> false 
        2. -> 왼 40회전 -> 재귀
            3. tree( 0 ) -> false 
        2. -> 오20회전 -> 되돌아오기 
        
    1 -> -> 오20회전 -> 되돌아오기 

"""


# t = turtle.Turtle() # 터틀 객체 생성
# t.forward( 200 )         # 터틀 전진
# t.left( 90 )                # 터틀 왼쪽 90도 회전
# t.forward( 200 )
# t.left( 90 )
# t.forward( 200 )
# t.left( 90 )
# t.forward( 200 )

