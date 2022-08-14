"""
    이진트리를 이용한 데이터 정렬[ 편의점 제품의 판매 수량 ]
"""
import random       # import : 현재 py파일 외 다른 미리 만들어진 파일[클래스] 불러오기 [ random클래스 : 난수 관련 메소드 제공 ]
# 1. 이진트리 노드 구현
class TreeNode( ) :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
# 2. 변수들
root = None
productlist = [ '바나나맛우유' , '레스비커피' , '츄파춥스' , '도시락' ,'삼다수','코카콜라','삼각김밥']
selllist = [ random.choice( productlist) for _ in range(100) ]  # 제품리스트에서 랜덤으로 리스트에 추가 [ 100회 ]
print( '오늘 판매된 리스트[중복o] : ' , selllist )

node = TreeNode( )                  # 노드 객체
node.data = selllist[0]            # 판매목록중 첫번째 데이터를 노드에 저장
root = node                              # 해당 노드를 root 사용

for name in selllist[ 1 :  ] :      # 판매리스트에서 1인덱스부터 마지막 인덱스까지 반복처리
    node = TreeNode()               # 노드 생성
    node.data = name                # 노드의 데이터에 노드 대입

    current = root                      # root를 현재노드 가정
    while True :        # 무한루프
        if name == current.data :       # 만약에 해당 인덱스의 data 와 현재위치의 data와 동일하면
            break                                           # 이름이 동일할경우[ 중복일 경우]  노드 추가X
        elif name < current.data :        # 현재 data보다 작으면 왼쪽노드에 연결
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :                                         # 현재 data보다 더 크면 오른쪽노드에 연결
            if current.right ==None :
                current.right = node
                break
            current = current.right

# 전위 순회 정의
def preorder( node ) :
    if node ==None :
        return
    print( node.data , end = ' ')
    preorder( node.left )
    preorder( node.right )

# 전위 순회 함수 호출
print()
print(' 오늘 판매된 물건[중복x] ---> ' , end = ' ')
preorder( root )
print()
# 메모리 확인

















