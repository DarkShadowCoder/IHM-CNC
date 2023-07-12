# REALISATION D'UNE INTERFACE HOMME MACHINE D'UNE CNC


# importation des bibliotheques
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.simpledialog as sd


# Création de la fenêtre principale
root = tk.Tk()
root.geometry("700x380")
root.title("IHM LASER CO2")
root.config(bg='#C3BDBC')


# Création d'une frame pour afficher l'image sélectionnée
frame1 = tk.Frame(root, width=400, height=300, bg='#EAE0DE')
frame1.place(x=10, y=5)


# fonction pour Redimensionner l'image et renvoyer l'objet ImageTk
def resize_image(image_path, width=40, height=40):
    with Image.open(image_path) as image:
        resized_image = image.resize((width, height))
        return ImageTk.PhotoImage(resized_image)
    

# creation d'une frame2 

frame2 = tk.Frame(root, width=200, height=300)
frame2.place(x=420, y=5)

# creation des boutton de direction

# boutton pour deplacer vers le haut
haut = "./images/4.png"
im_haut = resize_image(haut)
dir_haut = tk.Button(frame2, width=50, height=40, image=im_haut, command=lambda:move_axis('Y', 1))
dir_haut.place(x=70, y=140)


# bouton pour deplacer vers le bas
bas = "./images/6.png"
im_bas = resize_image(bas)
dir_bas = tk.Button(frame2, width=50, height=40, image=im_bas, command=lambda:move_axis('Y', -1))
dir_bas.place(x=70, y=240)


# bouton pour deplacer vers le gauche
gauche = "./images/5.png"
im_gauche = resize_image(gauche)
dir_gauche = tk.Button(frame2, width=50, height=40, image=im_gauche, command=lambda:move_axis('X', -1))
dir_gauche.place(x=10, y=190)


# bouton pour deplacer vers la droite
droite = "./images/7.png"
im_droite = resize_image(droite)
dir_haut = tk.Button(frame2, width=50, height=40, image=im_droite, command=lambda:move_axis('X', 1))
dir_haut.place(x=130, y=190)


# bouton pour la avancer
avance = "./images/1.png"
im_avance = resize_image(avance)
ralentir = "./images/2.png"
im_ralentir = resize_image(ralentir)

# Variables pour stocker l'état actuel de l'image
current_im = 1

# Définir une fonction pour changer l'image lorsqu'on clique sur le bouton
def toggl_image():
    global current_im
    if current_im == 1:
        button2.config(image=im_avance)
        current_im = 2
    elif current_im == 2:
        button2.config(image=im_ralentir)
        current_im = 1

# Créer un bouton pour changer l'image
button2 = tk.Button(frame2, image=im_avance, width=50, height=40, command=toggl_image)
button2.place(x=70, y=190)

#----------------------------------------------------------------------------------------------------------------

# focntion d'affichage de la posite de la broche en valeur numerique (x, y)
def move_axis(axis, direction):
    if axis == 'X':
        current_value = float(x_value.get())
        new_value = current_value + direction
        x_value.delete(0, 'end')
        x_value.insert(0, str(new_value))
    elif axis == 'Y':
        current_value = float(y_value.get())
        new_value = current_value + direction
        y_value.delete(0, 'end')
        y_value.insert(0, str(new_value))
 

x_label = tk.Label(root, text="X Axis:")
x_label.place(x=10, y=320)

x_value = tk.Entry(root, width=10)
x_value.insert(0, '0.0')
x_value.place(x=50, y=320)

y_label = tk.Label(root, text="Y Axis:")
y_label.place(x=10, y=345)

y_value = tk.Entry(root, width=10)
y_value.insert(0, '0.0')
y_value.place(x=50, y=345)

#----------------------------------------------------------------------------------------------


# bouton pour appuyer pause
pause = "./images/10.png"
im_pause = resize_image(pause)
play = "./images/9.png"
im_play = resize_image(play)

# Variables pour stocker l'état actuel de l'image
current_image = 1

