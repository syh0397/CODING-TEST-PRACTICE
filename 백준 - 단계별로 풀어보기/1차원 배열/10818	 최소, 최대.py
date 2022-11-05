# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
N_list = list(map(int, input().split()))


a = min(N_list)
x = max(N_list)

print(a,x, sep = ' ')