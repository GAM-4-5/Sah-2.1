from tkinter import*
from tkinter import messagebox
class Sah(Frame):
    def __init__(self, root):
        self.root=root
        self.root.title("Šah")
        super().__init__(self.root)
        self.grid()
        self.Start()
        return
    def Start(self): #privremeno, kasnije ce imati pravi start screen
        self.startgumb=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Zapocni avanturu',command=lambda:self.KreirajSucelje())
        self.startgumb.grid(row=1,column=1)
        self.root.mainloop()
    def KreirajSucelje(self): #sucelje za 1. level, kasnije ce biti dodan prijelaz na 2. level itd. gdje ce klikom nastati novo polje
        self.startgumb.destroy()
        self.l=[]
        self.l1=[]
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] #Lista svih polja
        print(self.l1)
        for i in range (8):                 #stvara sve gumbe i slaze ih tako da crna i bijela idu naizmjenicno
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=5, height=2, text=str(self.l1[i+j*8]), bg='black',fg='white')  #samo privremeno ce pisati broj polja,
                    self.gumb.grid(row=8-i,column=j+1)                                                                      #kasnije ce biti figure
                else:
                    self.gumb=Button(self, font=self.f,width=5, height=2, text=str(self.l1[i+j*8]), bg='white',fg='black')
                    self.gumb.grid(row=8-i,column=j+1)
        self.Level1()
        return
    def Level1(self):
        self.uvjetpobjede1=["A1","A2","H8","B2","C4"] #lista kako treba kliknuti polja, redom (za sada bez veze odabrano)
        self.brojacneki=0#broji koliko se polja stvorilo
        self.brojacpb=0#brojac tocnih poteza
        self.brojacdrugi=0 #brojac klikova
        self.listaneka=[]
        while self.brojacneki<len(self.uvjetpobjede1):#slaze pobjedonosna polja, na kraju cu dodati da sva polja s figurama mozes kliknuti i on ce prepoznati je li ispravno
            for i in range (8):
                for j in range(8):
                    if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]: #iz nekog razloga pise list index out of range iako stvori sve buttone
                        self.gumb1=Button(self, font=self.f,width=5, height=2, bg="purple",command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                        self.gumb1.grid(row=8-j, column=i+1)
                        print(i,j,self.brojacneki,i*8+j)
                        self.brojacneki+=1
        self.root.mainloop()
        return
    #Samo provjerava prepoznaje li kad kliknes, kasnije ce provjeravati uvjete i redoslijed,
    #stavit cu da stvara listu kliknutih polja i ako se nakon len(self.uvjetpobjede1) poteza
    #lista poklapa s self.uvjetpobjede1 onda ce ici na level 2 i izbaciti messagebox ili nesto 
    def Klik(self, klik1):
        self.listaneka+=[klik1]
        self.brojacdrugi+=1
        if self.brojacdrugi==len(self.uvjetpobjede1): #provjerava poklapaju li se kliknuta polja s listom
            if self.uvjetpobjede1==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): #ako se poklapaju, onda te pita ako hoćeš nastaviti, ako se 
                    self.KreirajSucelje2()                                                                #ne poklapaju iskoči da si izgubio MOŽDA će kasnije biti zaslon koji 
            else:                                                                                         #će te pitati umjesto ovih prozora
                messagebox.showwarning("nop","izgubio si!")
        return



    
    #samo copypaste s izmijenjenim imenima funkcija i onoga u zagradi (klik1 u klik2), kasnije će biti svih 10
    def KreirajSucelje2(self):
        self.l=[]
        self.l1=[]
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=5, height=2, text=str(self.l1[i+j*8]), bg='black',fg='white')
                    self.gumb.grid(row=8-i,column=j+1)
                else:
                    self.gumb=Button(self, font=self.f,width=5, height=2, text=str(self.l1[i+j*8]), bg='white',fg='black')
                    self.gumb.grid(row=8-i,column=j+1)
        self.Level2()
        return
    def Level2(self):
        self.uvjetpobjede1=["A3","A5","H7","D2","C4"]
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]: 
                        self.gumb1=Button(self, font=self.f,width=5, height=2, bg='purple',command=lambda klik2=(self.uvjetpobjede1[self.brojacneki]) : self.Klik2(klik2))
                        self.gumb1.grid(row=8-j, column=i+1)
                        print(i,j,self.brojacneki,i*8+j)
                        self.brojacneki+=1
        self.root.mainloop()
        return
    def Klik2(self, klik2):
        self.listaneka+=[klik2]
        self.brojacdrugi+=1
        if self.brojacdrugi==len(self.uvjetpobjede1):
            if self.uvjetpobjede1==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'):
                    self.KreirajSucelje3()
                else:
                    messagebox.showwarning("nop","izgubio si!")
        return
    def KreirajSucelje3(self): 
        self.startgumb.destroy()
        self.l=[]
        self.l1=[]
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)]
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=5, height=2, text=str(self.l1[i+j*8]), bg='black',fg='white')  
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=5, height=2, text=str(self.l1[i+j*8]), bg='white',fg='black')
                    self.gumb.grid(row=8-i,column=j+1)
        self.Level3()
        return
    def Level3(self):
        self.uvjetpobjede1=["A8","A8","H8","B2","C4"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]: 
                        self.gumb1=Button(self, font=self.f,width=5, height=2, bg='purple',command=lambda klik3=(self.uvjetpobjede1[self.brojacneki]) : self.Klik3(klik3))
                        self.gumb1.grid(row=8-j, column=i+1)
                        print(i,j,self.brojacneki,i*8+j)
                        self.brojacneki+=1
        self.root.mainloop()
        return
    def Klik3(self, klik3):
        self.listaneka+=[klik3]
        self.brojacdrugi+=1
        if self.brojacdrugi==len(self.uvjetpobjede1):
            if self.uvjetpobjede1==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'):
                    print("mhm")
                else:
                    messagebox.showwarning("nop","izgubio si!")
        return
Sah(Tk())
