import tkinter as tk

def on_button_click():
    print("Bouton cliqué!")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter")

# Créer un bouton
button = tk.Button(root, text="Cliquez-moi", command=on_button_click)
button.pack(pady=20)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
