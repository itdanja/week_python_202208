"""
    큐 구현
"""
# 1. 배열[리스트] 이용한 구현
queue = [ None , None , None ]
# 2.
rear = -1       # 입구 위치
front = -1      # 출구 위치
# 출력 함수
def queue_print() :
    print( '[출구]<------ ' , end =' ')
    for i in range( 0 , len(queue) , 1 ) :
        print( queue[i] , end = ' ')
    print('<-----[입구] ')
# 3. 데이터 추가
rear +=1
queue[rear] = '유재석'
queue_print()

rear +=1
queue[rear] = '강호동'
queue_print()

rear +=1
queue[rear] = '신동엽'
queue_print()
# 4. 데이터 삭제
front += 1
queue[front] = None
queue_print()

front += 1
queue[front] = None
queue_print()

front += 1
queue[front] = None
queue_print()


