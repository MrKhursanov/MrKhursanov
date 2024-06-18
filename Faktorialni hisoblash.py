n=int(input('Sizga necha faktorial son kerak?'))
jami=1
for i in range(n):
    s=n-i
    if s!=1:
        jami=jami*s
    else:
        break
print(jami)
