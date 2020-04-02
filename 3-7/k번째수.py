N = int(input())
k = int(input())

B = []

i = 1
j = 1

for idx in range(N * N):
	B.append(i * j)
	j += 1
	if j > N:
		j = 1
		i += 1

B.sort()

print(B[k])
