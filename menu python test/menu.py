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
        self.window.geometry("1080x1920")
        self.window.minsize(720, 480)
        path = os.path.abspath(os.getcwd())
        test =os.path.join(path, "bg.jpg")
        self.choix = True 
        
        
        #bg = PhotoImage(file = test)

        
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


    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_button()
        self.create_button3()
        self.create_button2()
        self.vocal_intro()

        

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
        #webbrowser.open_new("http://youtube.com")
       
        text2 = os.getcwd() + "\Passacaglia.mscz"
        
        print(text2)
        music_1 = r'"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe" ' +'"'+ text2 +'"' 
        
        print(music_1)
        os.popen(music_1)
        #subprocess.call([r"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe 'C:\Users\EN_Le\OneDrive\Bureau\PFE\menu python test\Passacaglia.mscz'"])
        #c = music21.converter.parse('path_to_musicxml.xml')
        #c.show('musicxml.pdf')
        #c.show('midi')

    def create_button3(self):
        yt_button3 = Button(self.frame, text="Oral Instructions", font=("Courrier", 25), bg='white', fg='#2962ff',
                       command=self.vocal)
        yt_button3.pack(pady=45, fill=X)




    def open_channel3(self):
        music_1 = r'"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe" "C:\Users\elyes\Documents\GitHub\PFE2023\menu python test\Passacaglia.mscz"'
        
        
        os.popen(music_1)



    def create_button2(self):
        yt_button2 = Button(self.frame, text="select a music sheet", font=("Courrier", 25), bg='white', fg='#2962ff',
                           command=self.open_channel2)
        yt_button2.pack(pady=45, fill=X)

    def open_channel2(self):
        

        liste = Listbox(self.frame)
        liste.insert(1, "music 1")
        liste.insert(2, "music 2")
        liste.insert(3, "music 3")
        liste.insert(4, "music 4")
        liste.insert(5, "music 5")
        liste.insert(6, "music 6")

        liste.pack()

    def vocal(self):

        mytext = 'Instruction'
        textSpeech = gTTS(text=mytext, lang='fr', slow=False)
        #textSpeech.save("instruction" + ".mp3")
       # playsound.playsound('./vocal/' + mytext + '.mp3')

    def vocal_intro(self):
        playsound.playsound('./vocal/intro.mp3')
    
    def vocal_choix1(self):
        playsound.playsound('./vocal/instruction.mp3')
    
    def vocal_choix2(self):
        playsound.playsound('./vocal/select a music sheet.mp3')

    
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