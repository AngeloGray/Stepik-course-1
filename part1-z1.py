# В данной задаче требуется вычислить сумму двух входных целых чисел, лежащих в отрезке от нуля до десяти.
import sys
# способ 1
a, b = sys.stdin.readline().split()
print(int(a) + int(b))
# способ 2
a = input()
b = input()
print(int(a) + int(b))
# способ 3
print(sum(map(int, input().split())))
