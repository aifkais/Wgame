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
    for i in range(len(words)):
        for e in range(3):
            ruestungslist1.append([len(ruestungslist1),words[i],0,0,0,0,0,0,0,0])


    # erstelle weitere 72 Ruestungsobjekte, zuf�lligverteilt

    for i in range(72):
        ruestungslist1.append([len(ruestungslist1),words[random.randint(0,len(words)-1)],0,0,0,0,0,0,0])
    
    for i in range(len(ruestungslist1)):
        print(ruestungslist1[i])
        print()    
    
    for i in range(len(ruestungslist1)):
        doStats(ruestungslist1[i])
        
    

    for i in range(len(ruestungslist1)):
         print(ruestungslist1[i])
         print() 
  
    print()
    ruestungslist1=sortlist(ruestungslist1)
    for i in range(len(ruestungslist1)):
         print(ruestungslist1[i])
         print() 
  
    #erstelle Charakter
    
    char1 = [1,'Fav',50,50,5,10,5,10]
    char2 = [1,'Udog',50,50,5,10,5,10]
    fight(char1,char2)
        
       
def sortlist(items):
    # Die Tier-Reihenfolge, von der höchsten (S) bis zur niedrigsten (E)
    tiers = {'S': 5, 'A': 4, 'B': 3, 'C': 3, 'D': 2, 'E': 1}
    
    # Sortiere die Items basierend auf dem zweiten Element (den Tier-Namen)
    sorteditems = sorted(items, key=lambda x: tiers.get(x[1][0], 0), reverse=True)
    
    return sorteditems
    
    
def sortTier(list,tierlist):
    templist=[]
    for i in range(len(tierlist)):
        for e in range(len(list)):
            if list[i][1][0] == tierlist[i]:
                templist.append(list[i])                
                
    list=templist
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
#0 id, 1 name,  2 atk, 3 def, 4 crt,5 spd, 6 intl, 7 lck

def fight(char1,char2):
    spw1 = random.randint(0,100)
    spw2 = random.randint(0,100)
    print(spw1)
    print(spw2)
    
    while spw1 <= char1[7] and spw2<=char2[7]:
        spw1 = random.randint(0,100)
        spw2 = random.randint(0,100)
        print('ups')
     
        

       


    if spw1 <= char1[7]:
        print('first durch Glueck gewonnen')
    elif spw2 <= char2[7]:
        print('second durch Glueck geworden')
    hp1=500
    hp2=500
    turn = 0
    if char1[5]< char2[5]:
        turn = 1
"""        
    if char1[5] == char2[5]:
	    if random.randint(1,50)<50:
	        turn=1
    while hp1>0 and hp2>0:
	    if turn == 0:
	           turn=1
	           hp2=hp-td()
"""        


def td(atk):
    spw = random.randint(0,15)
    atk=int(atk *(100-spw)/100)
    return atk





init()
