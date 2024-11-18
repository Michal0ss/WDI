def komb(s,k):
    if k==1:
        for x in s: yield x
    elif len(s) == k:
        yield s
    else:
        for x in komb(s[1:],k): yield x
        for x in komb(s[1:], k-1): yield s[0]+x

for a in komb('ABCDE',3):
    print(a)