# Définir une fonction pour changer d'icone lorsqu'on clique sur le bouton play/pause
def toggle_image():
    global current_image
    if current_image == 1:
        button.config(image=im_play)
        current_image = 2
    elif current_image == 2:
        button.config(image=im_pause)
        current_image = 1

# Créer un bouton qui contient les icone des actions pause et play
button = tk.Button(root, image=im_play, width=50, height=50, command=toggle_image)
button.place(x=630, y=190)

#-------------------------------------------------------------------------------------------------------

# bouton pour activer le laser
laser = "./images/3.png"
im_laser = resize_image(laser)
dir_haut = tk.Button(root, width=50, height=50, image=im_laser)
dir_haut.place(x=630, y=130)


# bouton pour stopper
stopper = "./images/8.png"
im_stopper = resize_image(stopper)
dir_haut = tk.Button(root, width=50, height=50, image=im_stopper)
dir_haut.place(x=630, y=250)


# bouton pour recardrer l'image
cardre = "./images/11.png"
im_cardre = resize_image(cardre)
dir_haut = tk.Button(root, width=50, height=50, image=im_cardre)
dir_haut.place(x=630, y=70)

#----------------------------------------------------------------------------------------------------------

# boutton pour changer de langue en francais et en anglais
french_text = {
    "temperature":"Temperature",
    "vitesse":'vitesse',
    "puissance":'Puissance',
    "fichier":"Sélectionner un fichier",
    'quitter':'Quitter', 
    'frabricant':"produit de l'entreprise AFRICA ROBOT"
}

english_text = {
    "temperature":'Temperature',
    "vitesse":'Speed',
    'puissance':'Power', 
    "fichier":"Select file",
    'quitter':'Quit',
    'frabricant':"product of the company AFRICA ROBOT"
}

# le langage courant est defini oar defaut comme etant le francais
current_text = french_text

def button_clicked():
    global current_text

    # changer de langue
    if current_text==french_text:
        current_text=english_text
    else:
        current_text=french_text
    
    temperature.config(text=current_text['temperature'])
    vitesse.config(text=current_text['vitesse'])
    puissance.config(text=current_text['puissance'])
    button3.config(text=current_text['fichier'])
    quitter.config(text=current_text['quitter'])
    fabricant.config(text=current_text['frabricant'])

# bouton pour changer de langue
langue = "./images/13.jpg"
im_langue = resize_image(langue)
dir_langue = tk.Button(root, width=50, height=50, image=im_langue, command=button_clicked)
dir_langue.place(x=630, y=5)


# Créer des variables de texte pour la température, la vitesse et la puissance
temperature_text = tk.StringVar(value="0°C")
speed_text = tk.StringVar(value="0 mm/min")
power_text = tk.StringVar(value="0%")

# Créer des étiquettes pour afficher les informations de température, de vitesse et de puissance
temperature = tk.Label(frame2, text=current_text['temperature'], font=('century schoolbook', 12, 'bold'))
temperature.place(x=10, y=20)
tk.Label(frame2, textvariable=temperature_text, font=('century schoolbook', 12, 'bold')).place(x=150, y=20)
vitesse = tk.Label(frame2, text=current_text['vitesse'], font=('century schoolbook', 12, 'bold'))
vitesse.place(x=10, y=50)
tk.Label(frame2, textvariable=speed_text,font=('century schoolbook', 11, 'bold')).place(x=100, y=50)
puissance = tk.Label(frame2, text=current_text['puissance'], font=('century schoolbook', 12, 'bold'))
puissance.place(x=10, y=80)
tk.Label(frame2, textvariable=power_text, font=('century schoolbook', 12, 'bold')).place(x=130, y=80)

# Ajouter des boutons pour modifier les informations de température, de vitesse et de puissance
def change_temperature():
    # Demander à l'utilisateur de saisir une nouvelle température
    new_temperature = sd.askstring("Modifier la température", "Nouvelle température:")

    # Mettre à jour la variable de texte de la température
    if new_temperature:
        temperature_text.set(f"{new_temperature}°C")

