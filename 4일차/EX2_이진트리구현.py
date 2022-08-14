"""
    이진트리 구현
"""
#1. 이진트리형 노드 클래스[ 미리 구성된 설계도 ] 선언
class TreeNode( ) : # 1. 클래스 선언한다.
    def __init__(self):     # 2. 객체 생성자[ 객체 생성시 기본값 ] 설정
        self.left = None           # 1. 왼쪽 자식 노드를 연결 할 필드
        self.data = None        # 3. 데이터
        self.right = None       # 2. 오른쪽 자식 노드를 연결 할 필드

# 2. 노드 객체 생성
# [1]
node1 = TreeNode( )     # 클래스를 이용한 객체 선언 [   변수명 = 클래스명() ]
node1.data ='유재석'
# [2]
node2 = TreeNode( )
node2.data = '강호동'
# [ 1 ] -> left -> [ 2 ]
node1.left = node2      # 유재석 노드의 왼쪽 자식 노드를 강호동 노드로 연결
# [3]
node3 = TreeNode( )
node3.data ='신동엽'
# [ 1 ] -> right -> [ 3 ]
node1.right = node3     # 유재석 노드의 오른쪽 자식 노드를 신동엽 노드로 연결
# [4]
node4 = TreeNode( )
node4.data = '서장훈'
# [2] -> left -> [4]        # 강호동 노드의 왼쪽 자식 노드를 서장훈 노드로 연결
node2.left = node4
# [5]
node5 = TreeNode( )
node5.data ='하하'
# [3] -> right -> node5     # 신동엽 노드의 오른쪽 자식 노드를 하하 노드로 연결
node3.right = node5

"""
    각 노드는 LEFT , DATA , RIGHT 
    
                                         L   유재석  R 
                                         
                      L   강호동  R                            L  신동엽  R 
      
      L  서장훈 R                                                                  L  하하  R 
"""
# 트리 순회[호출]
# 1. 전위 순회 함수       :   data -> left -> right
def preodrder( node ) :
    if node == None : # 만약에 node가 존재하지 않으면
        return # 종료
    print( node.data , end='-->')
    preodrder( node.left )      # 재귀함수 [ 함수안에서 현재함수 재호출 ]
    preodrder( node.right )
# 2. 중위 순회 함수       : left -> data -> right
def inorder( node ) :
    if node == None :
        return
    inorder( node.left )
    print( node.data , end = '-->')
    inorder( node.right )
# 3. 후위 순회 함수       : left -> right -> data
def postorder( node ) :
    if node == None :
        return
    postorder( node.left )
    postorder( node.right)
    print( node.data , end ='-->')

# 전위순회함수 실행
print()
print(' 전위 순회 : ' , end = ' ')
preodrder( node1 )
print( 'end')
# 중위순회함수 실행
print()
print('중위 순회 : ' , end = ' ')
inorder( node1 )
print('end')
# 후위순회함수 실행
print()
print('후위 순회 : ' , end =' ')
postorder( node1 )
print('end')

























