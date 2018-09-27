from random import choice
import sys
def init(alist):#will change the oldlist
    for a in range(0, 4):
        for b in range(0, 4):
            alist[a][b] = 0
    return alist
def main():
    oldlist=[[0,0,0,0], [0,2,2,2], [4,2,2,2], [4,4,4,4]]
    #newlist=oldlist
    newlist=init(oldlist)
    new2=getzero(oldlist)
    flag=False
    if len(new2)==0:
        print('gameover')
    while len(new2)!=0:
        new2 = getzero(newlist)
        if len(new2)==1:
            newlist[new2[0][0]][new2[0][1]]=2
        elif len(new2)==0:
            print('gameover')
            break
        else:
            tlist=getrandom(new2)
            for (c,d) in tlist:#random结果可能为一个
                newlist[c][d]=2
        draw(newlist)
        xx=getinput()#get user input "w a s d"
        if xx=='a':
            newlist=moveleft(newlist)
            #draw(newlist)
def gameover(alist):
    pass
def getinput():
    print('Please enter Up(w),Down(s),Left(a),Right(d)')
    action=input()
    return action
def getrandom(alist):
    ranlist=[]
    zeronum=len(alist)
    if zeronum==1:
        return alist[0]
    else:
        for x in range(2):
            ranlist.append(choice(alist))
        return ranlist
def draw(alist):
    for a in range(0,4):
        for b in range(0,4):
            print(alist[a][b],' ',end=' ')#print 默认是换行结尾so use end=‘
        print('\n')
def getzero(alist):
    zerolist=[]
    for a in range(0,4):
        for b in range(0,4):
            if alist[a][b]==0:
                zerolist.append([a, b])#返回非零的行列号
    return zerolist
def moveleft(alist):
    flag=False
    for a in range(0,4):#[0,4)
        if flag:
            break
        for b in range(3,0,-1):#[3,0) attension
            if alist[a][b]==alist[a][b-1]!=0:
                alist[a][b]=0
                alist[a][b-1]*=2
                if alist[a][b-1]==16:
                    flag=True
                    break#out of one "for"
                alist = moveleft(alist)
            if alist[a][b-1]==0 and alist[a][b]!=0:
                alist[a][b-1],alist[a][b]=alist[a][b],0
    while flag:#该语句不放在for循环里，好最后一行时a=3此时不再执行for
        draw(alist)
        print('win do u want to play again(Y/N)')
        ans = input()
        if ans == 'y':
            flag = False
            init(alist)
            break
        elif ans == 'n':
            sys.exit()
        else:
            continue
    return alist
def moveright():
    pass
def movedown():
    pass
def moveup():
    pass
if __name__=='__main__':
    main()