"""Life Calculator v0.1294a
   Added Features:
   --->kongum cringu
   --->Fixed  some things...
   --->Blank ah vitta, unaku varum cringu!
   --->Nee ippo try panni paaru!

   Done with lov and affection by ironman_jd & sagur_bhai.
   Edited with passion by RobinHoodUthappa
   Produced with cringe by MukiUltraDetergent
   Idea sim card given by greaat AdolfAnnand
   No comments. Simply waste.
"""
import mysql.connector as sql
import csv
import time

time.sleep(2)
def test2(Name1,Name2,Relation):
    connection = sql.connect(host = "localhost", user = 'root', passwd = '7981.jsdh', database = 'KBROS')
    cursor = connection.cursor()
    
    c = "insert into MAMA_INFO values('{}','{}','{}')".format(Name1,Name2,Relation)
    cursor.execute(c)
    connection.commit()

    

def Test(Name1,Name2,Relation):               
    with open("C:\\Users\lab\AppData\Local\Temp\MAMA_INFO.csv","a")as f:
        cwriter = csv.writer(f)
        cwriter.writerow([Name1,Name2,Relation])
    
class lifeCalculator:

    def __init__(self,Name1,Name2):

        global count
        Name1List = list(Name1)
        Name2List = list(Name2)
        for i in Name2:
            if i in Name1List:
                Name1List.remove(i)
                Name2List.remove(i)

        lname = Name1List+Name2List
        count = len(lname)

    def lifecalculation (self):
        l = ['F','L','A','M','E','S']
        pop=0
        while len(l)>1:
            for i in range(count):
                if pop>len(l)-1:
                    pop = 0
                pop += 1
                
            l.pop(pop-1)
           
            pop -=1
        return l[0]

    def Display(self,Relation,Name1,Name2,type=0):
        #test2(Name1,Name2,Relation)
        #Test(Name1,Name2,Relation)
        if type == 0:
            return("            .>>>   <<<.\n           /    \ /    \\\n           |     ^     |\n            \         /\n             \   "+Relation+"   /\n              \     /\n               \   /\n                \ /\n                 !")
        
        elif type==1:
            
            if Relation == "F":
                return("You and YOUR CRUSH are GOOD FRIENDS")
            elif Relation == "L":
                return(Name2+" LOVE'S You")
            elif Relation == "A":
                return("You Have AFFECTION on Him/Her ")
            elif Relation == "M":
                return("In future u both will have a baby" )
            elif Relation == "E":
                return("Try ur best")
            elif Relation == "S":
                return("She will call u as brother"+'('+"RAJA RANI"+')')
        elif type==3:
            return("It will be with u Forever")
            
def main():
    global Name1,Name2
    Name1 = input('enter ur name :')
    Name2 = input('enter ur crush name :')       

main()

if Name1.strip() == "":
    print("Trying to avoid ah?")
    main()

elif Name2.strip() == "":
    print("Trying to avoid ah?")
    main()

elif Name1 == Name2:
    print("u can have hanndyy relationship with ur bro/sis!")

else:
    Flames = lifeCalculator(Name1,Name2)
    Relationship = Flames.lifecalculation()
    print(Flames.Display(Relationship,Name1,Name2,type=0))
    print(Flames.Display(Relationship,Name1,Name2,type=1))
