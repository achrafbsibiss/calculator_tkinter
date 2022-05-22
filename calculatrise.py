from tkinter import *

expression = ""


# set foction un fois on clik sur un boutton il s'affiche sur le menu
def appuyer(touche):
    if touche == "=":
        calculer()
        return
    
    global expression
    expression += str(touche)
    equation.set(expression)



# set fonction permes de calculer notre equation
def calculer():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression=""



# cet fonction permet nous pour tous effacer
def effacer():
    global expression
    expression = ""
    equation.set("")



# est ici on vas crée un l'intreface graphique
if __name__ == "__main__":
    
    gui = Tk()

    # Couleur de fond
    gui.configure(background="#101419")

    # Titre de l'application
    gui.title("Calculatrice")

    # Tailler de la fenetre
    gui.geometry("195x359")

    # Variable pour stocker le contenu actual
    equation = StringVar()

    # Boite de resultats
    resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)
    resultat.grid(columnspan=4)

    # Boutons
    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "=", "/"]
    ligne = 1
    colonne = 0
    
    # cet un loop pour cree les bouton 
    for bouton in boutons:
       

    #  ici  si  les buton de l'equation avec backround blande
        if bouton == "*" or bouton == "+" or bouton == "+" or bouton =="/" or bouton == "-" or bouton == "=":
               
                b = Label(gui, text=str(bouton),bg="white",fg="black",height=4, width=6)
                # Rendre le texte cliquable
                b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))
       
        else:
           
            b = Label(gui, text=str(bouton),bg="orange",activebackground="black",fg="white",height=4, width=6)
            # Rendre le texte cliquable
            b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1
    
    # Bouton pour effacer
   
    b = Label(gui, text="Effacer", bg="#FF5733",fg="black", height=4, width=28)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=6)
    # Demarrer l'interface graphique
    gui.mainloop()
 