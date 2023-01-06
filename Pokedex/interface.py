# Modulos
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import random

from database import *

# cores
Preto = "#444466"  # Preta
Branco = "#feffff"  # branco
Azul = "#6f9fbd"  # azul
Vermelho = "#ef5350"   # vermelho
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


def trocar_pokemon(i):
    global imagem_pokemon, poke_img

    # Tipo do pokemon
    poke_nome['text'] = i
    poke_tipo['text'] = pokemon[i]['tipo'][1]
    poke_id['text'] = pokemon[i]['tipo'][0]

    imagem_pokemon = pokemon[i]['tipo'][2]

    # Imagens
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((545, 230))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    poke_img = Label(frame_pokemon,image=imagem_pokemon, relief='flat', bg=Branco, fg=Preto)
    poke_img.place(x=0, y=5)

    # Ajustes das imagens
    poke_nome.lift()
    poke_tipo.lift()
    poke_id.lift()


# Nome
poke_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=Letra, fg=Branco)
poke_nome.place(x=12, y=15)

# Tipo
poke_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=Letra, fg=Branco)
poke_tipo.place(x=12, y=50)

# ID
poke_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=Letra, fg=Branco)
poke_id.place(x=12, y=75)

# Status
poke_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=Branco, fg=Preto)
poke_status.place(x=15, y=250)

# HP
poke_hp = Label(janela, text='HP: 35', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_hp.place(x=15, y=300)

# Ataque
poke_atk = Label(janela, text='Ataque: 55', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_atk.place(x=15, y=330)

# Defesa
poke_def = Label(janela, text='Defesa: 40', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_def.place(x=15, y=360)

# Velocidade
poke_agi = Label(janela, text='Velocidade: 90', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_agi.place(x=15, y=390)

# Total
poke_tot = Label(janela, text=f'Total: 220', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Valor)
poke_tot.place(x=15, y=420)

# Habilidades
poke_status = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=Branco, fg=Preto)
poke_status.place(x=180, y=250)

# HB1
poke_hb_1 = Label(janela, text='Thunder Shock', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_hb_1.place(x=195, y=300)

# HB2
poke_hb_2 = Label(janela, text='Electro Ball', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=Branco, fg=Letra)
poke_hb_2.place(x=195, y=330)

# Criando os botões

# Imagem dos botões 1
imagem_pokemon_1 = Image.open('image/pokeball.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_poke_img_1 = Button(janela, command=lambda:trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12',bg=Branco, fg=Preto)
b_poke_img_1.place(x=375, y=235)

# Imagem dos botões 2
imagem_pokemon_2 = Image.open('image/pokeball.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_poke_img_2 = Button(janela, command=lambda:trocar_pokemon('Eevee'), image=imagem_pokemon_2, text='Eevee', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12',bg=Branco, fg=Preto)
b_poke_img_2.place(x=375, y=280)

# Imagem dos botões 3
imagem_pokemon_3 = Image.open('image/pokeball.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_poke_img_3 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'),image=imagem_pokemon_3, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12',bg=Branco, fg=Preto)
b_poke_img_3.place(x=375, y=325)

# Imagem dos botões 4
imagem_pokemon_4 = Image.open('image/pokeball.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_poke_img_4 = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=imagem_pokemon_4, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12',bg=Branco, fg=Preto)
b_poke_img_4.place(x=375, y=370)

# Imagem dos botões 5
imagem_pokemon_5 = Image.open('image/pokeball.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_poke_img_5 = Button(janela, command=lambda:trocar_pokemon('Squirtle'), image=imagem_pokemon_5, text='Squirtle', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12',bg=Branco, fg=Preto)
b_poke_img_5.place(x=375, y=415)

# Imagem dos botões 6
imagem_pokemon_6 = Image.open('image/pokeball.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_poke_img_6 = Button(janela, command=lambda:trocar_pokemon('Kecleon'), image=imagem_pokemon_6, text='Kecleon', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12',bg=Branco, fg=Preto)
b_poke_img_6.place(x=375, y=460)

# Ordem aleatória
lista_pokemons = ['Pikachu', 'Eevee', 'Bulbasaur', 'Squirtle', 'Kecleon']
pokemon_escolhido = random.sample(lista_pokemons, 1)

print(f'O pokémon {pokemon_escolhido[0]} foi escolhido!')
trocar_pokemon(pokemon_escolhido[0])

janela.mainloop()