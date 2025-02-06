#25314 코딩은 체육과목입니닼
# long int = 4 byte, long long int = 8 byte 
# long * n = 4 * n byte

N = int(input())
a = N//4

# for i in range(1, (N/4)+1) :
#     i =+i
#     print ("long")


# # 25304 영수증
# X = int(input())
# N = int(input())
# list = []
# for i in range(1, N+1) :
#     a, b = map(int, input().split())
#     list.append(a * b)
#     i +=i
# if X == sum(list) :
#     print('Yes')
# else : print('No')





# ## 8393 합 n이 주어졌을 때, 1부터 n 까지 합을 구함 
# n = int(input())
# print(sum(range(1, n + 1)))


# n = int(input())
# for i in range(1, n+1):
#     print(sum(range(1, n+1)))


# ## 10950번 A+B (gpt 해결)
# # 입력 받을 테스트 케이스 수
# T = int(input())  # 첫 줄에 테스트 케이스 수를 입력받음

# # 테스트 케이스 처리
# for _ in range(T):
#     A, B = map(int, input().split())  # 각 줄마다 두 정수를 입력받음
#     print(A + B)  # A와 B의 합을 출력


# A, B = map(int(input().split))

# for a in A :
#     for b in B:
#         print (A + B)

# ## 2739번 구구단 
# n = int(input())

# multiple = [1,2,3,4,5,6,7,8,9]

# for i in multiple :
#     print(f"{n} * {i} =", n * i)