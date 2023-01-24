from tkinter import *
import time
import datetime
#import playsound

montre = Tk()
# titre de l'interface
montre.title("horloge")
#background color
montre.config(bg="black")
# la taille de l'interface
montre.geometry("1900x1000+0+0")

#créer une fonction qui permet de recuperer l'heure en temps réel et l'afficher tous les x ms    

def recupererheure(): 
    # on recupère les heures, minutes et secondes sous forme de chaines de caractère
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    #on recupère les labele heure minute et seconde
    lab_heure.config(text=h)
    lab_minute.config(text=m)
    lab_seconde.config(text=s)
    # maintient l'execution de la fonction recupereheure tous les 1000ms
    lab_heure.after(1000, recupererheure)

# définir les label heures minutes et secondes
#heure
lab_heure = Label(montre, text="00", font =("time new roman", 50,"bold"), bg="#FFFFFF")
lab_heure.place(x=400, y=300, width=200, height=130)
heure = Label(montre, text="heures", font =("time new roman", 20,"bold"), bg="#FFFFFF")
heure.place(x=400, y=450, width=200, height=30)
#minute
lab_minute = Label(montre, text="00", font =("time new roman", 50,"bold"), bg="#FFFFFF")
lab_minute.place(x=650, y=300, width=200, height=130)
minute = Label(montre, text="minutes", font =("time new roman", 20,"bold"), bg="#FFFFFF")
minute.place(x=650, y=450, width=200, height=30)
#seconde
lab_seconde = Label(montre, text="00", font =("time new roman", 50,"bold"), bg="#FFFFFF")
lab_seconde.place(x=900, y=300, width=200, height=130)
seconde = Label(montre, text="secondes", font =("time new roman", 20,"bold"), bg="#FFFFFF")
seconde.place(x=900, y=450, width=200, height=30)
recupererheure()
        
# bouton pour regler l'heure
heureplus = Button(montre, text="+")
heureplus.place(x=400, y=500, width=50, height=30, )
heuremoin = Button(montre, text="-")
heuremoin.place(x=550, y=500, width=50, height=30)

#bouton pour regler les minutes

minuteplus = Button(montre, text="+")
minuteplus.place(x=650, y=500, width=50, height=30)
minutemoin = Button(montre, text="-")
minutemoin.place(x=800, y=500, width=50, height=30)


def alarme():   
    alarmeheure = int(input("heure: "))
    alarmeminute = int(input("Minutes: "))
    #alarme_heure = alarmeheure
    #alarme_minute = alarmeminute
    #print("reglage alamre")
    while True:
        now = time
        heurecourant = now.strftime("%H")
        minutecourant = now.strftime("%M")
        if (alarmeheure == heurecourant):
            if(alarmeminute == minutecourant):
                print("lève toi! ")
            break

reveil = Button(montre, text="Alarme", command=alarme)
reveil.place(x=600, y=550, width=50, height=30,)


#alarme()


montre.mainloop()



