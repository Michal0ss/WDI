#Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
# Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.



def podzial(n,wym="",ost=1):
    if n==0 and "+" in wym[:-1]:
        print(wym[:-1])
    else:
        for x in range(ost,n+1):
            podzial(n-x, wym+f"{x}+",x)

podzial(4)