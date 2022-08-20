"""
    하노이 탑 [ 재귀 함수 ]

            3
            2
           1
        rod1        rod2         rod3

"""
def hanoi( n , rod1 , rod3 , rod2 ) :
    # n : 원판   / rod1~3 탑
    if n == 1 :     # 만약에 원판이 한개이면 rod1 -> rod3 옮긴다.
        print( rod1 , rod3 )
    else:
        # 1. 원판 n-1개를 rod1에서 rod2 로 옮기다 [
        hanoi( n-1 , rod1 , rod2 , rod3 )
        # 2. 제일 밑에 있는 원판을 rod3 로 이동
        print( rod1 , rod3 )
        # 3. rod2 에 있는 원반 n-1개를 nod3 이동
        hanoi( n-1 , rod2 , rod3 , rod1 )

hanoi( 3 , 1 , 3 , 2 )
"""
    1.  hanoi( 3 , 1 , 3 , 2 ) -> 재귀                            rod1 [ 1 2 3 ]      rod2[  ]         rod3[  ]
        2. hanoi( 2 , 1 , 2 , 3  ) -> 재귀                        rod1 [ 1 2 3 ]      rod2[  ]         rod3[  ]
            3. hanoi( 1 , 1 , 3 , 2  ) -> 1 3 -> return      rod1 [ 1 2  ]      rod2[  ]         rod3[  3 ]       
        2. 1 2 -> 재귀                                                   rod1 [ 1   ]      rod2[ 2  ]         rod3[  3 ]  
            3. hanoi( 1 ,  3 , 2 , 1   ) -> 3 2 -> return    rod1 [ 1   ]      rod2[ 2 3  ]         rod3[   ]  
        2.  1 3 -> 재귀                                                  rod1 [    ]      rod2[ 2 3  ]         rod3[  1  ]  
        
        
            
            
"""



