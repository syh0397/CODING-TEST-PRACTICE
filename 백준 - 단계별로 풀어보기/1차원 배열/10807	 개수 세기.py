# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
# 11
# 1 4 1 2 4 2 4 2 3 4 4
# 2
# 예제 출력 1 복사
# 3


N = int(input())
int_list = list(map(int, input().split()))
v = int(input())

cnt = int_list.count(v)
print(cnt)