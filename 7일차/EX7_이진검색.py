"""
    이진검색 [ 도서 : 도서명 , 저자 ]
"""
from operator import itemgetter     # import 함수 가져오기 [ itemgetter ]

bookAry = [
        ['어린왕자' ,'쌩덱쥐베리'] , ['이방인','까뮈'] , ['부활' , '톨스토이'] ,
        ['신곡' , '단테'] ,  ['돈키호테' , '세르반테스'] , ['동물농장','조오웰'] ,
        ['데미안' , '헤르만헤세'] , [ '파우스트','괴테'] , ['대지','펄벅']
    ]

def bookSearch( ary , fdata , cnum ) :
    pos = -1
    start , end = 0 , len( ary )-1
    while start <= end :
        mid = ( start + end ) // 2
        if fdata == ary[mid][cnum] :
            return ary[mid][cnum]
        elif fdata > ary[mid][cnum] :
            start = mid + 1
        else:
            end = end - 1
    return pos

while True :
    btn =  int( input('검색 카테고리 : 1.책이름 2.저자명 입력 : ') )
    fdata = ''
    pos = -1
    if btn == 1 :
        fdata = input('안내) 도서명 입력 : ')
        bookOrder = sorted( bookAry , key=itemgetter(0) )
                        # sorted( 배열 , key=itemgetter(인덱스) ) : 해당 인덱스 기준으로 정렬
        pos = bookSearch( bookOrder , fdata , 0 )

    elif btn == 2 :
        fdata = input('안내) 저자명 입력 : ')
        bookOrder = sorted(bookAry, key=itemgetter(1))
        pos = bookSearch(bookOrder, fdata, 1 )

    else :
        print('안내) 알수 없는 번호 입니다. ')
    # 결과 출력 
    if pos == -1 :
        print('안내) 검색 데이터가 없습니다. ')
    else :
        print('안내) 검색 도서는 : ' , pos , '  존재합니다. ')

