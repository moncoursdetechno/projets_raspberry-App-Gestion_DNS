from guizero import App,Text,TextBox, PushButton, Picture
import webbrowser


def valider():
    newIP=IP_box.value
    newDNS=DNS_box.value
    print(newIP + " "+newDNS)
    file=open("/etc/hosts","a")
    nouveauDNS=file.write( newIP+"            "+newDNS)
    file.write('\n')
    file.close()
  
def effacer():
    IP_box.value=""
    DNS_box.value=""
    
def open_mcdt():
    webbrowser.open_new("http://moncoursdetechno.ovh")

app = App(title="Gestionnaire DNS")

intro1 = Text(app, text="Ajouter facilement un nom de domaine")
intro2 = Text(app, text="� l'une des machines de votre r�seau local !")
picture = Picture(app, image="/home/pi/Downloads/352321_dns_icon.png")
consigne1=Text(app, text="Entrer un nom de domaine :")
DNS_box = TextBox(app, width=20)

consigne1=Text(app, text="Associer l'adresse IP :")
IP_box = TextBox(app, width=20)

#info="Vous voulez associer l'adresse IP "+str(input_box2)+"au nom de domaine"+str(input_box1)+"?"

button1 = PushButton(app, command=valider, text="valider")
button2 = PushButton(app, command=effacer, text="effacer")
#message=Text(app, text=(info))
ligne=Text(app, text="----------------------------------------")
droits = Text(app, text="L.Chastain : Ac-Limoges.fr")
#lien = Text(app,text="http://moncoursdetechno.ovh", command=open_mcdt)
app.display()
