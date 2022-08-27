"""

    문제2
        1. 설명
            수학 포기한 학생들이 시험 보는데 1번부터 마지막 문제까지 답을 찍는다.

            예)
            유재석 : 1 2 3 4 5 1 2 3 4 5 ~~~       모든 문제를 찍는다 -> 난수 생성
            강호동 : 2 1 2 3 2 4 2 5 2 1 ~~~       모든 문제를 찍는다 -> 난수 생성
            신동엽 : 3 3 1 1 1 2 2 4 4 5 ~~~       모든 문제를 찍는다 -> 난수 생성

            1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열이 있을때

            가장 많은 문제를 맞힌 사람 결과 찾기

        2. 조건
            - 시험은 최대 10,000 문제가 있음
            - 정답은 선택지는 1~5 중 하나
            - 정답지는 문제 개수 만큼 난수로 생성
            예)
                정답지 = [ 1 , 2, 3 , 4 , 5 ]
"""
import random

def solution( answerlist ) :
    counter = [ 0 , 0 , 0 ]         # 학생들 맞힌 개수를 저장하는 배열[리스트]
    size = len(answerlist)      # 문제 개수
    for i in range( size ) :        # 문제 개수만큼 반복
        if answerlist[i] == s1[i] :     # 만약에 정답지의 i번째 정답 과 s1의 i번째 답안 과 같으면
            counter[0] += 1                 # s1 정답개수 증가
        if answerlist[i] == s2[i] :     #만약에 정답지의 i번째 정답 과  s2의 i번째 답안 과 같으면
            counter[1] += 1                     # s2 정답개수 증가
        if answerlist[i] == s3[i] :     #만약에 정답지의 i번째 정답 과 s3의 i번째 답안 과 같으면
            counter[2] += 1                     # s3 정갑개수 증가
    print(' 채점 결과 : ' , counter )
    # 1등찾기
    best = max( counter )       # 가장 많이 맞춘 수
    result = [ ] # 1등 목록
    for i in range( 3 ) :
        if counter[i] == best :     # i번째 학생의 맞춘 개수와 가장 많이 맞춘 수 같으면
            result.append( i+1 )        # 1등에 추가
    return result

answerlist = [ random.randint(1,5) for _ in range(10) ] # 1. 정답지
s1 = [ random.randint(1,5) for _ in range(10) ] # 첫번재 학생이 제출한 답안지
s2 = [ random.randint(1,5)for _ in range(10) ] # 두번째 학생이 제출한 답안지
s3 = [ random.randint(1,5) for _ in range(10) ] # 세번째 학생이 제출한 답안지

print('시험 정답지 : ' , answerlist )
print('1번 학생이 찍은 답안지 : ' , s1 )
print('2번 학생이 찍은 답안지 : ' , s2 )
print('3번 학생이 찍은 답안지 : ' , s3 )
print('1등 ' , solution( answerlist ) , '번 학생 ')
















