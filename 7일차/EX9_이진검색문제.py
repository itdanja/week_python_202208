"""
    문제1 : 이진검색 이용한 수 찾기
        조건1 : N개의 정수가 주어져 있을때 , 이 안에 X 라는 정수가 존재하는지 체크
        조건2 : 입력[1~100사이]
            1. 출력 첫번째 줄에 N의 자연수 입력
            2. 출력 두번째 줄에 N개의 난수 생성
            3. 출력 세번째 줄에 검색할 M 입력받기
            4. 출력 네번째 줄에 난수 목록중에 M 이 존재여부 판단 [ 1 없으면 0 ]
"""
import random

def binSearch( ary , fdata ) :
    start , end  =  0 , len(ary)-1
    while start <= end :
        mid = (start+end)//2
        if fdata == ary[mid] :
            return  1
        elif fdata > ary[mid] :
            start = mid + 1
        else:
            end = mid -1
    return 0
N = int( input() ) # 1. 출력 첫번째 줄에 N의 자연수 입력
arr = [ random.randint(1,100) for _ in range(N) ] #   2. 출력 두번째 줄에 N개의 난수 생성
arr.sort()
print( arr )
M = int( input() ) # 3. 출력 세번째 줄에 검색할 M 입력받기
print( binSearch( arr , M ) )
