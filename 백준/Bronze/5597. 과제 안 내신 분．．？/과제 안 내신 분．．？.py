n = list(range(1,31))
for _ in range(28):
  x = int(input())
  if x in n:
    n.remove(x)

for i in n:
  print(i)