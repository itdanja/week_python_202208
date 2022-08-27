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

for p in sellproduct :
    count , pos = 0 , 0
    while pos != -1 :
        pos = binSearch( sellAry , p )
        if pos != -1 :
            count += 1
            del( sellAry[pos] )
    sellcount.append( ( p , count ) )

print('제품별 판매수량 : ' , sellcount )





















