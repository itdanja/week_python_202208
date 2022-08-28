"""
    동적 계획법[ DP : 다이나믹 프로그래밍 ]
        - 큰 문제를 작은 문제로 쪼개서 저장 하면서 풀이 과정 [ 저장하면서 풀기]
        - 재귀 : 동일한 반복이 비효율적인 계산 발생 가능성이 나타남..\
        효율적으로 문제 해결 가능

        - 특정한 경우에 알고리즘X -> 정해진 규칙/문법X
        1. DP로 풀 수 있는 문제 확인
        2. 문제의 변수 확인
        3. 변수들의 관계 확인
        4. 기록[메모]       : 메모이제이션
        5. 구현

"""
# 예) 피보나치 수열 [ 재귀 vs DP ]
    # 피보나치 수열 : 앞 두항의 더한 값이 현재 항의 값을 갖는다.
    # 1 1 2 3 5

# 동적 계획법 으로 피보나치 구현
def dp_fibo( n ) :
    global count_dp
    memo = [ 1 , 1 ]        # 계산된 수열 저장 하는 공간 ( 저장[기억] 하면서 풀기 )
    if n<2 :
        return memo[n]
    else:
        for i in range( 2 , n+1 ) :
            memo.append(   memo[i-2] + memo[i-1] )      # 메모리에 두 항을 더한 값을 추가한다.
            count_dp += 1
        return memo[n]

# 재귀함수 로 피보나치 구현
def requ_fibo( n ) :
    global count_requ
    count_requ += 1         # 함수가 실행 될때마다 1씩 증가
    if n<2 :
        return  1
    else:
        return requ_fibo( n-2 ) + requ_fibo( n-1) # 앞 두항의 더한 값

count_requ = 0  # 재귀방식 피보나치 반복횟수
count_dp = 0       # dp방식 피보나치 반복횟수

print( '재귀를 이용한 피보나치 수열 : ' , requ_fibo( 30 ) , '  반복수 : ' , count_requ  )
print( 'DP를 이용한 피보나치 수열 : ' , dp_fibo( 30 )  , ' 반복수 : ' , count_dp  )


