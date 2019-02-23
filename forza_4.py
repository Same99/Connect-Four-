#forza 4
import cImage as image
import tkinter as tk
from tkinter import messagebox 
import sys

def emptyMatrix(n, m):
    #genera una matrice nxm vuota
    m3 = [[0 for i in range(m)] for i in range(n)]
    return m3

def scegli(f):
    #memorizza la colonna corrispondente alla freccia scelta dove verra' posizionata la pedina
    coord = f.getMouse()
    colonna = 0
    while coord[0] < 100 or coord[1] < 0 or coord[0] > 700 or coord[1] > 100:
        coord = f.getMouse()
    if coord[0] > 100 and coord[0] < 200:
        colonna = 0
    elif coord[0] > 200 and coord[0] < 300:
        colonna = 1
    elif coord[0] > 300 and coord[0] < 400:
        colonna = 2
    elif coord[0] > 400 and coord[0] < 500:
        colonna = 3
    elif coord[0] > 500 and coord[0] < 600:
        colonna = 4
    elif coord[0] > 600 and coord[0] < 700:
        colonna = 5
    return colonna

def disegna(c_i, f, p_s, p_d, arr):
    #disegna il campo da gioco  
    p_s.draw(f)
    sposta_x = 100
    for i in range(len(arr)):
        arr[i].draw(f)
        arr[i].setPosition(sposta_x, 0)
        sposta_x += 100
    sposta_x = 100
    sposta_y = 100
    for i in range(len(c_i)):
            sposta_x = 100    
            for j in range(len(c_i[0])):
                    c_i[i][j].draw(f)
                    c_i[i][j].setPosition(sposta_x, sposta_y)
                    sposta_x += 100
            sposta_y += 100
    p_d.draw(f)
    p_d.setPosition(700, 0)

def colloca(c_m, c_i, p, cc):
    #colloca la pedina nella matrice con i numeri e con le immagini
    r = 0
    while r != 5 and c_m[r+1][cc] == 0:
        #controlla la posizione piu' in basso che puo' raggiungere
        c_m[r+1][cc], c_m[r][cc] = c_m[r][cc], c_m[r+1][cc]
        r += 1
    if c_m[r][cc] != 0:
        #se l'ultimo posto libero e' gia' occupato non viene inserito 
        return False
    else:
        #sostituisce i nuovi valori nelle rispettive matrici
        c_i[r][cc] = p[0]
        c_m[r][cc] = p[1]
    return True

def controlla(c_m):
    #controlla che uno dei due giocatori abbia vinto
    vinto = 0

    #controlla sulle righe
    for c in range(len(c_m[0])):
        for r in range(len(c_m)-3):
            if c_m[r][c] == 1 and c_m[r+1][c] == 1 and c_m[r+2][c] == 1 and c_m[r+3][c] == 1:
                vinto = 1
                break
            elif c_m[r][c] == 2 and c_m[r+1][c] == 2 and c_m[r+2][c] == 2 and c_m[r+3][c] == 2:
                vinto = 2
                break

    #controlla sulle colonne
    for r in range(len(c_m)):
        for c in range(len(c_m[0])-3):
            if c_m[r][c] == 1 and c_m[r][c+1] == 1 and c_m[r][c+2] == 1 and c_m[r][c+3] == 1:
                vinto = 1
                break
            elif c_m[r][c] == 2 and c_m[r][c+1] == 2 and c_m[r][c+2] == 2 and c_m[r][c+3] == 2:
                vinto = 2
                break
    
    #controlla sulla diagonale principale
    for c in range(len(c_m[0])):
        for r in range(len(c_m)-3):
            if c<=2:
                if c_m[r][c] == 1 and c_m[r+1][c+1] == 1 and c_m[r+2][c+2] == 1 and c_m[r+3][c+3] == 1:
                    vinto = 1
                    break
                elif c_m[r][c] == 2 and c_m[r+1][c+1] == 2 and c_m[r+2][c+2] == 2 and c_m[r+3][c+3] == 2:
                    vinto = 2
                    break

    #controlla sulla diagonale secondaria
    for c in range(len(c_m[0])-3):
        for r in range(3, len(c_m)):
            if c_m[r][c] == 1 and c_m[r-1][c+1] == 1 and c_m[r-2][c+2] == 1 and c_m[r-3][c+3] == 1:
                vinto = 1
                break
            elif c_m[r][c] == 2 and c_m[r-1][c+1] == 2 and c_m[r-2][c+2] == 2 and c_m[r-3][c+3] == 2:
                vinto = 2
                break

    #controlla che sul campo ci sia spazio libero per posizionare pedine
    contatore = 0
    for r in range(len(c_m)):
        for c in range(len(c_m[0])):
            if c_m[r][c] == 0:
                contatore += 1
    if contatore == 0 and vinto == 0:
        vinto = 3
    return vinto

