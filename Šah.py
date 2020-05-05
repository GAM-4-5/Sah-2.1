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
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] #Lista svih polja
        print(self.l1)
        for i in range (8):                 #stvara sve gumbe i slaze ih tako da crna i bijela idu naizmjenicno
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik3(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik3(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza1()
        return
    def Faza1(self):
        self.pijunc=PhotoImage(file="Pijunc.png")
        self.kulac=PhotoImage(file="Kulac.png")
        self.konjc=PhotoImage(file="Konjc.png")
        self.lovacc=PhotoImage(file="Lovacc.png")
        self.kraljicac=PhotoImage(file="Kraljicac.png")
        self.kraljc=PhotoImage(file="Kraljc.png")
        self.pijunb=PhotoImage(file="Pijunb.png")
        self.kulab=PhotoImage(file="Kulab.png")
        self.konjb=PhotoImage(file="Konjb.png")
        self.lovacb=PhotoImage(file="Lovacb.png")
        self.kraljicab=PhotoImage(file="Kraljicab.png")
        self.kraljb=PhotoImage(file="Kraljb.png")
        self.belapolja=[self.pijunb,self.kulab,self.konjb,self.lovacb,self.kraljicab,self.kraljb] #lista svih mogucih bijelih figura
        self.listaostalih=[self.kulab,self.kulab,self.kraljb,self.lovacb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.lovacb,self.pijunb,self.pijunc,self.lovacc,self.pijunc,self.pijunc,self.lovacc,self.pijunc,self.pijunc,self.pijunc,self.kraljc,self.kulac,self.kraljicac,self.kulac] #lista svih figura koje su na polju
        self.ostalapolja=["C1","H1","A2","B2","C2","F2","G2","H2","A3","B3","D3","D4","D5","G5","E6","A7","B7","F7","G7","H7","B8","D8","F8","H8"] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.bogznasto=[]#neka lista koja ce provjeravati ako smo kliknuli na polje zauzeto bijelom figurom da tek onda provjerava da nam je sljedeci potez kriv
        while self.brojacneki<len(self.ostalapolja):#slaze pobjedonosna polja, na kraju cu dodati da sva polja s figurama mozes kliknuti i on ce prepoznati je li ispravno
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:#samo bijela ce imati ucinak na klik
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik2(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki])
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level1()
        self.Level1()
    def Level1(self):
        self.slikepkp=[self.kraljicab]#ovo ce biti polja na kojima ce na pocetku biti figure
        self.brojacpkp=0 #brojac dal su sve figure s kojih se pocinje na mjestu
        self.poljaskojihsepocinje=["E1"]
        self.uvjetpobjede1=["E1","E5","E5"] #lista kako treba kliknuti polja, redom (za sada bez veze odabrano)
        self.brojacneki=0#broji koliko se polja stvorilo
        self.brojacpb=0#brojac tocnih poteza
        self.brojacdrugi=0 #brojac klikova
        self.listaneka=[]#???
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):#slaze pobjedonosna polja
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    #Samo provjerava prepoznaje li kad kliknes, kasnije ce provjeravati uvjete i redoslijed,
    #stavit cu da stvara listu kliknutih polja i ako se nakon len(self.uvjetpobjede1) poteza
    #lista poklapa s self.uvjetpobjede1 onda ce ici na level 2 i izbaciti messagebox ili nesto 
    def Klik(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:#kako ce biti figure koje se krecu
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1): #provjerava poklapanje polja i zabranjuje klikanje polja 2 puta jer bi prije mogao kliknuti na neko polje 2. put i gumb bi se premjestio 
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): #ako se poklapaju, onda te pita ako hoćeš nastaviti, ako se 
                    self.KreirajSucelje2()                                                                #ne poklapaju iskoči da si izgubio MOŽDA će kasnije biti zaslon koji 
            else:                                                                                         #će te pitati umjesto ovih prozora
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik2(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik3(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera()
        return
    def LeProvjera(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("POPOGA","izgubio si!")
            self.KreirajSucelje()
        return
    def KreirajSucelje2(self): #sucelje za 1. level, kasnije ce biti dodan prijelaz na 2. level itd. gdje ce klikom nastati novo polje
        self.startgumb.destroy()

        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] #Lista svih polja
        print(self.l1)
        for i in range (8):                 #stvara sve gumbe i slaze ih tako da crna i bijela idu naizmjenicno
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik3(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik3(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza2()
        return
    def Faza2(self):
        self.listaostalih=[self.pijunb,self.pijunb,self.kraljb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.lovacb,self.pijunb,self.pijunc,self.pijunc,self.pijunc,self.kraljicac,self.pijunc,self.pijunc,self.kulac,self.kraljc]
        self.ostalapolja=["B2","C2","F2","G2","H2","A3","D3","F3","F6","D4","A5","C6","E6","B7","F7","A8","E8"] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.bogznasto=[]#neka lista koja ce provjeravati ako smo kliknuli na polje zauzeto bijelom figurom da tek onda provjerava da nam je sljedeci potez kriv
        while self.brojacneki<len(self.ostalapolja):#slaze pobjedonosna polja, na kraju cu dodati da sva polja s figurama mozes kliknuti i on ce prepoznati je li ispravno
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:#samo bijela ce imati ucinak na klik
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik2(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki])
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level2()
        self.Level2()
    def Level2(self):
        self.slikepkp=[self.kraljicab]#ovo ce biti polja na kojima ce na pocetku biti figure
        self.brojacpkp=0 #brojac dal su sve figure s kojih se pocinje na mjestu
        self.poljaskojihsepocinje=["H6"]
        self.uvjetpobjede1=["H6","H8","E5"] #lista kako treba kliknuti polja, redom (za sada bez veze odabrano)
        self.brojacneki=0#broji koliko se polja stvorilo
        self.brojacpb=0#brojac tocnih poteza
        self.brojacdrugi=0 #brojac klikova
        self.listaneka=[]#???
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):#slaze pobjedonosna polja
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    #Samo provjerava prepoznaje li kad kliknes, kasnije ce provjeravati uvjete i redoslijed,
    #stavit cu da stvara listu kliknutih polja i ako se nakon len(self.uvjetpobjede1) poteza
    #lista poklapa s self.uvjetpobjede1 onda ce ici na level 2 i izbaciti messagebox ili nesto 
    def Klik(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:#kako ce biti figure koje se krecu
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1): #provjerava poklapanje polja i zabranjuje klikanje polja 2 puta jer bi prije mogao kliknuti na neko polje 2. put i gumb bi se premjestio 
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): #ako se poklapaju, onda te pita ako hoćeš nastaviti, ako se 
                    self.KreirajSucelje2()                                                                #ne poklapaju iskoči da si izgubio MOŽDA će kasnije biti zaslon koji 
            else:                                                                                         #će te pitati umjesto ovih prozora
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik2(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik3(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera()
        return
    def LeProvjera(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("POPOGA","izgubio si!")
            self.KreirajSucelje()
        return
Sah(Tk())
