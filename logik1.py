#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:57:31 2019

@author: vla35123
"""

import tkinter as tk

class Application (tk.Tk):
    name = 'Logik'
   
    def __init__(self):
        super().__init__ (className = self.name)
        self.title(self.name)
        self.barvy = '#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 #dd9900 #ffffff'.split()
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
        
        ### Hádaná barva ###
        self.HadaneBarvy = []
        for radek in range (10):
            RadekBarev = []
            for sloupec in range (5):     
                c = tk.Canvas(self, background = 'grey', width = self.sirka, 
                              height = self.vyska)
                c.grid(column = sloupec, row = radek + 3)
                RadekBarev.append (c)
            self.HadaneBarvy.append(RadekBarev)
        
        ### Odpověď programu ###
        OdpovedProgramu = []
        for radek in range (10):
            lbl = tk.Label(self, text = '- / -', font = 'Arial 13')
            lbl.grid(column = 7, row = radek + 3)
            OdpovedProgramu.append(lbl)
        
        ### Tlačítka ###
        self.pokusBarvy = []
        
        for cislo in range (5):
            self.prvni = 0
            self.druhy = 0
            self.treti = 0
            self.ctvrty = 0
            self.paty = 0
            barva = (self.barvy[self.prvni])
            def akce (c = cislo, b = barva):
                self.click(c,b)
            b = tk.Button (self, width = self.sirka, height = self.vyska, 
                           bg = barva, fg = barva, bitmap = 'gray12',
                           command = akce, activebackground = barva)
            b.barva = 0
            b.grid(column = cislo, row = 13)
            self.pokusBarvy.append(b)

#        for radek, barva in enumerate (self.barvy):
#            for sloupec in range (5):
#                def akce (r = radek, s = sloupec):
#                    self.click(r, s)
#                b = tk.Button(self, width = self.sirka, height = self.vyska, 
#                              bg = barva, fg = barva, bitmap = 'gray12',
#                              command = akce)
#                b.grid(column = sloupec, row = radek + 13)
        
       
    def click (self, c, b):
        self.pokusBarvy[c].barva += 1
        self.pokusBarvy[c].barva %= len(self.barvy)
        print(self.pokusBarvy[c].barva)
    
        
        #barva = (self.barvy[self.prvni])
        self.pokusBarvy[c].configure(bg = barva, activebackground = barva)
        return
        
        if c == 0:
            self.prvni = self.prvni + 1
            if self.prvni == 8:
                self.prvni = 0
            else:
                pass
            barva = (self.barvy[self.prvni])
            self.pokusBarvy[c].configure(bg = barva, activebackground = barva)
        if c == 1:
            self.druhy = self.druhy + 1
            if self.druhy == 8:
                self.druhy = 0
            else:
                pass
            barva = (self.barvy[self.druhy])
            self.b.configure(bg = barva, activebackground = barva)
        if c == 2:
            self.treti = self.treti + 1
            if self.treti == 8:
                self.treti = 0
            else:
                pass
            barva = (self.barvy[self.treti])
            self.b.configure(bg = barva, activebackground = barva)
        if c == 3:
            self.ctvrty = self.ctvrty + 1
            if self.ctvrty == 8:
                self.ctvrty = 0
            else:
                pass
            barva = (self.barvy[self.ctvrty])
            self.b.configure(bg = barva, activebackground = barva)
        if c == 4:
            self.paty = self.paty + 1
            if self.paty == 8:
                self.paty = 0
            else:
                pass
            barva = (self.barvy[self.paty])
            self.b.configure(bg = barva, activebackground = barva)
        print (c, barva)

app = Application()
app.mainloop()