def change_speed():
    # Demander à l'utilisateur de saisir une nouvelle vitesse
    new_speed = sd.askstring("Modifier la vitesse", "Nouvelle vitesse:")

    # Mettre à jour la variable de texte de la vitesse
    if new_speed:
        speed_text.set(f"{new_speed} mm/min")

def change_power():
    # Demander à l'utilisateur de saisir une nouvelle puissance
    new_power = sd.askstring("Modifier la puissance", "Nouvelle puissance:")

    # Mettre à jour la variable de texte de la puissance
    if new_power:
        power_text.set(f"{new_power}%")



# bouton pour quitter l'application

def on_exit():
    result = messagebox.askquestion("Quitter", "Etes-vous sure de vouloir quitter le programme?")
    if result == "yes":
        root.destroy()
quitter = tk.Button(root, text=current_text["quitter"], width=10, command=on_exit,
                    font=("arial", 10, 'bold'), bg="#970F0F")
quitter.place(x=580, y=340)


############### le menu ############
frame1 = tk.Frame(root, width=400, height=300)
frame1.place(x=10, y=5)

############### fonctionnalites et composant #############

# Fonction pour ouvrir une boîte de dialogue pour sélectionner une image
def open_image():
    # Ouverture de la boîte de dialogue pour sélectionner un fichier
    filepath = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Fichiers image", "*.png;*.jpg;*.jpeg;*.gif")])
    if not filepath:
        # Affichage d'un message si aucun fichier n'a été sélectionné
        label.config(text="Sélectionnez une image à afficher")
        return
    # Chargement de l'image sélectionnée
    image = Image.open(filepath)
    # Redimensionnement de l'image en une dimension de 400x300
    image = image.resize((400, 300))
    # Conversion de l'image en un format compatible avec Tkinter
    photo = ImageTk.PhotoImage(image)
    # Affichage de l'image dans un widget Label
    label.config(text="")
    image_label.config(image=photo)
    image_label.image = photo
     # Afficher le nom de l'image
    name_label = tk.Label(root, text=f"{filepath.split('/')[-1]}", width=38)
    name_label.place(x=135, y=315)

# Création d'un bouton pour ouvrir la boîte de dialogue de sélection de fichier
button3 = tk.Button(root, text=current_text['fichier'], command=open_image)
button3.place(x=135, y=340)


# Création d'un widget Label pour afficher un message si aucun fichier n'a été sélectionné
label = tk.Label(frame1, fg="red", text="Aucun fichier !", font=('New times roman', 29, 'bold'))
frame1.place(x=10, y=5)


# Création d'un widget Label pour afficher l'image sélectionnée
image_label = tk.Label(frame1)
image_label.pack()


# Create the menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", )
file_menu.add_command(label="Ouvrir...", command=open_image)
file_menu.add_separator()
file_menu.add_command(label="Sauvegarder")
file_menu.add_command(label="Sauvegarder en tant que...")
file_menu.add_separator()
file_menu.add_command(label="Sortir", command=root.quit)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Create the Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Modifier la température", command=change_temperature)
edit_menu.add_command(label="Modifier la vitesse", command=change_speed)
edit_menu.add_command(label="Modifier la puissance", command=change_power)

# Add the Edit menu to the menu bar
menu_bar.add_cascade(label="Option", menu=edit_menu)

# Display the menu bar
root.config(menu=menu_bar)

# ajouter le logo de africa robot

# redimensionner l'image contenant le logo
logo = "./images/12.png"
im_logo = resize_image(logo)
dir_logo = tk.Label(root, width=40, height=40, image=im_logo, bg='#C3BDBC')
dir_logo.place(x=305, y=340)

# ajouter le texte du fabrican
fabricant = tk.Label(root, text=current_text['frabricant'], bg='#C3BDBC', font=('century schoolbook', 8, 'italic'))
fabricant.place(x=350, y=360)

# Lancement de la boucle principale
root.mainloop()
