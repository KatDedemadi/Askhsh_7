#Άσκηση 7
#ΤΡΙΛΙΖΑ

import random
while True:
        #Επιλογή Συμβόλου
        print("Dialekse me poio symvolo thes na paikseis: X or O? ")
        symvolo_paixth=str(input())
        while symvolo_paixth!="O" and symvolo_paixth!="X" and symvolo_paixth!="o" and symvolo_paixth!="x":
                #Έλεγχος Εγκυρότητας
                print("Dialekses lathos symbolo! Prospathise ksana!!!")
                print("Dialekse me poio symvolo thes na paikseis: X or O? ")
                symvolo_paixth=str(input())
        
        #Καταχώρηση Συμβόλων
        if symvolo_paixth=="x" or symvolo_paixth=="X":
                symvolo_ypologisth="O"
                symvolo_paixth="X"
        else:
                symvolo_ypologisth="X"
                symvolo_paixth="O"

#Τυχαία επιλογή πρώτου παίχτη

        seira=random.randint(0, 1)
        if seira==0:  #Όταν seira=0 παίζει ο παίχτης
                print("Paizeis protos!!")
        else:         #Όταν seira=1 παίζει ο υπολογιστής
                print("O ypologistis paizei protos!!")

#Δημιουργία πύνακα triliza 
      
        triliza=[[" "," "," "],[" "," "," "],[" "," "," "]]

#Εμφάνιση σχήματος τρίλιζας

        if seira==0:
                print(triliza[0][0] , "|", triliza[0][1],  "| " , triliza[0][2])
                print("------------")
                print(triliza[1][0] ,"|"  ,triliza[1][1]  ,"|",  triliza[1][2])
                print("------------")
                print(triliza[2][0] ,"|",  triliza[2][1] , "|" , triliza[2][2])
       
#Έναρξη παιχνιδιού      

        fores=0
        fores=int(fores)
        while True:
                if seira==0:    #Όταν seira=0 παίζει ο παίχτης
                        while True:
                                sthlh=int(input("Dwse moy ton arithmo ths sthlhs poy thes na paikseis(1 h 2 h 3): "))
                                while sthlh<1 or sthlh>3:
                                        print("Edwses lanthasmeno arithmo stilis!")
                                        sthlh=int(input("Dwse moy ton arithmo ths sthlhs poy thes na paikseis(1 h 2 h 3): "))

                                grammh=int(input("Dwse moy ton arithmo ths grammhs poy thes na paikseis(1 h 2 h 3):  "))
                                while grammh<1 or grammh>3:
                                        print("Edwses lanthasmeno arithmo grammhs!")
                                        grammh=int(input("Dwse moy ton arithmo ths grammhs poy thes na paikseis(1 h 2 h 3):  "))

                                if triliza[grammh-1][sthlh-1]==" ":
                                        triliza[grammh-1][sthlh-1]=symvolo_paixth
                                        fores+=1
                                        seira=1
                                        break
                                else:
                                        print("Kati phge strava! Prospathise ksana!!")

                if seira==1:    #Όταν seira=1 παίζει ο υπολογιστής
                        while True:
                                grammh=random.randint(0,2)
                                sthlh=random.randint(0,2)
                        
                                if triliza[grammh][sthlh]==" ":
                                        triliza[grammh][sthlh]=symvolo_ypologisth
                                        fores+=1
                                        seira=0    #Για να δωθει η επόμενη σειρα στον παίχτη 
                                        break
                
#Εμφάνιση σχήματος τρίλιζας
        
                print(triliza[0][0] , "|", triliza[0][1],  "| " , triliza[0][2])
                print("------------")
                print(triliza[1][0] ,"|"  ,triliza[1][1]  ,"|",  triliza[1][2])
                print("------------")
                print(triliza[2][0] ,"|",  triliza[2][1] , "|" , triliza[2][2])

#Έλεγχος αν κέρδισε ο παίχτης

                k=False
                for i in range(3):
                        if ((triliza[i][0]==symvolo_paixth and triliza[i][1]==symvolo_paixth and triliza[i][2]==symvolo_paixth) or
                        (triliza[0][i]==symvolo_paixth and triliza[1][i]==symvolo_paixth and triliza[2][i]==symvolo_paixth)):
                                print("KERDISES!")
                                k=True    
                    
                if ((triliza[0][0]==symvolo_paixth and triliza[1][1]==symvolo_paixth and triliza[2][2]==symvolo_paixth) or
                (triliza[0][2]==symvolo_paixth and triliza[1][1]==symvolo_paixth and triliza[2][0]==symvolo_paixth)):
                        print("KERDISES!")
                        k=True

#Έλεγχος αν κέρδισε ο υπολογιστής

                for i in range(3):
                        if ((triliza[i][0]==symvolo_ypologisth and triliza[i][1]==symvolo_ypologisth and triliza[i][2]==symvolo_ypologisth) or
                        (triliza[0][i]==symvolo_ypologisth and triliza[1][i]==symvolo_ypologisth and triliza[2][i]==symvolo_ypologisth)):
                                print("EXAESES!")
                                k=True
               
                if ((triliza[0][0]==symvolo_ypologisth and triliza[1][1]==symvolo_ypologisth and triliza[1][1]==symvolo_ypologisth) or
                (triliza[0][2]==symvolo_ypologisth and triliza[1][1]==symvolo_ypologisth and triliza[2][0]==symvolo_ypologisth)):
                        print("EXASES!")
                        k=True

#Έλεγχος αν υπάρχει ισοπαλία
                if k==False and fores==9:
                        print("ISOPALIA!")
                        break
                elif k==True:
                        break
                
#Επανεκκίνηση παιχνιδιού
        apantisi=str(input("An thelete na paiksete ksana pieste to 'ENTER'"))
        if apantisi!="":
                break
                
