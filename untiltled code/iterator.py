import re
import itertools
inchar="send + more == money"
def solve(putin):
    word=re.findall('[A-Z]+',putin.upper())#i love u xue
    words=set(''.join(word))#i,l,o,v,e,u,xC^^C
    assert len(words)<=10,'More than 10 letters'
    cwords=tuple(ord(c) for c in words)
    cint=tuple(ord(c) for c in '0123456789')
    aint=itertools.permutations(cint,len(cwords))
    for guess in aint:
        sign=0
        bputin=putin.upper()
        resolution=bputin.translate(dict(zip(cwords,guess)))
        newres=re.findall('[0-9]+',resolution)
        for c in newres:
            if c[0][:1] is '0':# the first num can not 0
                sign=1
        if sign==0:
            if eval(resolution):
                return resolution
    return('none')
if __name__=='__main__':
    import sys
    resolution=solve(inchar)
    if resolution:
        print(resolution)
    print(inchar)




