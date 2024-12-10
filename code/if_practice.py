# #14681번 사분면 고르기
[x, y] = [input() for _ in range(2)]

if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0 :
    print(3)
elif x > 0 and y < 0 :
    print(4)
else :
    None

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