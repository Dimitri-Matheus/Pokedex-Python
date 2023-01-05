# Modulos
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

# cores
Preto = "#444466"  # Preta
Branco = "#feffff"  # branca
Azul = "#6f9fbd"  # azul
Vermelho = "#ef5350"   # vermelha
Valor = "#38576b"  # valor
Letra = "#403d3d"   # letra


# Criando a janela
janela = ThemedTk(theme="Breeze")
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg=Branco)

ttk.Separator(janela, orient="horizontal").grid(row=0, columnspan=1, ipadx=272)

# Criando o frame
frame_pokemon = Frame(janela, width=550, height=230, relie='flat')
frame_pokemon.grid(row=1, column=0)

# Nome
poke_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=Letra, fg=Branco)
poke_nome.place(x=12, y=15)

# Tipo
poke_tipo = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=Letra, fg=Branco)
poke_tipo.place(x=12, y=50)

# ID
poke_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=Letra, fg=Branco)
poke_id.place(x=12, y=75)

# Imagens
imagem_pokemon = Image.open('image/Pikachu.png')
imagem_pokemon = imagem_pokemon.resize((545, 230))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

poke_img = Label(frame_pokemon,image=imagem_pokemon, relief='flat', bg=Branco, fg=Preto)
poke_img.place(x=0, y=3)

poke_nome.lift()
poke_tipo.lift()
poke_id.lift()

# Status
poke_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=Branco, fg=Preto)
poke_status.place(x=15, y=250)

# HP
poke_hp = Label(janela, text='HP: 35', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_hp.place(x=15, y=300)

# Ataque
poke_atk = Label(janela, text='Ataque: 55', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_atk.place(x=15, y=325)

# Defesa
poke_def = Label(janela, text='Defesa: 40', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_def.place(x=15, y=350)

# Velocidade
poke_agi = Label(janela, text='Velocidade: 90', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_agi.place(x=15, y=375)

# Total
poke_tot = Label(janela, text=f'Total: 220', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Valor)
poke_tot.place(x=15, y=400)


janela.mainloop()