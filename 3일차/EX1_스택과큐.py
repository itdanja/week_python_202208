"""
    자료구조  : 데이터를 효율적으로 저장하는 방법
        1. 선형리스트 2.연결리스트
        3. 스택 4.큐
        * 상황에 따라 선택해서 사용
    알고리즘  : 코드가 실행되는 순서도
    1.  스택 [ stack ] : Last in Frist Out  [ LIFO ]
        예) 1.동전케이스 2.ctrl+z(뒤로가기) 3.프링글스  등등
        1. 먼저 들어간 데이터는 가장 나중에 나온다. [ 입구와 출구가 동일하다 ]
        2. 용어
                1. PUSH : 데이터 추가
                2. POP : 데이터 추출
                3. TOP :  현재 마지막 데이터의 위치[인덱스] / 가장 위에 있는 데이터
        3. 배열[리스트] 이용한 구현


  ------------   push 2번 했을떄

   input            output
             입/출구
        |               |
        |               |
        |   '신동엽' |        top = 1       +1
        |  '유재석'  |        top = 0       +1
        |_______ |        top = -1       [ 데이터 1개도 없다 ]

  ------------   pop 1번 했을떄

     input            output
             입/출구
        |               |
        |               |
        |               |        top = 1        -1          -> top =0
        |  '유재석'  |        top = 0
        |_______ |        top = -1      [ 데이터 1개도 없다 ]


    2.  큐 [ Queue ] : Frist in Frist Out    [ FIFO ]
        예 ) 대기 프로그램 , 지하철 , 카페주문 등등
        1. 먼저 들어온 데이터는 가장 먼저 나온다 [ 입구와 출구 별도로 존재 ]
        2. 용어
            1. enqueue  : 데이터 추가
            2. dequeue  : 데이터 추출
            3. rear         : 데이터 추가되는 위치[인덱스]
            4. front        : 데이터 추출되는 위치[ 인덱스
                ------------------------
                  rear                                     front
input                 data2            data1            output
   입구      ------------------------         출구
enqueue                                                     dequeue


    ------------ 유재석 추가 했을때 ----------------
    rear = -1       front = -1
        +1
    --------------------------
                                        rear
                                        유재석
                                                        front
    --------------------------
    ------------ 강호동  추가 했을때 ----------------
    rear = 0       front = -1
        +1
    --------------------------
                   rear
                  강호동               유재석
                                                        front
    --------------------------
------------  삭제  했을때 ----------------
    rear = 1       front = -1
                                +1
    --------------------------
                   rear
                  강호동               유재석
                                           front
    --------------------------

"""