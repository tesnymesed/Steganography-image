from tkinter import *

window= Tk()
window.title("Application")
window.geometry("1080x600")
window.config(background="#e3e9d6")

aceuil_btn=Button(window, text="ACCEUIL", font=("Arial",8),bg='#e3e9d6')
insertion_btn=Button(window, text="INSERTION", font=("Arial",8),bg='#fff') 
extraction_btn=Button(window, text="EXTRACTION", font=("Arial",8),bg='#fff') 
aceuil_btn.grid(row=0,column=0, padx=5,columnspan=1,rowspan=500)
insertion_btn.place(x=0,y=0, padx=5)
extraction_btn.place(row=0,column=2, padx=5,columnspan=1,rowspan=500)

frame=Frame(window, bg="#e3e9d6")
label_title=Label(window,text="Bienvenue sur l'application",font=("Arial",40),bg='#e3e9d6')
label_subtitle=Label(window,text="Algorithme de Stéganographie basée sur la DCT et la modification de la table de quantification JPEG",font=("Arial",20),bg='#e3e9d6')
label_title.grid(row=500,column=5)
#label_subtitle.grid(row=101,column=3)
label_binome=Label(window,text="Binome:\n SEDDIKI tesnyme\n BETEBBICHE mahdi sami\n ",font=("Arial",15),bg='#e3e9d6')
#label_binome.pack(side=LEFT)

window.mainloop()