def perm(s):
    "funkcja generuje permutacje liter w napisie s"
    if len(s)==1:
        yield s
    else:
        for p in perm(s[:-1]):
            for i in range(len(s)):
                yield p[:i]+s[-1]+p[i:]

for a in perm("MICHAL"):
    print(a)