import random


def init():
    itemlist =[]
    for i in range(2):
        itemlist.append([len(itemlist),"Schwert",2])
        itemlist.append([len(itemlist),"Bogen",2])
        itemlist.append([len(itemlist),"Schield",2])
        itemlist.append([len(itemlist),"Zauberbarriere",2])
        itemlist.append([len(itemlist),"Flinktrank",2])
        itemlist.append([len(itemlist),"Gürteltasche",2])
        itemlist.append([len(itemlist),"Schriftrolle",2])
        itemlist.append([len(itemlist),"Romanze",2])
        itemlist.append([len(itemlist),"Malset",2])
        itemlist.append([len(itemlist),"Burbon",2])

    ruestungslist1 = []
    words = ["S Kopfschutz","S Ruestung", "S Handschuhe","S Stiefel",
                    "A Kopfschutz","A Ruestung","A Handschuhe", "A Stiefel",
                    "B Kopfschutz","B Ruestung","B Handschuhe", "B Stiefel",
                    "C Kopfschutz","C Ruestung","C Handschuhe", "C Stiefel",
                    "D Kopfschutz","D Ruestung","D Handschuhe", "D Stiefel",
                    "E Kopfschutz","E Ruestung","E Handschuhe", "E Stiefel"]

    #erstelle 72 Ruestungsobjekte: 24*3 = 72 gleichverteilt
    for i in range(3):
        for e in range(len(words)):
            ruestungslist1.append([len(ruestungslist1),words[i],0,0,0,0,0,0,0,0])


    # erstelle weitere 72 Ruestungsobjekte, zuf�lligverteilt

    for i in range(72):
        ruestungslist1.append([len(ruestungslist1),random.randint(0,len(words)),0,0,0,0,0,0,0])

    for i in range(len(ruestungslist1)):
        for e in range( len(ruestungslist1[i])):
            print(ruestungslist1[e],' ')
        print()    

    for i in range(len(ruestungslist1)):
        doStats(ruestungslist1[i])
    
    
    for i in range(len(ruestungslist1)):
        for e in range( len(ruestungslist1[i])):
            print(ruestungslist1[e],' ')
        print()    
    






def doStats(ruestung):
    zzahl =0
    if ruestung[1][0] == 'S':
        zzahl = 6
    elif ruestung[1][0] == 'A':
        zzahl = 5
    elif ruestung[1][0] == 'B':
        zzahl = 4
    elif ruestung[1][0] == 'C':
        zzahl = 3
    elif ruestung[1][0] == 'D':
        zzahl = 2
    elif ruestung[1][0] == 'E':
        zzahl = 1
    givestat(ruestung,zzahl)
    return

def givestat(ruestung, zahl):
    randzahl = 0
    if zahl<4:
        randzahl = random.randint(1,6)
        if randzahl ==1:
            ruestung[2]=zahl
        elif randzahl ==2:
            ruestung[3]=zahl
        elif randzahl ==3:
            ruestung[4]=zahl
        elif randzahl ==4:
            ruestung[5]=zahl
        elif randzahl ==5:
            ruestung[6]=zahl
        elif randzahl ==6:
            ruestung[7]=zahl
    else:
        randzahl = random.randint(1,4)    
        if randzahl == 1:
            ruestung[2]=zahl
        if randzahl == 2:
            ruestung[3]=zahl
        if randzahl == 3:
            ruestung[4]=zahl
        if randzahl == 4:
            ruestung[5]=zahl    

init()