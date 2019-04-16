#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:57:31 2019

"""

import tkinter as tk
import random

class Application (tk.Tk):
    name = 'Logik'
   
    def __init__(self):
        super().__init__ (className = self.name)
        self.title(self.name)
        self.barvy = '#ff0000 #ffa500 #ffff00 #ff00ff #ffffff #00ff00 #00ffff #0000ff'.split()
        self.sirka = 60
        self.vyska = 40
        
        ### Titulek ###
        tk.Label (self, text = 'Logik', font = 'Arial 20').grid(columnspan = 5)
        
        ### Skrytá barva ###  
        self.SkryteBarvy = []
        for sloupec in range (5):
            c = tk.Canvas(self, background = 'black', width = self.sirka, 
                          height = self.vyska)
            c.grid(column = sloupec, row = 1)
            self.SkryteBarvy.append(c)
        
        ### Barva a místo ###
        tk.Label(self, text = 'Barva / Místo', font = 'Arial 13', height = 2, 
                 width = 15).grid(column = 7, row = 2)
        
        ### Potvrď ###
        self.Odeslat = tk.Button (self, text = 'Potvrď', font = 'Arial 12', command = self.Potvrd)
        self.Odeslat.grid (row = 14, column = 7)

        ### Odpověď programu ###
        self.OdpovedProgramu = []
        for radek in range (10):
            lbl = tk.Label(self, text = '- / -', font = 'Arial 13')
            lbl.grid(column = 7, row = radek + 3)
            self.OdpovedProgramu.append(lbl)
        
        tk.Canvas(self, background = 'black', width = 325, height = 5).grid(padx = 4, pady = 4, row=13, column = 0, columnspan = 5)
             
        ### Tlačítka ###
        self.pokusBarvy = []    
        for cislo in range (5):
            barva = (self.barvy[0])
            def akce (c = cislo, b = barva):
                self.click(c,b)
            b = tk.Button (self, width = self.sirka, height = self.vyska, 
                           bg = barva, fg = barva, bitmap = 'gray12',
                           command = akce, activebackground = barva)
            b.barva = 0
            b.poradi = cislo
            b.grid(column = cislo, row = 14)
            self.pokusBarvy.append(b)

        ### Nová hra ###
        tk.Button (self, text = 'Nová hra', font = 'Arial 12', command = self.NewGame).grid(column = 7, row = 1)
        self.NewGame()

    def NewGame(self):
        self.Odeslat.config(state = tk.NORMAL)
        self.hadanka=self.Generuj()
        self.HadaneBarvy = []
        self.pokusBarva = [None]*5
        for radek in range (10):
            self.RadekBarev = []
            for sloupec in range (5):     
                c = tk.Canvas(self, background = 'grey', width = self.sirka, 
                              height = self.vyska)
                c.sloupec = (sloupec)
                c.radek = (radek)
                c.grid(column = sloupec, row = radek + 3)
                self.RadekBarev.append (c)
            self.HadaneBarvy.append(self.RadekBarev)
        self.OdpovedProgramu = []
        for radek in range (10):
            lbl = tk.Label(self, text = '- / -', font = 'Arial 13')
            lbl.grid(column = 7, row = radek + 3)
            self.OdpovedProgramu.append(lbl)
        for i in range (5):
            self.SkryteBarvy[i].config(background = 'black')
        for i in range (5):
            self.pokusBarvy[i].barva = 0
            self.pokusBarvy[i].barva %= len(self.barvy)
            barva = self.barvy[self.pokusBarvy[i].barva]
            self.pokusBarva[i]=barva
            self.pokusBarvy[i].configure(bg = barva, activebackground = barva)
            
    def Generuj(self):
        self.hadanka = []
        self.aktualniradek = 9
        for i in range (5):
            while 1:
                nahodnaBarva = self.barvy [random.randint(0, len(self.barvy)-1)]
                if not nahodnaBarva in self.hadanka:
                    break
            self.hadanka.append(nahodnaBarva)
        return self.hadanka    

    def Potvrd(self):
        print (self.pokusBarva)
        print (self.hadanka)
        self.spravnaBarva = 0
        self.spravnaPozice = 0
        for i in range (5):
            if self.pokusBarva[i] == self.hadanka[i]:
                
                self.spravnaPozice += 1
            elif self.pokusBarva[i] in self.hadanka:
                self.spravnaBarva += 1
        self.OdpovedProgramu[self.aktualniradek].config(text = '{}/{}'.format
                            (self.spravnaBarva, self.spravnaPozice))
        if self.aktualniradek < 1 or self.spravnaPozice == 5:
            self.odkryjHadanku()
            self.Odeslat.config(state = tk.DISABLED)
        self.aktualniradek -= 1
        print (self.spravnaPozice)
        print (self.spravnaBarva)
        self.prepis()

    def click (self, c, b):
        self.pokusBarvy[c].barva += 1
        self.pokusBarvy[c].barva %= len(self.barvy)
        barva = self.barvy[self.pokusBarvy[c].barva]
        self.pokusBarva[c]=barva
        self.pokusBarvy[c].configure(bg = barva, activebackground = barva)
        return
    
    def prepis (self):
        for i in range (5):
            self.HadaneBarvy[self.aktualniradek + 1][i].config(background = self.pokusBarva[i])
    
    def odkryjHadanku(self):
        for i in range (5):
            self.SkryteBarvy[i].config(background = self.hadanka[i])

app = Application()
app.mainloop()
