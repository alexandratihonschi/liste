with open('input.txt', 'r') as f:
    x=list(eval(f.readline()))

a = x
y=sorted(x)
x.sort(reverse=True)
len = len(x)
min = min(x)
max = max(x)
x.extend([111])
x[1]=222

with open('lista.txt', 'w') as f1:
    for chars in y:
        f1.write(f'{str(chars)} , ')


