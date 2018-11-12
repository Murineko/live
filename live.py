import random
a=int(input("введите количество поколенией: "))
counter=1
home=[]
present=[]
future=[]
w=0
buf=[]
wer=0
dead=0
#описание дома
with open('home.micro.txt', 'r') as file:
    home = file.readlines()
del home[0]
home = [[n for n in x.split()] for x in home]
bufer=[]
for i in range(23):
    bufer.append([])
    for j in range(23):
        bufer[i]. append(0)
for i in range(1,22):
    for j in range(1,22):
        bufer[i][j]=home[i-1][j-1]
#описание настоящего
for i in range(23):
    present.append([])
    for j in range(23):
        if (i!=0 and j!=0 and j!=22 and i!=22):
            if bufer[i][j]=='0':
                present[i].append(0)
            if bufer[i][j]=='X':
                present[i].append(1)
        else:
            present[i].append(0) 
for k in present:
    print ("настоящее", k)
    
f = open('work.out.txt', 'w')
f.close()
# отсчет поколений
while counter<=a:
    f = open('work.out.txt', 'a')
    print ("поколение ", counter)
    f.write('\n'+ "поколение", )
    f.write(str(counter) + '\n')
    #заполняем будущее
    for i in range(23):
        future.append([])
        for j in range(23):
            if (i!=0 and j!=0 and j!=22 and i!=22):
                if present[i][j]==12:
                    future[i].append(0)
                if 0<=present[i][j]<=11:
                    w=0
                    kill=0
                    if (present[i-1][j]!=0 and present[i-1][j]!=-1) : # без учета диагоналей
                        w+=1
                    if (present[i][j-1]!=0 and present[i][j-1]!=-1):
                        w+=1
                    if (present[i-1][j-1]!=0 and present[i-1][j-1]!=-1):
                        w+=1
                    if (present[i+1][j+1]!=0 and present[i+1][j+1]!=-1):
                        w+=1
                    if w<2:
                        future[i].append(0)
                    if w>=2:
                        if present[i][j]==11:
                            future[i].append(12)
                        if present[i][j]==10:
                            future[i].append(11)
                        if present[i][j]==9:
                            future[i].append(10)
                        if present[i][j]==8:
                            future[i].append(9)
                        if present[i][j]==7:
                            future[i].append(8)
                        if present[i][j]==6:
                            future[i].append(7)
                        if present[i][j]==5:
                            future[i].append(6)
                        if present[i][j]==4:
                            future[i].append(5)
                        if present[i][j]==3:
                            future[i].append(4)
                        if present[i][j]==2:
                            future[i].append(3)
                        if present[i][j]==1:
                            future[i].append(2)
                        if present[i][j]==0:
                            future[i].append(1)
            else:
                future[i].append(0)
                
    print ("будущее поколение: ")
    f.write('\n')
    buf=[]
    buf=future
    for i in range (1,22):
        for j in range(1,22):
            print(buf[i][j]," ", end= '') #записать в файл
            f.write(str(buf[i][j]))
            f.write(" ")
        print () #записать в файл
        f.write(''+ '\n')
    dead=0
    for i in range(23):
        for j in range(23):
            if future[i][j]==0 or future[i][j]==-1:
                dead+=1

    print ("мертвы", dead)
    if dead==(23)*(23):
        print ("все умерли *играет грустная музыка*")
        f.write("все умерли *играет грустная музыка* ")
        counter=100
        break
    #будущее становится настоящим
    present=future
    future=[]
    counter+=1
f.close()
                        
                     
