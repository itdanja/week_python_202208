"""
    그래프 구현
"""
# 1. 그래프 클래스 선언
class Graph( ) :
    def __init__(self , size ):
        self.size = size
        self.graph = [ [ 0 for _ in range(size) ] for _ in range(size) ]

# 2. 무방향 그래프 구현
G1 = Graph( 4 )     # SIZE 4 인 그래프 객체 선언
G1.graph[0][1] = 1; G1.graph[0][2] = 1 ;  G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1 ;  G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

# 3. 무향 그래프 출력
print(' ---------- 무방향 그래프 ----------- ')
for row in range( 4 ) :
    for col in range( 4 ) :
        print( G1.graph[row][col] , end = ' ' )
    print( )
"""
    무방향 그래프 란 ??? 
        목적 : 관계 표현시 연결 작업을 그래프하자 
        0 : 연결 안했다..      1 : 연결 했다 
        size = 4  , row = 행 , col = 열 
        대칭 구조 
# 1. 
             A   B   C   D                                                    B[강남역]
        A   0     
        B        0                                                   A[역삼역]             C[삼성역]
        C              0
        D                  0                                                      D[선릉역]
        
# 2. 
             A   B   C   D                                                      B[강남역]
        A   0   1                                                             /  
        B   1   0                                                   A[역삼역]              C[삼성역]
        C             0
        D                  0                                                       D[선릉역]
        
# 3. 
             A   B   C   D                                                      B[강남역]
        A   0   1   1                                                       /  
        B   1   0                                                   A[역삼역] --------    C[삼성역]
        C   1        0
        D                  0                                                        D[선릉역]
        
# 4. 
             A   B   C   D                                                        B[강남역]
        A   0   1   1   1                                                       /  
        B   1   0                                                   A[역삼역]  ------  C[삼성역]
        C   1        0                                                           \                    
        D   1             0                                                        D[선릉역]
        
# 5. 
             A   B   C   D                                                      B[강남역]
        A   0   1   1   1                                                       /               \
        B   1   0   1                                              A[역삼역] ------ C[삼성역]
        C   1   1    0                                                           \                    
        D   1             0                                                          D[선릉역]
# 6. 
             A   B   C   D                                                      B[강남역]
        A   0   1   1   1                                                       /              \
        B   1   0   1   0                                         A[역삼역]   -----  C[삼성역]
        C   1   1    0  1                                                       \               /
        D   1   0   1   0                                                          D[선릉역]

"""
# 4. 방향 그래프 구현
G2 = Graph( 4 )
G2.graph[0][1] = 1 ;    G2.graph[0][2] = 1
G2.graph[3][0] = 1;    G2.graph[3][2] = 1

# 5. 방향 그래프 출력
print('----------- 방향 그래프 ------------- ')
for row in range( 4 ) :
    for col in range( 4 ) :
        print( G2.graph[row][col] , end = ' ')
    print( )

"""
    방향 그래프란 ? 
        0: 연결X      1 : 방향위치 
        size = 4 , row = 행[출발지] , col = 열[도착지] 
        대칭구조 X
        
# 1. 
             A   B   C   D                                                    B[강남역]
        A   0     
        B        0                                                   A[역삼역]             C[삼성역]
        C              0
        D                   0                                                      D[선릉역]
        
# 2. 
             A   B   C   D                                                    B[강남역]
        A   0   1                                                           /[ A->B]
        B        0                                                   A[역삼역]             C[삼성역]
        C              0
        D                   0                                                      D[선릉역]
# 3. 
             A   B   C   D                                                     B[강남역]
        A   0   1    1                                                      /[ A->B]
        B        0                                                   A[역삼역]  -------> C[삼성역]
        C              0                                                                [A->C]
        D                   0                                                      D[선릉역] 
# 4. 
             A   B   C   D                                                     B[강남역]
        A   0   1    1                                                     /[ A->B]
        B                                                          A[역삼역]  --[A->C]--> C[삼성역]
        C              0                                                       \ [ D->A]    
        D   1              0                                                      D[선릉역] 
# 5. 
             A   B   C   D                                                     B[강남역]
        A   0   1    1    0                                               /[ A->B]
        B   0   0    0   0                                      A[역삼역]  --[A->C]--> C[삼성역]
        C   0   0    0   0                                                  \ [ D->A]          / [ D->C]
        D   1   0    1   0                                                         D[선릉역]   
    
"""











