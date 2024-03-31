cnt = 1
def hanoi(frm,to,hlp,n):
    global cnt
    if n==1:
        print(cnt,frm,to)
        cnt+=1
        return
    hanoi(frm,hlp,to,n-1)
    print(cnt,frm,to)
    cnt+=1
    hanoi(hlp,to,frm,n-1)
n = int(input())
hanoi('A','C','B',n)
