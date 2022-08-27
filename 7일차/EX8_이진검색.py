# 판매제품별 판매수량의 정렬과 검색
# 이진검색


import random

def binSearch( ary , fdata ) :
    start , end = 0 , len( ary )-1
    while start<=end :
        mid = (start + end )// 2
        if fdata == ary[mid] :
            return mid
        elif fdata > ary[mid] :
            start = mid +1
        else:
            end = mid -1
    return  -1

dataAry = ['나이키' ,'아디다스' , '리북','휠라' , '뉴발란스','언더아머'] # 제품 목록
sellAry = [ random.choice( dataAry ) for _ in range(20) ] # 제품 목록에서 20개를 랜덤으로 판매목록
sellAry.sort()  # 정렬
sellproduct = list( set( sellAry ) )        # 판매목록중에 중복을 제거 # 판매된 제품 목록
sellcount = [ ] # 제품별 판매수량

# 확인차
print('제품목록 : ' , dataAry )
print('판매목록 : ' , sellAry )
print('판매된 제품목록(중복제거) : ' , sellproduct )

for p in sellproduct :                              # 판매된제품목록에서 판매제품 반복문
    count , pos = 0 , 0                             # 판매개수 , 검색위치
    while pos != -1 :                               # 검색 결과가 없을때 반복
        pos = binSearch( sellAry , p )      # 판매목록 , 제품명
        if pos != -1 :                                  # 판매목록에서 제품명을 찾았으면
            count += 1                                  # 판매 개수 증가
            del( sellAry[pos] )                     # 판매된제품목록 제거
    sellcount.append( ( p , count ) )       # 제품별 판매수량에 추가

print('제품별 판매수량 : ' , sellcount )





















