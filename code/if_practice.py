# 2480번 주사위 세개
# 같은 눈 3개 나오면 1만원 + 같은눈 X 1000원 
# 같은 눈 2개 나오면 1000원 + 같은눈 X 100원
# 모두 다른 눈이면 그중 가장 큰눈 X 100원 
A, B, C = map(int, input().split())

if A== B == C :
    print(10000+(A*1000))
elif A==B :
    print(1000+(A*100))
elif  B==C :
    print(1000+(B*100))
elif  A==C :
    print(1000+(C*100))
elif A > B and A >C :
    print(A*100)
elif B > A and B >C :
    print(B*100)
elif C > A and C >B :
    print(C*100)



# 2525번
# 자동 끝나는시간 계산
# 첫번째 줄 현재시각 (0<=A<=23, 0<=B<=59)
# 두번째 줄 필요시간 분단위 주어짐 (0<=C<=1000)
# A, B = map(int, input().split())
# C = int(input())

# # 총 분 계산
# total_minutes = B + C

# # 시(hour)와 분(minute)으로 나누기
# new_hour = (A + total_minutes // 60) % 24
# new_minute = total_minutes % 60

# # 결과 출력
# print(new_hour, new_minute)

# A, B = map(int, input().split())
# C = int(input())

# if 0 < B+C <=59 :
#     print (A, B+C)
# elif 59 < B+C <=1000:
#     if 0<= A <=23 :
#         print((A + (B+C)//60)//24, (B+C)%60)
#     elif 23 == A:
#         print ()


# if 0<= B+C <= 59 :
#     if 0 < A + (B+C//60) <= 23 and 0 == (B+C)//60 :
#         print (A, (B+C)%60)
#     elif 24 < A + (B+C//60):
#         print ((A + (B+C//60)//24), (B+C)%60)
#     elif 24 == A + (B+C//60):
#         print( 0 , (B+C)%60)

# # 2884번 알람시계
# # 45분 일찍 알람 설정하기 
# #첫째 줄 : 두 정수 H, M(0<= H <= 23, 0<= M <= 59)
# #입력시간 24시간 표현 하루 시작 0:0 끝 23:59 
# H, M = map(int, input().split())

# if 0 <= H <= 23 and 45 <= M <= 59 :
#     print (H, M-45)
# elif 1 <= H <= 23 and 0 <= M < 45 :
#     print (H-1, M+15)
# elif 0 == H and 0 <=M <45:
#     print (23, M+15)



# # #14681번 사분면 고르기
# [x, y] = [input() for _ in range(2)]

# if x > 0 and y > 0 :
#     print(1)
# elif x < 0 and y > 0 :
#     print(2)
# elif x < 0 and y < 0 :
#     print(3)
# elif x > 0 and y < 0 :
#     print(4)
# else :
#     None

# # 2753 윤년
# # 윤년이면 1, 아니면 0 
# # 윤년은 4의배수 & 100의배수가 아닐때 또는 400의 배수일때 
# # ex 1. 2012년은 4의 배수이면서 100의 배수가 아니다. 
# # ex 2. 1990년은 100의 배수이고 400의 배수가 아니다. 
# # ex 3. 2000년은 400의 배수이기 때문에 윤년이다. 
# year = int(input())

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
#     print('1')
# else :
#     print('0')

# # year = int(input())

# # if year % 4 == 0 & year % 100 != 0 :
# #     print(1)
# # elif year % 400 == 0 :
# #     print(1)
# # else :
# #     print(0)

# # year = int(input())

# # if year % 4 == 0 & year % 100 == 0 : -- 틀림
# #     print(1)
# # elif year % 4 == 0 & year % 100 != 0 :
# #     print(1)
# # elif year % 400 == 0 :
# #     print(1)
# # else :
# #     print(0)

# # 9498번
# # 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 
# # 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력
# # score = int(input())
# # if 0 <= score <= 100:

# #     if 90 <= score <= 100:
# #         print('A')
# #     elif 80 <= score < 90:
# #         print('B')
# #     elif 70 <= score < 80:
# #         print('C')
# #     elif 60 <= score < 70:
# #         print('D')
# #     else:
# #         print('F')
# # else :
# #     None

# #1330번
# # 첫째 줄에 다음 세 가지 중 하나를 출력한다.

# # A가 B보다 큰 경우에는 '>'를 출력한다.
# # A가 B보다 작은 경우에는 '<'를 출력한다.
# # A와 B가 같은 경우에는 '=='를 출력한다.