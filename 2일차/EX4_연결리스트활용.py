"""
    연결리스트 활용
        전화번호부 프로그램
        1. 이름 , 전화번호 입력받아서 명단 관리
        2. 기능 : 등록
"""
# 1. Node 클래스 선언
class Node() :
    def __init__(self):
        self.data = None        # 데이터
        self.link = None          # 링크[연결 대상]

# 2. 노드 등록 함수 선언
def add_node( name , phone ) :
    # 전역변수 호출
    global head , current , pre
    # 1. 노드 객체 선언한다.
    node = Node()
    # 2. 노드의 정보를 담는다.
    node.data = ( name , phone )
    # [조건1] 첫 노드 일경우
    if head == None :   # 가장 앞에 노드가 없으면
        head = node # 첫노드 등록
        return
    # ( 없어도 실행되는 코드) [ 조건3] 첫번째 노드보다 정렬 기준으로 헤드 교체  [  > : 오름차순    < : 내림차순 ]
    if head.data[0] > name :
        node.link = head
        head = node
        return
    # [조건2] 첫 노드가 아닐경우
    current = head      # 현재위치를 첫 노드 부터 시작
    while current.link !=None : # 마지막 노드까지 [ 노드가 2개이상일때 마지막노드 찾아서 current 로 사용]
        pre = current       # 현재노드를 이전 노드 저장
        current = current.link  # 현재노드를 다음노드로 변경
        #( 없어도 실행되는 코드) 만약에 이름순으로 정렬
        if current.data[0] > name :     # 만약에 현재노드의 이름이 새로운이름 보다 크면
            pre.link = node                   #이전노드 링크의 새로운 노드
            node.link = current             # 새로운노드 링크의 현재노드
            return
    current.link = node
    return

# 3. 노드 출력 함수 선언
def node_print() :
    current = head
    print( current.data , end = ' ')
    while current.link !=None :
        current = current.link
        print( current.data , end = ' ')
    print()
    return

# 4. 실행 함수
def phone_start( ) :
    while True :
        name = input('이름 : ')
        phone = input( '연락처 : ')
        add_node( name , phone )
        node_print()
# 5. 실행
head = None     # 1.가장 앞에있는 노드
current = None # 2.현재 노드
pre = None        # 3.이전 노드
phone_start( )


# 1. 강호동 노드 등록  -> 첫노드에 등록
#   강호동
# 2. 신동엽 노드 등록 ->   마지막 노드(None) 까지 이동
#       1. 강호동.신동엽링크
#   강호동 신동엽
# 3. 유재석 노드 등록  -> 마지막 노드
#        1. 강호동 -> 신동엽 이동
#        2. 신동엽.link -> None
#                   pre = 강호동
#                   current = 강호동.link
#         3. 신동엽.like = 새로운노드 등록







