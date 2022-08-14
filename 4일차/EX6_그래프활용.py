"""
    그래프 활용 [ 최단거리 찾기 ]
        # 조건
            1. 지역 : 춘천 , 서울 , 속초 , 대전 ,광주 , 부산
            2. 춘천 -> 부산까지의 최단거리 찾기
            3. 지역간 걸리는시간 [임의]
                    춘천-> 서울 [10]    춘천->속초[15]
                    서울-> 춘천[10]     서울->속초[40]  서울->대전[11]  서울->광주[50]
                    속초-> 춘천[15]     속초->서울[40]  속초->대전[12]
                    대전->서울[11]      대전->속초[12]  대전->광주[20]  대전->부산[30]
                    광주->서울[50]      광주->대전[20]  광주->부산[25]
                    부산->대전[30]      부산->광주[25]

            * 무방향 가중치 그래프 그리기
                                춘천
                         10             15
                서울           40         속초
                         11             12
                 50           대전
                         20            30
                광주           25         부산

"""
# 1. 그래프 클래스

class Graph( ) :
    def __init__(self , size ):
        self.size = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

# 3. 그래프 출력 함수
def Graph_print( g ) :
    print('       '  , end = ' ')       # 행/열 교차지점 칸 의 공백
    for v in range( g.size ) :      # 열에 지역명 출력하는 반복문
        print( Locationlist[v] , end = ' ')
    print()
    for row in range( g.size ) :
        print( Locationlist[row] , end = ' ')   # 열에 지역명 출력하는 반복문
        for col in range( g.size ) :
            print( "%4d" % g.graph[row][col] , end =' ')
        print()
    print()
    # %숫자d : 해당 숫자만큼 자리차지
    # %3d  : 정수 세자리 자리차지
            # 정수가 세자리가 아닐 경우 공백으로 채움
    # #03d : 정수 세자리 자리차지
            # 정수가 세자리가 아닐 경우 0 으로 채움

# 2. 조건 구현
Locationlist = ['춘천','서울','속초','대전','광주','부산']
춘천 , 서울 , 속초 , 대전 , 광주 , 부산 = 0 , 1 , 2 , 3 , 4 , 5
G1 = Graph( 6 )
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15

G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40
G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50

G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40
G1.graph[속초][대전] = 12

G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12
G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30

G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20
G1.graph[광주][부산] = 25

G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

# 4. 그래프 출력함수 호출
Graph_print( G1 )

# 5.이동시간 정렬
from operator import itemgetter
edgelist = [ ]

for i in range( G1.size ) :
    for k in range( G1.size ) :
        if G1.graph[i][k] !=0 : # 거리가 있으면
            edgelist.append( [ G1.graph[i][k] , i , k ] )
                                            #   거리      , 출발지 , 도착지
print(' 정렬 전 : ' , edgelist )
# 정렬
edgelist = sorted( edgelist , key = itemgetter(0) , reverse=True)
                                        # 정렬기준 : 인덱스(0) = 거리 ,  reverse=True[ 내림차순 ] vs 생략시 [ 오름차순 ]
print(' 정렬 후 : ' , edgelist )

# 6. 무방향 대칭 관계 -> 단방향
newary = [ ]
for i in range(0 , len(edgelist) , 2 ) :    # i는 0부터 배열의 길이까지 2씩 증가
    newary.append( edgelist[i])

print(' 단향향 정렬 : ' , newary )

# 7. 방문 기록 함수
def find( g , location ) :
    stack = [ ]     # 지역을 지나온 기록
    visitedary = [ ] # 방문한 지역
    current = 0     # 시작위치 [ 0 : 춘천 ]
    stack.append( current )
    visitedary.append( current )

    while( len(stack) != 0 ) :
        next = None     # 다음 지역 선언
        for i in range( g.size ) :
            if g.graph[current][i] != 0 : # 거리가 존재하면
                if i in visitedary  :   # 방문한 적이 있는 지점이면 x
                    pass        # 넘어가기 [ pass 키워드 ]
                else:
                    next = i    # 현재 지역을 다음지역으로 선정
                    break
        # for end
        if next != None :   # 만약에 다음지역이 있으면
            current = next      # 현재위치를 다음지역 선정
            stack.append( current ) # 스택 추가
            visitedary.append( current ) # 방문목록 추가
        else :
            current = stack.pop( )  # 스택 제거
    # while end
    if location in visitedary :     # 방문기록이 있으면
        return True
    else:
        return False

# 결과 : 거리 계산
index = 0 # 거리 순서
while( len(newary) > G1.size -1 ) : # 지역의 개수가 마지막 지역까지 반복
    start = newary[index][1]     # 출발지
    end = newary[index][2]      # 도착지
    saveTime = newary[index][0] # 걸린시간

    G1.graph[start][end] = 0        #
    G1.graph[end][start] = 0

    startYN = find( G1 , start )
    endYN = find( G1 , end )

    if startYN and endYN : # 방문 했으면
        del( newary[index] )
    else:
        G1.graph[start][end] = saveTime
        G1.graph[end][start] = saveTime
        index += 1

print( ' 춘천 --> 부산까지의 최단 거리 : '  )
Graph_print( G1 )




























