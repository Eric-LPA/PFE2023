from tkinter import *
import os
import webbrowser
import subprocess
import pathlib
import playsound
from gtts import gTTS

#import music21
# coding: utf-8

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("720x580")
        self.window.minsize(720, 480)
        path = os.path.abspath(os.getcwd())
        test =os.path.join(path, "bg.jpg")
        self.choix = False

        #self.vocal()

        self.window.config(background='#2962ff')

        # initialization des composants
        self.frame = Frame(self.window, bg='#2962ff')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)
      
        def key_press(e):
            self.return_choix()

        self.window.bind('<Tab>',key_press)

        def on_select(event):
            selected_item = self.listbox.get(self.listbox.curselection())
            music = os.getcwd() +"\\" + selected_item + ".mscz"
            music_1 = r'"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe" ' +'"'+ music +'"'
            playsound.playsound('./vocal/' + selected_item + '.mp3')
            #os.popen(music_1)

            print("Selected item:", selected_item)

        self.listbox.bind('<<ListboxSelect>>', on_select)

        def spacebar_action(event):
            # Perform action
            selected_item = self.listbox.get(self.listbox.curselection())
            music = os.getcwd() +"\\" + selected_item + ".mscz"
            music_1 = r'"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe" ' +'"'+ music +'"'
            #playsound.playsound('./vocal/' + selected_item + '.mp3')
            os.popen(music_1)
            
        self.listbox.bind('<space>', spacebar_action)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        #self.create_button()
        self.create_button3()
        #self.create_button2()
        self.vocal_intro()
        self.open_channel2()

    def create_title(self):
        label_title = Label(self.frame, text="Music for Everyone", font=("Courrier", 40), bg='#2962ff',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Naviguate with Tabulations", font=("Courrier", 25), bg='#2962ff',
                               fg='white')
        label_subtitle.pack()

    def create_button(self):
        yt_button = Button(self.frame, text="start the application", font=("Courrier", 25), bg='white', fg='#2962ff',
                           command=self.open_channel)
        yt_button.pack(pady=25, fill=X)

    def open_channel(self):
        text2 = os.getcwd() + "\Passacaglia.mscz"
        print(text2)
        music_1 = r'"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe" ' +'"'+ text2 +'"'      
        print(music_1)
        os.popen(music_1)

    def create_button3(self):
        yt_button3 = Button(self.frame, text="Oral Instructions", font=("Courrier", 25), bg='white', fg='#2962ff',
                       command=self.vocal_instruction)
        yt_button3.pack(pady=45, fill=X)

    def open_channel3(self):
        music_1 = r'"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe" "C:\Users\elyes\Documents\GitHub\PFE2023\menu python test\Passacaglia.mscz"'
              
        os.popen(music_1)

    def create_button2(self):
        yt_button2 = Button(self.frame, text="select a music sheet", font=("Courrier", 25), bg='white', fg='#2962ff',
                           command=self.open_channel2)
        yt_button2.pack(pady=45, fill=X)

    def open_channel2(self):

        self.listbox = Listbox(self.window)
        self.listbox.insert(1, "Passacaglia")
        self.listbox.insert(2, "5 Centimetres par Seconde")
        self.listbox.insert(3, "Rachmaninoff Numero 2")
        self.listbox.insert(4, "Duvernoy Etude")

        self.listbox.pack(side=BOTTOM, pady=10)
        self.listbox.configure(width=60, background='#A9A9A9', foreground="white", font=('Times 13'), selectbackground='#DCDC14')

    def vocal(self):
        #mytext = " Voici les Instructions pour naviguer dans notre application Blindar. Utiliser la touche tabulation pour naviguer entre les différents boutons. Une fois sur l'option musique, utiliser les fleches haut et bas pour selectionner la partition voulu. Vous pouvez maintenant lancer l'application. Appuyez sur la touche 'J'. vous pouvez maintenant ecouter chaque note en parcourant la partition avec les fléches gauche et droite. Ou bien appuyer sur espace pour démarrer la musique. Il est aussi possible de passer d'une mesure à l'autre en appuyant sur la touche control plus les flèches de directions. Enfin pour fermer l'application, veuillez appuyer sur la touche F, il sera possible de choisir une nouvelle partition."
        mytext = "Duvernoy Etude"
        textSpeech = gTTS(text=mytext, lang='fr', slow=False)
        textSpeech.save("Duvernoy Etude" + ".mp3")
        #playsound.playsound('./vocal/' + mytext + '.mp3')

    def vocal_intro(self):
        playsound.playsound('./vocal/intro.mp3')
    
    def vocal_choix1(self):
        playsound.playsound('./vocal/instruction.mp3')
    
    def vocal_instruction(self):
        playsound.playsound('./vocal/instruction_full.mp3')

    def vocal_choix2(self):
        playsound.playsound('./vocal/go.mp3')
    
    def return_choix(self):
        print("avant if")
        print(self.choix)
        if self.choix:
            self.choix = False
            self.vocal_choix1()
            print("if")
            print(self.choix)
            
        else:
            self.choix = True
            self.vocal_choix2()
            print("else")
            print(self.choix)
            
    
# afficher
app = MyApp()
app.window.mainloop()