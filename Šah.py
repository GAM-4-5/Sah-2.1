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
        self.poc=PhotoImage(file='START.png')
        self.le1=PhotoImage(file='l1.png')
        self.le2=PhotoImage(file='l2.png')
        self.le3=PhotoImage(file='l3.png')
        self.le4=PhotoImage(file='l4.png')
        self.le5=PhotoImage(file='l5.png')
        self.le6=PhotoImage(file='l6.png')
        self.le7=PhotoImage(file='l7.png')
        self.le8=PhotoImage(file='l8.png')
        self.le9=PhotoImage(file='l9.png')
        self.pocetniskrin=Label(self,image=self.poc)
        self.pocetniskrin.grid(row=1, column=1)
        self.startgumb=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Zapocni avanturu',command=lambda:self.s1())
        self.startgumb.grid(row=2,column=1)
        self.root.mainloop()
    def s1(self): #prijelaz na 1. level
        self.pocetniskrin.destroy()
        self.startgumb.destroy()
        self.pocetniskrin1=Label(self,image=self.le1)
        self.pocetniskrin1.grid(row=1, column=1)
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje())
        self.startgumb1.grid(row=2,column=1)
        self.root.mainloop()
        
    def KreirajSucelje(self): #sucelje za 1. level, kasnije ce biti dodan prijelaz na 2. level itd. gdje ce klikom nastati novo polje
        self.upitnik=PhotoImage(file='pit.png')
        self.startgumb1.destroy()
        self.pocetniskrin1.destroy()
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
        self.root.mainloop()
        return
    def Faza1(self):
        self.lala=0#brojac hintova
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
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik4())
        self.goomba.grid(row=1, column=10)
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
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level1()
                        self.root.mainloop()
        self.Level1()
        self.root.mainloop()
    def Level1(self):
        self.slikepkp=[self.kraljicab]#ovo ce biti polja na kojima ce na pocetku biti figure
        self.brojacpkp=0 #brojac dal su sve figure s kojih se pocinje na mjestu
        self.poljaskojihsepocinje=["E1"]
        self.uvjetpobjede1=["E1","E5","A1"] #lista kako treba kliknuti polja, redom (za sada bez veze odabrano)
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
    def Klik4(self):
        messagebox.showinfo("Hint","Nešto nešto najjaca figura")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
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
                    self.s2()                                                                #ne poklapaju iskoči da si izgubio MOŽDA će kasnije biti zaslon koji 
            else:                                                                                         #će te pitati umjesto ovih prozora
                messagebox.showwarning("nop","Izgubio si!")
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
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    def s2(self):
        self.pocetniskrin1=Label(self,image=self.le2)
        
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje2())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()

    def KreirajSucelje2(self): 
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik32(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik32(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza2()
        self.root.mainloop()
        return
    def Faza2(self):
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik42())
        self.goomba.grid(row=1, column=10)
        self.listaostalih=[self.pijunb,self.pijunb,self.kraljb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.lovacb,self.pijunb,self.pijunc,self.pijunc,self.pijunc,self.kraljicac,self.pijunc,self.pijunc,self.kulac,self.kraljc]
        self.ostalapolja=["B2","C2","F2","G2","H2","A3","D3","F3","F6","D4","A5","C6","E6","B7","F7","A8","E8"] 
        self.brojacneki=0
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:#samo bijela ce imati ucinak na klik
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik22(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level2()
        self.Level2()
        self.root.mainloop()
    def Level2(self):
        self.slikepkp=[self.kraljicab]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["H6"]
        self.uvjetpobjede1=["H6","H8","E5"]
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik02(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik02(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik02(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik02(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    def Klik42(self):
        messagebox.showinfo('Hint','Samo naprijed, mozes ti to!')
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik02(self, klik1):
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
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'):  
                    self.s3()                                                                 
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik22(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik32(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera2()
        return
    def LeProvjera2(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
            self.root.mainloop()
        return
    def s3(self):
        self.pocetniskrin1=Label(self,image=self.le3)
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje3())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()


    #level 3
    def KreirajSucelje3(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik33(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik33(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza3()
        self.root.mainloop()
        return
    def Faza3(self):
        self.listaostalih=[self.kraljb,self.kulab,self.kulab,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.lovacb,self.pijunb,self.lovacb,self.pijunb,self.pijunc,self.pijunc,self.pijunc,self.konjc,self.pijunc,self.pijunc,self.pijunc,self.lovacc,self.kraljc,self.kulac,self.kulac] #lista svih figura koje su na polju
        self.ostalapolja=["B1","D1","E1","B2","C2","G2","A3","D3","F3","G3","H3","F5","G5","A6","C6","H6","B7","C7","D7","B8","C8","H8"] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik43())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik23(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level3()
        self.Level3()
        self.root.mainloop()
    def Level3(self):
        self.slikepkp=[self.kraljicab]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["F2"]
        self.uvjetpobjede1=["F2","B6","A1"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)
        

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik03(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik03(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik03(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik03(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.gumb18=Button(self, width=50, height=50, font=self.f,image=self.kraljicac, command=lambda klik1="B6" : self.Klik03(klik1))
        self.gumb18.grid(row=3, column=2)
        
        
        self.root.mainloop()
        return
    def Klik43(self):
        messagebox.showinfo("Hint","Supstitucija")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik03(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik03(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik03(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): 
                    self.s4()                                                                 
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik23(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik33(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera3()
        return
    def LeProvjera3(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    #level 4
    def s4(self):
        self.pocetniskrin1=Label(self,image=self.le4)
     
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje4())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()
    def KreirajSucelje4(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik34(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik34(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza4()
        self.root.mainloop()
        return
    def Faza4(self):
        self.listaostalih=[self.kraljb,self.kulab,self.kraljicab,self.lovacb,self.kulab,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.kraljicac,self.pijunc,self.pijunc,self.pijunc,self.pijunc,self.pijunc,self.pijunc,self.kulac,self.konjc,self.kraljc,self.kulac] #lista svih figura koje su na polju
        self.ostalapolja=['B1','C1','E1','F1','H1','A2','B2','C2','G2','H2','E4','D6','A7','B7','C7','G7','H7','A8','B8','D8','H8'] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik44())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik24(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik34(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level4()
                        self.root.mainloop()
        self.Level4()
        self.root.mainloop()
        return
    def Level4(self):
        self.slikepkp=[self.lovacb]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["C3"]
        self.uvjetpobjede1=["C3","F6","E5"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik04(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik04(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik04(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik04(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.gumn1=Button(self, width=50, height=50, font=self.f,image=self.konjc, command=lambda klik1="F6" : self.Klik04(klik1))
        self.gumn1.grid(row=3, column=6)
        self.root.mainloop()
        return
    def Klik44(self):
        messagebox.showinfo("Hint","Pronadi svoju lovinu")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik04(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik04(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik04(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                self.s5()
                return
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
                return
        return
    def Klik24(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik34(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera4()
        return
    def LeProvjera4(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    #level 5
    def s5(self):
        self.pocetniskrin1=Label(self,image=self.le5)
        
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje5())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()
    def KreirajSucelje5(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik35(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik35(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza5()
        return
    def Faza5(self):
        self.listaostalih=[self.kraljb,self.pijunb,self.pijunb,self.kulab,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunc,self.kraljicab,self.konjc,self.kraljicac,self.pijunc,self.pijunc,self.pijunc,self.kulac,self.kulac,self.kraljc,self.kulab] #lista svih figura koje su na polju
        self.ostalapolja=['B1','B2','C2','F2','G2','A3','H3','F4','A5','B6','C6','D6','B7','F7','G7','A8','C8','G8','D1'] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik45())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik25(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level5()
        self.Level5()
    def Level5(self):
        self.slikepkp=[self.lovacb,self.kulab]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["D3"]
        self.uvjetpobjede1=["D3","H7",'A1'] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik05(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik05(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik05(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik05(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    def Klik45(self):
        messagebox.showinfo("Hint","Igra se zove sah")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik05(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik05(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik05(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): 
                    self.s6()                                                                 
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik25(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik35(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera5()
        return
    def LeProvjera5(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return

    #level 7
    def s6(self):
        self.pocetniskrin1=Label(self,image=self.le6)
        
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje7())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()
    def KreirajSucelje7(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik37(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik37(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza7()
        return
    def Faza7(self):
        self.listaostalih=[self.kulab,self.kraljb,self.pijunb,self.lovacb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunc,self.pijunc,self.konjc,self.pijunc,self.kraljicac,self.pijunc,self.pijunc,self.pijunc,self.kulac,self.kraljc] #lista svih figura koje su na polju
        self.ostalapolja=['E1','G1','A2','B2','C2','F2','G2','H2','B3','D5','A6','B6','B7','D7','F7','G7','H7','C8','G8'] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik47())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik27(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level7()
        self.Level7()
    def Level7(self):
        self.slikepkp=[self.kraljicab]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["D1"]
        self.uvjetpobjede1=["D1","D4","A1"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik07(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik07(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik07(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik07(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    def Klik47(self):
        messagebox.showinfo("Hint","Crni pijun tebe stiti")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik07(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik07(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik07(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): 
                    self.s7()                                                                 
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik27(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik37(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera7()
        return
    def LeProvjera7(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    #level 8
    def s7(self):
        self.pocetniskrin1=Label(self,image=self.le7)
        
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje8())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()
    def KreirajSucelje8(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik38(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik38(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza8()
        return
    def Faza8(self):
        self.listaostalih=[self.kraljicab,self.kraljb,self.pijunb,self.pijunb,self.kulac,self.pijunb,self.pijunb,self.pijunb,self.pijunc,self.pijunb,self.pijunc,self.pijunb,self.pijunc,self.pijunc,self.pijunc,self.kraljicac,self.pijunc,self.pijunc,self.kraljc] #lista svih figura koje su na polju
        self.ostalapolja=['B2','F2','H2','A3','C3','E3','G3','B4','E4','F4','B5','C5','G5','A6','E6','F6','H6','F7','C8'] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik48())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik28(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level8()
        self.Level8()
    def Level8(self):
        self.slikepkp=[self.kulab]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["F1"]
        self.uvjetpobjede1=["F1","C1","A5"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik08(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik08(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik08(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik08(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    def Klik48(self):
        messagebox.showinfo("Hint","Kula F1 -> C1")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik08(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik08(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik08(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): 
                    self.s8()                                                                 
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik28(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik38(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera8()
        return
    def LeProvjera8(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    #level 9
    def s8(self):
        self.pocetniskrin1=Label(self,image=self.le8)
        
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje9())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()
    def KreirajSucelje9(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik39(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik39(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza9()
        return
    def Faza9(self):
        self.listaostalih=[self.kulab,self.kulab,self.kraljb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.kraljicac,self.pijunc,self.pijunc,self.pijunc,self.kulac,self.pijunc,self.pijunc,self.pijunc,self.kulac,self.kraljc] #lista svih figura koje su na polju
        self.ostalapolja=['C1','E1','G1','A2','B2','F2','G2','H2','E3','C5','B6','E6','A7','E7','F7','G7','H7','C8','G8'] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik49())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik29(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level9()
        self.Level9()
    def Level9(self):
        self.slikepkp=[self.kraljicab]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["C3"]
        self.uvjetpobjede1=["C3","D2","A1"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik09(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik09(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik09(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik09(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.root.mainloop()
        return
    def Klik49(self):
        messagebox.showinfo("Hint","begaj")
        self.lala+=1
        if self.lala==3:
            
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()
    def Klik09(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik09(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik09(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                if messagebox.askyesno('Pobjeda', 'Pobjedili ste! Želite li krenuti na sljedeci level?'): 
                    self.s9()                                                                 
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik29(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik39(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera9()
        return
    def LeProvjera9(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    #10
    def s9(self):
        self.pocetniskrin1=Label(self,image=self.le9)
        self.startgumb1=Button(self,width=20, font=('Calibri',16,'bold'), height=6, text='Kreni',command=lambda:self.KreirajSucelje10())
        self.pocetniskrin1.grid(row=1, column=1,rowspan=8,columnspan=8)
        self.startgumb1.grid(row=9,column=1, columnspan=9)
        self.root.mainloop()
    def KreirajSucelje10(self):
        self.pocetniskrin1.destroy()
        self.startgumb1.destroy()
        self.l=[]
        self.l1=[]
        self.bijela=PhotoImage(file="bijela.png")
        self.crna=PhotoImage(file="crna.png")
        self.gumb2=self.gumb=Button(self,width=75, height=75, image=self.bijela)
        self.gumb2.grid(row=1,column=1)
        self.f=('Calibri',16,'bold')
        for i in range (8):
            for j in range (1,9):
                self.l1+=[chr(i+65)+str(j)] 
        print(self.l1)
        for i in range (8):                 
            for j in range (8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.crna,command=lambda klik3="le Pew" : self.Klik310(klik3)) 
                    self.gumb.grid(row=8-i,column=j+1)                                                                      
                else:
                    self.gumb=Button(self, font=self.f,width=75, height=75, image=self.bijela,command=lambda klik3="le Pew" : self.Klik310(klik3))
                    self.gumb.grid(row=8-i,column=j+1)
        self.Faza10()
        return
    def Faza10(self):
        self.listaostalih=[self.kulab,self.kulab,self.kraljb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.pijunb,self.konjb,self.kraljicab,self.kraljicac,self.lovacc,self.konjc,self.pijunc,self.pijunc,self.pijunc,self.pijunc,self.pijunc,self.pijunc,self.kulac,self.kulac,self.kraljc] #lista svih figura koje su na polju
        self.ostalapolja=['D1','F1','G1','A2','B2','F2','G2','H2','C3','A4','H4','D6','F6','A7','B7','C7','F7','G7','H7','A8','F8','G8'] #lista polja zauzetih figurama iz liste ostalih, usporeduje pozicije
        self.brojacneki=0
        self.goomba=Button(self,image=self.upitnik, command=lambda  :self.Klik410())
        self.goomba.grid(row=1, column=10)
        self.bogznasto=[]
        while self.brojacneki<len(self.ostalapolja):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.ostalapolja[self.brojacneki]:
                            if self.listaostalih[self.brojacneki] in self.belapolja:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki], command=lambda klik2=(self.ostalapolja[self.brojacneki]) : self.Klik210(klik2))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                            else:
                                self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.listaostalih[self.brojacneki],command=lambda klik3="le Pew" : self.Klik3(klik3))
                                self.gumb1.grid(row=8-j, column=i+1)
                                print(i,j,self.brojacneki,i*8+j)
                                self.brojacneki+=1
                    except IndexError:
                        self.Level10()
        self.Level10()
    def Level10(self):
        self.slikepkp=[self.lovacb]
        self.brojacpkp=0 
        self.poljaskojihsepocinje=["C4"]
        self.uvjetpobjede1=["C4","F7","A1"] 
        self.brojacneki=0
        self.brojacpb=0
        self.brojacdrugi=0 
        self.listaneka=[]
        self.LISTANEZAUZETIH=list(set(self.l1)-set(self.ostalapolja+[self.uvjetpobjede1[0]]))
        print(self.LISTANEZAUZETIH)

        while self.brojacneki<len(self.uvjetpobjede1):
            for i in range (8):
                for j in range(8):
                    try:
                        if self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki] and (self.uvjetpobjede1[self.brojacneki] not in self.poljaskojihsepocinje):
                            if i%2==j%2:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.crna, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik10(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                            else:
                                self.gumb10=Button(self, width=75, height=75, font=self.f,image=self.bijela, command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik10(klik1))
                                self.gumb10.grid(row=8-j, column=i+1)
                                self.brojacneki+=1
                        elif self.l1[j+8*i]==self.uvjetpobjede1[self.brojacneki]:
                            try:
                                if self.l1[j+8*i]==self.poljaskojihsepocinje[0]:
                                    self.gumb1=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik10(klik1))
                                    self.gumb1.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                                else:
                                    self.gumb2=Button(self, width=50, height=50, font=self.f,image=self.slikepkp[self.brojacpkp], command=lambda klik1=(self.uvjetpobjede1[self.brojacneki]) : self.Klik10(klik1))
                                    self.gumb2.grid(row=8-j, column=i+1)
                                    self.brojacneki+=1
                                    self.brojacpkp+=1
                            except IndexError:
                                self.brojacneki+=1
                    except IndexError:
                        print(self.brojacneki)
        self.butonOKAY=Button(self, width=50, height=50, font=self.f,image=self.pijunc, command=lambda klik1="F7":self.Klik10(klik1))
        self.butonOKAY.grid(row=2, column=6)
        self.root.mainloop()
        return
    def Klik410(self):
        messagebox.showinfo("Hint","Kraljica mora umrijeti")
        self.lala+=1
        if self.lala==3:
            messagebox.showwarning("oh ne","upozoren si da ne koristis previse hintova")
            self.KreirajSucelje()         
    def Klik10(self, klik1):
        self.bogznasto+=["Pepe"]
        self.listaneka+=[klik1]
        if klik1 in self.uvjetpobjede1[0]:
            self.gumb1.destroy()
        else:
            self.gumb2.destroy()
        print(self.uvjetpobjede1[self.brojacdrugi-1], klik1,self.brojacdrugi)
        if klik1==self.uvjetpobjede1[self.brojacdrugi]:
            try:
                if self.uvjetpobjede1[self.brojacdrugi] in self.uvjetpobjede1[:self.uvjetpobjede1.index(self.poljaskojihsepocinje[self.brojacpkp-1])]:
                    self.gumb1=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-2],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik10(klik1))
                    self.gumb1.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
                else:
                    self.gumb2=Button(self, font=self.f,width=50, height=50, image=self.slikepkp[self.brojacpkp-1],command=lambda klik1=(self.uvjetpobjede1[self.brojacdrugi]) : self.Klik10(klik1))
                    self.gumb2.grid(row=9-int(klik1[1]), column=ord(klik1[0])-64)
                    self.brojacdrugi+=1
            except IndexError:
                print("kminkuS")
        else:
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        if (self.brojacdrugi==len(self.uvjetpobjede1)-1):  
            if self.uvjetpobjede1[0:len(self.uvjetpobjede1)-1]==self.listaneka:
                
                self.Pobjeda()                                                                
            else:                                                                                         
                messagebox.showwarning("nop","izgubio si!")
                self.KreirajSucelje()
        return
    def Klik210(self,klik2):
        self.bogznasto+=["Pepe"]
        print(self.bogznasto)
        return
    def Klik310(self,klik3):
        if "Pepe" in self.bogznasto:
            self.bogznasto+=[klik3]
            print(self.bogznasto)
        self.LeProvjera10()
        return
    def LeProvjera10(self):
        if ("Pepe" in self.bogznasto) and ("le Pew" in self.bogznasto):
            messagebox.showwarning("nop","izgubio si!")
            self.KreirajSucelje()
        return
    def Pobjeda(self):
        self.p=PhotoImage(file="p.png")
        self.ccc=Label(self, image=self.p)
        self.ccc.grid(row=1, column=1, rowspan=8, columnspan=8)
        self.root
        return
Sah(Tk())
