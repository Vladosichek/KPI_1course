def control(line):
    d=1
    i=0
    while(i<len(line)):
        if line[i]==chr(19):
            d=0
        i+=1
    return d

def put(name):
    des=1
    flag=0
    line=""
    text=open(name, "w")
    while(des==1):
        text.write(line)
        if flag:
             text.write('\n')
        line=input()
        des=control(line)
        flag=1
    i=0
    while(i<len(line)):
        if line[i]==chr(19):
            line=line[:i:]
        i+=1
    text.write(line)
    text.close()

def add(name,  sym):
    if sym=='Y':
        print("   Add to file 1:")
        des=1
        line=""
        text=open(name, "a")
        while(des==1):
            text.write(line)
            text.write('\n')
            line=input()
            des=control(line)
        i=0
        while(i<len(line)):
            if line[i]==chr(19):
                line=line[:i:]
            i+=1
        text.write(line)
        text.close()

def out(name):
    text=open(name, "r")
    for i in text.readlines():
        print(i, end="")
    print("\n")
    text.close()

def fil(name_old, name, a_s1):
    a_s=int(a_s1)
    text_old=open(name_old, "r")
    text=open(name, "w")
    flag=0
    for i in text_old.readlines():
        if flag:
            text.write('\n')
        words=i.split()
        spa=0
        length=0
        for j in words:
            length+=len(j)
            spa+=1
        spa-=1
        ammgen=0
        ammadd=0
        if spa==-1:
            ammgen=a_s
        elif spa==0:
            ammgen=a_s-length
        else:
            total=a_s-spa-length
            if(total<=0):
                ammgen=1
            else:
                ammgen=(a_s-length)//spa
                ammadd=(a_s-length)%spa
        if spa==-1:
            for h in range(ammgen):
                text.write(' ')
        elif spa==0:
            for h in range(ammgen):
                text.write(' ')
            text.write(words[0])
        else:
            text.write(words[0])
            for h in range(1, spa+1):
                for p in range(ammgen):
                    text.write(' ')
                if ammadd:
                    text.write(' ')
                    ammadd-=1
                text.write(words[h])
        flag=1
    text_old.close()
    text.close()