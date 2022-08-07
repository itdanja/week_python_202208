"""
    선형 리스트 [ Linear List ]
    연결 리스트
        선형 vs 연결
        1. 순서대로 vs 연결
        2. 인덱스 사용 vs 노드 사용
                인덱스 형식  :   [ 0 , 1 , 2 ,3 ,4 ]
                    1. 인덱스(저장되는 순서 번호 ) : 검색 속도 빠름
                노드형식  :      1 ---->    2 ---->  3 ----> 4
                    [  1.머리(앞노드연결) 2.몸(데이터) ]
                    1. 연결형식 : 중간 삽입/삭제 빠름
        3. 노드 구현 시나리오
                1. 노드 클래스( 데이터 , 링크 ) 구현

        * 왜?? 객체지향
                4차 산업혁명 : AI(자동) 빅데이터( 많은 자료 제공 ) --- 대량생산 --> 수익(돈)
                    빠르고 자동적으로  => 컴퓨터 가능
        * 클래스
            * 객체 지향
                * 객체 [ object ] : 사전(미리)적인 정의로 실제 존재하는 것을 말한다
                    * 사전적인 정의 = 클래스
                    * 클래스로 정의된 실제 메모리
                    * 객체 선언 [ 파이썬 방식 ]
                        변수명 = 클래스명()        =  객체
                    * 객체가 클래스내 필수/메소드=함수 호출시
                        객체명.필드명
                        객체명.함수( )
            * 클래스 : 미리 정의된 설계도
                * 변수와 함수 미리 정의
                * 클래스 선언 [ 파이썬 방식 ]
                    class 클래스명() :

            클래스( 설계 ) -- 메모리(인스턴화) ---> 객체

        * 자동차 클래스 [ 핸들 , 바퀴 , 문 등 ]
                객체1 = [ 핸들 = 노랑 , 바퀴 = 세모 , 문 = 파랑 ]
                객체2 = [ 핸들 = 빨강 , 바퀴 = 동그라미 , 문 = 초록 ]
            * 설계는 같지만 설계 안에 있는 필드(내용물) 다를수 있다.
"""
# 1. class 선언 키워드 [ 클래스 만들겠다는 의미 ]
class Node( ) :                 # 1. Node 이름으로 클래스 선언
    def __init__(self):         # 2. 객체 생성시 자동으로 초기값 설정 함수 [ 생성자 ]
        self.data  = None           # 3. 데이터 저장되는 변수
        self.link   = None          # 4. 연결된 노드의 변수
# 2. 데이터 추가 [ Node 객체 생성 ]
node1 = Node()                      # 1. 객체 생성      = 노드( data , link ) 1개 생성
node1.data ='유재석'               # 2. 객체내 필드 호출 해서 값 대입
print( node1.data , end = ' ')
# 3, 데이터 추가
node2 = Node()                      # 1. 객체 생성
node2.data = '강호동'              # 2. 생성된 노드에 값 대입
node1.link = node2                # 3. 생성된 노드의 링크를 앞전 노드의 객체 대입             Node1.link  <----- Node2
print( node1.link.data , end =' ')  # Node1 --link--> Node2
# 4. 데이터 추가
node3 = Node()
node3.data = '신동엽'
node2.link = node3              #   유재석 --link--> 강호동 --link--> 신동엽     설정
print( node1.link.link.data , end=' ')

# 5. 데이터추가
node4 =Node()
node4.data ='김희철'
node3.link = node4
print( node1.link.link.link.data , end =' ')
print()

# 모든 노드 출력
def node_print() :
    current = node1     # current : 현재 위치의 노드 = head(처음)부터시작
    print( current.data , end = ' ')
    while current.link != None :         # 노드의 링크가 없을때 (  None ) 까지 반복
        current = current.link                  # 현재위치 의 노드를 -> 링크된 노드로 이동
        print( current.data , end = ' ')       #
    print( )

#6. 중간 데이터 삽입
insertnode = Node()
insertnode.data = '하하'
                        # 현재 : 유재석 - 강호동 - 신동엽 - 김희철
insertnode.link = node1.link #  하하.링크 ---> 유재석(강호동)
node1.link = insertnode # 유재석(강호동) ---> 하하
                        # 유재석  -> 하하 -> 강호동 -> 신동엽 -> 김희철
node_print()




