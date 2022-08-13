"""
# 지하철 관제 프로그램 [ QUEUE ]
조건
	1.노선 : 차고지 -> 강남역 ->역삼역 -> 선릉역 -> 삼성역 -> 차고지		[ 2차원 리스트 ]
	2.처음에 차고지 차량대기 : 전차A , 전차B , 전차C
	3. 출발 신호 메뉴 :
		0 . 차고지  1.강남역 2. 역삼역 3.선릉역 4.삼성역

	4. 출력예시)	0 1 0 2 를 순차적으로 입력했을때
			차고지 : 전차A ,전차B ,전차C  강남역: 		역삼역:  			선릉역: 		삼성역:
		0	차고지 : 전차B , 전차C 	강남역: 전차A  	역삼역:  			선릉역: 		삼성역:
		1	차고지 : 전차B , 전차C 	강남역: 	  	역삼역: 전차A 		선릉역: 		삼성역:
		0	차고지 : 전차C 		강남역: 전차B 	역삼역: 전차A 		선릉역: 		삼성역:
		2	차고지 : 전차C 		강남역: 전차B 	역삼역:  			선릉역: 전차A 	삼성역:

"""
# 1. 데이터 추가  함수
def enQueue() :
    return
# 2. 데이터 삭제 함수
def deQueue( stationNo ) :
    front = -1      # 출구 인덱스
    rear = -1       # 입구 인덱스
    # 해당 역의 입구 인덱스 찾기
    for i in 호선2[stationNo] :
        if i !=None :   # 만약에 None 아니면[전자존재]
            rear += 1       # 입구의 인덱스 +1 증가
    # 가장 앞에 있는 데이터 추출
    front += 1
    train =  호선2[ stationNo ][front]   # 출발한 전차 이름 추출
    호선2[stationNo][front] = None    # 해당 위치에 전차 제거
    # 제거후 뒤로 한칸씩 당기기
    for i in range( front+1 , rear+1 ) :
        호선2[stationNo][i-1] = 호선2[stationNo] [i]
        호선2[stationNo][i] = None
    return
# 3. 큐 상태 함수 [ # 현재 전차들의 위치 출력  ]
def printQueue( ) :
    for i in  range( 0 , len(호선2) , 1 ) :
        print( 호선2[i] )
    return

# 0. 필요한 변수들  [ 역 마다 리스트 선언 -> 2차원 리스트 ]
차고지 = [ '전차A' , '전차B' , '전차C']
강남역 = [ None , None , None ]
역삼역 = [ None , None , None ]
선릉역 = [ None , None , None ]
삼성역 = [ None , None , None ]
호선2 = [ 차고지,강남역,역삼역,선릉역,삼성역]    # 리스트안에 5개 리스트 넣어주기 -> 2차원 리스트

while True :
    printQueue()   # 현재 전차들의 위치 출력
    select = int( input( '출발신호 : 0.차고지 1.강남역 2.역삼역 3.선릉역 4.삼성역 ' ) )
    if select == 0 :
        print('안내) 차고지 에서 전차 출발합니다. ')
        deQueue( select )
    elif select == 1 :
        print('안내) 강남역 에서 전차 출발합니다. ')
        deQueue(select)
    elif select == 2 :
        print('안내) 역삼역 에서 전차 출발합니다. ')
        deQueue(select)
    elif select == 3 :
        print('안내) 선릉역 에서 전차 출발합니다. ')
        deQueue(select)
    elif select == 4 :
        print('안내) 삼성역 에서 전차 출발합니다. ')
        deQueue(select)
    else:
        print('안내) 알수 없는 번호입니다. ')























