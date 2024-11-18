def gen(n):
    if n==0:
        yield ""
    else:
        for c in gen(n-1):
            yield '0'+c+'0'  # generuje palindromy w sys binarnym
            yield '1'+c+'1'

for s in gen(4):
    print(s)