# 큐 활용 : 대기 프로그램
# 0.변수 :  size[메모리크기]  , queue[리스트] , front[출구 위치] , rear[입구 위치]
SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1
# 1. enQueue함수   : 데이터 추가 함수
def enQueue( data ) :
    global rear
    if isQueueFull() :  # 만약에 빈자리가 없으면
        print('안내) 대기 인원이 모두 찼습니다. ')
        return
    rear += 1   # 입구 인덱스 증가
    queue[rear] = data  # 입구 인덱스 데이터 추가
    print('안내) 대기 현황 : ' , queue )

# 2. deQueue함수 : 데이터 추출 함수
def deQueue() :
    global front , rear
    if isQueueEmpty() :
        print('안내) 대기 인원이 없습니다.')
        return
    front +=1       # 출구 인덱스 증가
    data = queue[front] #  제거된 데이터 임시 저장
    queue[front] = None #  해당 인덱스의 데이터 제거
    # 제거된 인덱스 뒤로 한칸씩 당기기
    for i in range( front+1 , rear+1 ) : # 출구부터 입구까지
        queue[i-1] = queue[i]   # 한칸씩 데이터를 앞으로 이동
        queue[i] = None
    # 출구는 항상 -1 이여야 한다.
    front = -1
    # 입구는 한칸 당기기
    rear -= 1
    print('안내) ' , data , '님 입장 합니다. ')
    print('안내) 대기 현황 : ', queue)

# 3. isQueueFull 함수 : 모두 찼는지 체크 함수
def isQueueFull() :
    if rear >= SIZE - 1 :           # 만약에 입구가 최대인원수와 같으면
        return True                 # 빈자리 없다 .
    else:
        return False            # 빈자리 있다.
# 4. isQueueEmpty함수 : 비어 있는지 체크 함수
def isQueueEmpty() :
    if front == rear : # 출구와 입구가 위치가 동일하면 데이터가 없다.
        return True # 데이터 1개도 없다 .
    else:
        return False    # 데이터 1개이상이다.

    return
# 5. peek() :  front 위치 함수
def peek() :
    if isQueueEmpty() :
        print('안내) 다음 대기 인원이 없습니다.')
        return
    print(' 곧 입장할 고객 : ' , queue[front+1] )
    return

#6.프로그램 실행
while True :
    peek()
    select = int(input('1.대기등록 2.입장 3.종료 선택 : ') )
    if select == 1 :
        print('안내) 등록 ')
        phone = input('전화번호 : ')
        count = input('인원수 : ')
        enQueue( (phone , count) )
    elif select == 2 :
        print('안내) 입장 ')
        deQueue()
    elif select == 3 :
        print('안내) 프로그램 종료')
        break # 무한루프 종료
    else:
        print('안내) 알수 없는 번호입니다. ')





















