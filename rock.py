import tkinter as tk
from tkinter import messagebox
import random as rd
sc=[]
def w1():
    main=tk.Tk()
    main.title("ROCK PAPER & SCISSORS")
    main.geometry("500x500")
    l1=tk.Label(main,text="WELCOME TO THE ROCK PAPER & SCISSORS GAME.")
    l1.place(x=100,y=50)
    l2=tk.LabelFrame(main,text="SELECT ANY ONE OPTION FROM BELOW")
    l2.place(x=100,y=100)
    var=tk.IntVar()
    b_1=tk.Radiobutton(l2,text="ROCK",variable=var,value=1).pack()
    b_2=tk.Radiobutton(l2,text="PAPER",variable=var,value=2).pack()
    b_3=tk.Radiobutton(l2,text="SCISSORS",variable=var,value=3).pack()
    def w2():
        global b1,b2
        b1=tk.Button(main,text="   EXIT   ",command=w3)
        b2=tk.Button(main,text="TRY AGAIN",command=w_1)
        b1.place(x=400,y=400)
        b2.place(x=300,y=400)
    def w3():
        main.destroy()
        last=tk.Tk()
        last.geometry("300x300")
        last.title("ROCK PAPER & SCISSORS")
        tk.Label(last,text=f"YOUR SCORE IS {sum(sc)}").place(x=100,y=100)
        last.mainloop()   
    def verify():
        if var.get()==0:
            messagebox.showerror("OPTION ERROR","SELECT ANY ONE OPTION.")
        else:
            
            n1=var.get()
            game=["ROCK","PAPER","SCISSORS"]
            n2=rd.choice(game)
            def win():
                info=tk.Label(main,text=f"YOU WON.YOU SELECTED {game[n1-1]} COMPUTER SELECTION IS {n2}")
                info.place(x=100,y=250)
                sc.append(1)
            def loss():
                info=tk.Label(main,text=f"YOU LOST.YOU SELECTED {game[n1-1]} COMPUTER SELECTION IS {n2}")   
                info.place(x=100,y=250)
            if game[n1-1]==n2:
                info=tk.Label(main,text=f"IT'S A TIE.YOU SELECTED {game[n1-1]} COMPUTER SELECTION IS {n2}")
                info.place(x=100,y=250)
            elif (game[n1-1]=="ROCK" and n2=="SCISSORS") or (game[n1-1]=="SCISSORS" and n2=="PAPER") or (game[n1-1]=="PAPER" and n2=="ROCK"):
                win()
            else:
                loss()        
            w2()            
    def w_1():
        b1.destroy()
        b2.destroy()
        verify_b         
    verify_b=tk.Button(main,text="VERIFY",command=verify).place(x=400,y=400)
    main.mainloop()
   
w1()  