from tkinter import * #year_num=5779 year_in_machsor=1-19

root=Tk()
root.geometry('450x300')

def mol(lst,num):
    for i in range(len(lst)):
        lst[i]=lst[i]*num
    return lst

def add(year_num,machsorim):
    for i in range(4):
        year_num[i]=year_num[i]+machsorim[i]
    return year_num

def take7(lst):
    lst[3],lst[2]=lst[3]%18,lst[2]+lst[3]//18
    lst[2],lst[1]=lst[2]%60,lst[1]+lst[2]//60
    lst[1],lst[0]=lst[1]%24,lst[0]+lst[1]//24
    lst[0]=lst[0]%7
    if lst[0]==0:
        lst[0]=7
    return lst

def chal (lst):     
    sm=lst[3]
    sm+=lst[0]*25920
    sm+=lst[1]*1080
    sm+=lst[2]*18
    return sm

def RH(molod):
    global jj
    tt=chal(molod)
    if year_in_machsor==3 or year_in_machsor==6 or year_in_machsor==8 \
    or year_in_machsor==11 or year_in_machsor==14 or year_in_machsor==17 or year_in_machsor==19:
        jj=3
    elif year_in_machsor==4 or year_in_machsor==7 or year_in_machsor==9 \
    or year_in_machsor==12 or year_in_machsor==15 or year_in_machsor==18 or year_in_machsor==1:
        jj=1
    elif year_in_machsor==2 or year_in_machsor==5 or year_in_machsor==10 \
    or year_in_machsor==13 or year_in_machsor==16:
        jj=2    
    if tt < chal([2,15,0,589]):
        return 2
    elif tt < chal([2,18,0,0]): 
        if jj==2 or jj==3:
            return 2
        elif jj==1:
            return 3
    elif tt < chal([3,9,0,204]):
        return 3                    
    elif tt <chal([3,18,0,0]): 
        if jj==2 or jj==1:
            return 5
        elif jj==3:
            return 3               
    elif tt < chal([5,18,0,0]):
        return 5
    elif tt < chal([7,18,0,0]):
        return 7
    elif tt < chal([8,0,0,0]):
        return 2
    
def yearmolod (year_num):
    global year_in_machsor
    machsorim=year_num//19   
    year_in_machsor=year_num%19
    if year_in_machsor==0:
        year_in_machsor=19
        machsorim-=1   
    return take7(add(add([2,5,0,204],mol([2,16,0,595],machsorim)),mol([1,12,44,1],int((year_in_machsor-1)*12.368+.09))))

def chart(num):
    for i in range(19):
        for j in range(13):
            print(num+j*-19+i,'=',RH(yearmolod (num+j*-19+i)),end=' ')
        print(num+13*-19+i,'=',RH(yearmolod (num+13*-19+i)),)

def oneday ():
    global pp
    print(ll[i],'=',vv[mm[0]+10],vv[uu],str(mm[1])+':'+str(mm[2]),vv[9],mm[3],vv[ww],' ',vv[xx],'=',vv[pp],vv[8])
    year_numa= Label(root, text=vv[pp])
    year_numa.place(width=35,height=20,x=0,y=i*20+10)
    bbb= Label(root, text=vv[xx])
    bbb.place(width=35,height=20,x=35,y=i*20+10)
    ccc= Label(root, text=(vv[9],mm[3],vv[ww]))
    ccc.place(width=75,height=20,x=125,y=i*20+10)
    ddd= Label(root, text=(str(mm[1])+':'+str(mm[2])))
    ddd.place(width=50,height=20,x=200,y=i*20+10)
    eee= Label(root, text=(vv[mm[0]+10],vv[uu]))
    eee.place(width=125,height=20,x=250,y=i*20+10)
    fff= Label(root, text=(vv[8],ll[i]))
    fff.place(width=75,height=20,x=375,y=i*20+10)
    pp=(pp+1)%7
    
def twoday ():
    global pp
    print(ll[i],'=',vv[mm[0]+10],vv[uu],str(mm[1])+':'+str(mm[2]),vv[9],mm[3],vv[ww],' ',vv[xx],'=',vv[pp],vv[pp+1],vv[8])
    year_numa= Label(root, text=(vv[pp],vv[pp+1]))
    year_numa.place(width=35,height=20,x=0,y=i*20+10)
    bbb= Label(root, text=vv[xx])
    bbb.place(width=35,height=20,x=35,y=i*20+10)
    ccc= Label(root, text=(vv[9],mm[3],vv[ww]))
    ccc.place(width=75,height=20,x=125,y=i*20+10)
    ddd= Label(root, text=(str(mm[1])+':'+str(mm[2])))
    ddd.place(width=50,height=20,x=200,y=i*20+10)
    eee= Label(root, text=(vv[mm[0]+10],vv[uu]))
    eee.place(width=125,height=20,x=250,y=i*20+10)
    fff= Label(root, text=(vv[8],ll[i]))
    fff.place(width=75,height=20,x=375,y=i*20+10)
    pp=(pp+2)%7
    
year_num=int(input('year? '))
print(year_num)

hh=['תשרי','חשון','כסלו','טבת','שבט','אדר','ניסן','אייר','סיון','תמוז','אב','אלול','תשרי']
kk=['תשרי','חשון','כסלו','טבת','שבט','אדר א','אדר ב','ניסן','אייר','סיון','תמוז','אב','אלול','תשרי']

qq=RH(yearmolod (year_num+1))
pp=RH(yearmolod (year_num))

qq+=7
rr=(qq-pp)%7

if jj==1 or jj==2:
    rr-=3
    ll=hh
elif jj==3:
    rr-=5
    ll=kk
rr%=7    

vv=['שבת','א','ב','ג','ד','ה','ו','שבת','מולד','מיט','שבת','זונטאג','מאנטאג','דינסטאג','מיטוואך','דאנערשטאג'
    ,'פרייטאג','שבת','ביינאכט','פארטאגס','צופרי','מיטאג','נאכמיטאג','מוצאי','שבת','ר"ח','חלק','ר"ה','חלקים']

for i in range(len(ll)):
    mm=mol([1,12,44,1],i)
    mm=add(mm,yearmolod (year_num))
    mm=take7(mm)
    
    if mm[1]==0:
        mm[0]-=1
        uu=22
    elif mm[1]<9:
        if mm[0]==1:
            mm[0]=13
            uu=24
        else:
            mm[0]-=1
            uu=18
    elif mm[1]<12:
        uu=19
    elif mm[1]<18:
        uu=20
    elif mm[1]==18:
        uu=21
    elif mm[1]<24:
        uu=22
        
    mm[1]+=6
    mm[1]%=12
    if mm[1]==0:
        mm[1]=12
    if mm[3]==1:
        ww=26
    else:
        ww=28
    if ll[i]=='תשרי':
        xx=27
    else:
        xx=25
    if mm[2]<10:
        mm[2]='0'+str(mm[2])
        
    pp%=7   
    if i ==0 or i==4:
        oneday ()
    elif i==1 or i==5:
        twoday ()
    elif i==2:
        if rr==2:
            twoday ()
        elif rr==1 or rr==0:
            oneday ()
    elif i==3:
        if rr==1 or rr==2:
            twoday ()
        elif rr==0:
            oneday ()
    elif i==6 or i==8 or i==10 or i==12:
        if len(ll)==14:
            twoday ()
        elif len(ll)==13:
            oneday ()
    elif i==7 or i==9 or i==11 or i==13:
        if len(ll)==14:
            oneday ()
        elif len(ll)==13:       
            twoday ()
            
#chart(5834)


            
root.mainloop()
