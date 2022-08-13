# 자판기 프로그램
# 변수 : stack[메모리구조] , top[마지막데이터위치] , size[메모리크기]
size = int( input('해당 제품의 재고 최대 개수 : ') )                 # 정수 입력받아서 변수에 저장
stack = [ None for _ in range(size) ]                               # 입력받은 변수 만큼 배열의 크기를 정하기
top = -1                                                                            # 현재 stack 저장된 마지막 데이터 위치 [ -1 : 없다 ]
# 1. push 함수  : 데이터 추가
def push( data ) :
    global top        # 전역변수 호출
    if isStackFull() :          # 빈자리 체크 [ 빈자리가 없으면 ]
        print('안내) 재고가 모두 찼습니다. ')
        return      # 함수 종료
    top += 1
    stack[top]  = data
    print('안내) 재고상태 : ' , stack )

# 2. pop 함수 : 데이터 삭제
def pop( ) :
    global top
    if isStackEmpty() :
        print('안내) 재고가 존재하지 않습니다. [구매불가] ')
        return
    data = stack[top]       # 삭제된 데이터를 미리 변수 저장
    stack[top] = None       # 해당 위치에 데이터를 삭제
    top -= 1                        # 위치를 1 차감
    print('안내)',data,' 를 구매 했습니다.')
    print('안내) 재고상태 : ' , stack )
    return
# 3. peek 함수  : top 위치 확인
def peek() :
    if isStackEmpty() :
        print("안내) 재고가 모두 비어 있습니다.")
        return
    print('안내) 재고상태 : ' , stack )
    print('안내) top제품 : ' , stack[top] )
    return
# 4. isStackFull  함수  :  스택내 남아있는 자리 체크
def isStackFull() :
    if top >= size-1 :      # top 위치가  마지막인덱스이면
        return True         # 빈 자리가 없다 .
    else:
        return False        # 빈 자리가 있다 .

#  5. isStackEmpty 함수 : 스택이  모두 비어있는 체크
def isStackEmpty() :
    if top == -1 :          # 만약에 top위치가 -1이면 재고 없다
        return True         # 재고가 모두 없다.
    else:
        return False            # 재고가 1개이상이다.

# 6. 프로그램 시작
while True : # 무한루프[ 종료조건 : 4 입력했을때 ]
    select = int(input('1.재고추가 2.구매 3.재고확인 4.종료 중 선택 : '))
    if select == 1 :
        print('안내) 재고 추가합니다. ')
        data = input('제품명 : ')
        push( data )
    elif select == 2 :
        print('안내) 재고 구매합니다.')
        pop( )
    elif select == 3 :
        print('안내)재고 확인합니다.')
        peek( )
    elif select == 4 :
        print('안내) 프로그램 종료 ')
        break       # 가장 가까운 반복문 탈출[나가기]
    else:
        print('안내) 알수 없는 번호입니다. ')























