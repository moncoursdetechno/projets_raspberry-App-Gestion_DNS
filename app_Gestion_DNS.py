from guizero import App,Text,TextBox, PushButton, Picture, Window, Box
import webbrowser

def afficher():
    ecran2 = Window(app, title="liste IP/Nom de domaine")
    file=open("/etc/hosts","r")
    liste=file.read()
    listeaffiche = Text(ecran2, text=liste)
    
    

def valider():
    newIP=IP_box.value
    newDNS=DNS_box.value
    print(newIP + " "+newDNS)
    file=open("/etc/hosts","a")
    nouveauDNS=file.write( newIP+"            "+newDNS)
    file.write('\n')
    file.close()
  
def recommencer():
    IP_box.value=""
    DNS_box.value=""
    
def open_mcdt(link):
    webbrowser.open_new(link)

app = App(title="Gestionnaire DNS")

intro1 = Text(app, text="Ajouter facilement un nom de domaine")
intro2 = Text(app, text="a l'une des machines de votre reseau local !")
picture = Picture(app, image="/home/pi/Downloads/352321_dns_icon.png")

button3 = PushButton(app, command=afficher, text="afficher la liste")

consigne1=Text(app, text="Entrer un nom de domaine :")
DNS_box = TextBox(app, width=20)

consigne1=Text(app, text="Associer l'adresse IP :")
IP_box = TextBox(app, width=20)

#info="Vous voulez associer l'adresse IP "+str(input_box2)+"au nom de domaine"+str(input_box1)+"?"

button1 = PushButton(app, command=valider, text="valider")
button2 = PushButton(app, command=recommencer, text="recommencer")

#message=Text(app, text=(info))
ligne=Text(app, text="----------------------------------------")
box1=Box(app)
box11=Box(box1, align="left")
box12=Box(box1, align="right")
box2=Box(app)
box21=Box(box2, align="left")
box22=Box(box2, align="right")

droits = Text(box11, text="L.Chastain : Ac-Limoges.fr     ")
#lien = Text(app,text="http://moncoursdetechno.ovh", command=open_mcdt)
logoac = Picture(box12, image="/home/pi/Downloads/logo-aclimoges_thumb.gif")
logoinfo = Picture(box21, image="/home/pi/Downloads/211762_information_icon.png")
lien = Text(box22, text="en savoir plus")

#label1 = PushButton(app, text = 'See a video',command = lambda : open_mcdt("https://examscuriosity.com"))

app.display()
