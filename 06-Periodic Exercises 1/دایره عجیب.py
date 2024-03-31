n, k = map(int, input().split())

i = 0 
is_start = True
count = 0
while True:
	if i == 0 and is_start == False:
		break;
	
	is_start = False
	i = (i + k) % n
	count += 1

print(count)
