"""
    스택 구현
"""
# 1. #배열[리스트] 선언
stack = [ None, None , None, None,None]
# 2. top 위치 정하기
top = -1
# 3. 최대 저장할수 있는 데이터 수
size = len(stack)       # 리스트의 길이

# 스택 출력 함수
def stack_print() :
    print("--------------- 스택 상태 -----------")
    print(' top 위치 : ' , top )
    for i in range( len(stack)-1 , -1 , -1 ) :
        print( stack[i] )
# 스택 비어있는 공간이 있는지 체크 함수
def isStackFull() :
    if top >=size :     # 만약에 top 위치가 저장할수있는 최대수 보다 크면
        print('안내)스택 모두 찼습니다. ')
        return True
    else :
        print('안내)비어 있는 자리가 존재합니다.' , ( size-top)-1 , '개 남았습니다. ')
        return False

# 스택 상태 확인
stack_print()   #  top   -1 이면 데이터가 없는 상태
isStackFull()   # 비어있는 수 체크
# 데이터 추가한다.     [ PUSH ]
top += 1           # top +1
stack[top] = '유재석'
# 스택 상태 확인
stack_print()
isStackFull()   # 비어있는 수 체크
# 데이터 추가한다.
top += 1           # top +1
stack[top] = '신동엽'
# 스택 상태 확인
stack_print()
isStackFull()
# 데이터 삭제한다.  [ POP ]
stack[top] = None           # 현재 top 위치에 데이터를 None 변경
top -= 1                            # 현재 top -1 차감
# 스택 상태 확인
stack_print()
isStackFull()
# 데이터 삭제한다.  [ POP ]
stack[top] = None
top -= 1
# 스택 상태 확인
stack_print()
isStackFull()