def riprova():
    #genera una schermata che chiede all'utente se vuole giocare ancora o uscire
    gioca = tk.Tk()
    gioca.title("Vuoi riprovare?")
    gioca.geometry("200x70")
    
    def quit():
        gioca.destroy()
        sys.exit()

    def gioca_ancora():
        gioca.destroy()
        main()

    riprova = tk.Button(gioca, text="Gioca ancora.", command=gioca_ancora)
    riprova.pack()
    fine = tk.Button(gioca, text="Esci.", command=quit)
    fine.pack()
    gioca.mainloop()
    
def main():
    f = tk.Tk()
    f.withdraw()
    finestra = image.ImageWin("Forza 4", 800, 700)
    vinto = False
    campo_matrice = emptyMatrix(6, 6)
    immagine = image.Image("forza4.gif")
    campo_immagini = [[immagine for i in range(6)] for i in range(6)]
    pedina1 = image.Image("pedina_1.gif")
    pedina2 = image.Image("pedina_2.gif")
    giocatore_1_dx = image.Image("giocatore_1_dx.gif")
    giocatore_1_sx = image.Image("giocatore_1_sx.gif")
    giocatore_2_dx = image.Image("giocatore_2_dx.gif")
    giocatore_2_sx = image.Image("giocatore_2_sx.gif")
    player_sx = giocatore_1_sx
    player_dx = giocatore_1_dx
    pedina = [pedina1, 1]
    freccia = image.Image("freccia.gif")
    frecce = [freccia for i in range(6)]
    fine_1_dx = image.Image("vittoria_1_dx.gif")
    fine_1_sx = image.Image("vittoria_1_sx.gif")
    fine_2_dx = image.Image("vittoria_2_dx.gif")
    fine_2_sx = image.Image("vittoria_2_sx.gif")
    turno = 0
    
    while not vinto:
        if turno % 2 == 0:
            player_sx = giocatore_1_sx
            player_dx = giocatore_1_dx
            pedina = [pedina1, 1]
        elif turno % 2 == 1:
            player_sx = giocatore_2_sx
            player_dx = giocatore_2_dx
            pedina = [pedina2, 2]
        for i in range(2):
            disegna(campo_immagini, finestra, player_sx, player_dx, frecce)
        colonna = scegli(finestra)
        colloca(campo_matrice, campo_immagini, pedina, colonna)
        disegna(campo_immagini, finestra, player_sx, player_dx, frecce)
        fine = controlla(campo_matrice)
        turno += 1
        if fine == 1:
            for i in range(2):
                disegna(campo_immagini, finestra, fine_1_sx, fine_1_dx, frecce)
            messagebox.showinfo("Game Over", "Ha vinto il Giocatore 1!")
            vinto = True
        elif fine == 2:
            for i in range(2):
                disegna(campo_immagini, finestra, fine_2_sx, fine_2_dx, frecce)
            messagebox.showinfo("Game Over", "Ha vinto il Giocatore 2!")
            vinto = True
        elif fine == 3:
            for i in range(2):
                disegna(campo_immagini, finestra, fine_2_sx, fine_2_dx, frecce)
            messagebox.showinfo("Game Over", "Non ha vinto nessuno!")
            vinto = True
           
    finestra._close()
    riprova()

main()  
