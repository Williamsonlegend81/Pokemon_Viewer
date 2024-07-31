from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("PokeInfo")
root.geometry("500x600")
TYPES = [
    ("Normal","Normal"),
    ("Fighting","Fighting"),
    ("Flying","Flying"),
    ("Poison","Poison"),
    ("Ground","Ground"),
    ("Rock","Rock"),
    ("Bug","Bug"),
    ("Ghost","Ghost"),
    ("Steel","Steel"),
    ("Fire","Fire"),
    ("Water","Water"),
    ("Grass","Grass"),
    ("Electric","Electric"),
    ("Psychic","Psychic"),
    ("Ice","Ice"),
    ("Dragon","Dragon"),
    ("Dark","Dark"),
    ("Fairy","Fairy")
]
def undo_information(name_pokemon,species_pokemon,list,image_number):
    global MyLabel1
    global my_btn_backward
    global my_btn_forward
    global my_btn_quit
    global my_pokemon
    global Label2
    global Label3
    global Label4
    global back_button
    global top1

    if (name_pokemon=="Bulbasaur" and species_pokemon=="Grass"):
        Label3.grid_forget()
        Label2.grid_forget()
        Label4.grid_forget()
        back_button.grid_forget()
        Image1 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/001_Bulbasaur.png"))
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(image_number+1,list,"Grass"))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(image_number-1,list,"Grass"),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_btn_forward.grid(row=1,column=2)
        my_btn_backward.grid(row=1,column=0)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=Image1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
        my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo("Bulbasaur",1,"Grass",list))
        my_pokemon.grid(row=1,column=3)
def pokeinfo(name_pokemon,image_number,type_pokemon,list):
    global my_pokemon
    global MyLabel1
    global my_btn_forward
    global my_btn_backward
    global my_btn_quit
    global Label2
    global Label3
    global Label4
    global back_button

    if (name_pokemon=="Bulbasaur"):
        MyLabel1.grid_forget()
        my_btn_forward.grid_forget()
        my_btn_backward.grid_forget()
        my_btn_quit.grid_forget()
        my_pokemon.grid_forget()
        Label2 = Label(top1,text="Information: A strange seed was planted on its back at birth. The plant sprouts and grows with this POKeMON")
        Label2.grid(row=0,column=0)
        Label3 = Label(top1,text="Weakness: Flying(x2), Fire(x2), Psychic(x2), Ice(x2)")
        Label3.grid(row=1,column=0)
        Label4 = Label(top1,text="Effective Against: Fighting(x(1/2)), Water(x(1/2)), Grass(x(1/2)), Electric(x(1/2)), Fairy(x(1/2))")
        Label4.grid(row=2,column=0)
        back_button = Button(top1,text="Back",command=lambda: undo_information("Bulbasaur",image_number,type_pokemon,list))
        back_button.grid(row=3,column=0,columnspan=4)
def forward(image_number,list,type_pokemon):
    global top1
    global MyLabel1
    global my_btn_forward
    global my_btn_backward
    global my_pokemon

    MyLabel1.grid_forget()
    my_pokemon.grid_forget()
    myImg1 = list[image_number-1]
    if (type_pokemon=="Grass"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo("Bulbasaur",1,"Grass",list))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Ivysaur",command=lambda: pokeinfo("Ivysaur",2,"Grass",list))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Venasaur",command=lambda: pokeinfo("Venasaur",3,"Grass",list))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Oddish",command=lambda: pokeinfo("Oddish",4,"Grass",list))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Gloom",command=lambda: pokeinfo("Gloom",5,"Grass",list))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Vileplume",command=lambda: pokeinfo("Vileplume",6,"Grass",list))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Paras",command=lambda: pokeinfo("Paras",7,"Grass",list))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Parasect",command=lambda: pokeinfo("Parasect",8,"Grass",list))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Bellsprout",command=lambda: pokeinfo("Bellsprout",9,"Grass",list))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Weepinbell",command=lambda: pokeinfo("Weepinbell",10,"Grass",list))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Victreebell",command=lambda: pokeinfo("Victreebell",11,"Grass",list))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Exeggcute",command=lambda: pokeinfo("Exeggcute",12,"Grass",list))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Exeggutor",command=lambda: pokeinfo("Exeggutor",13,"Grass",list))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Tangela",command=lambda: pokeinfo("Tangela",14,"Grass",list))
    elif (type_pokemon=="Fire"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Charmander",command=lambda: pokeinfo("Charmander"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Charmeleon",command=lambda: pokeinfo("Charmeleon"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Charizard",command=lambda: pokeinfo("Charizard"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Vulpix",command=lambda: pokeinfo("Vulpix"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Ninetales",command=lambda: pokeinfo("Ninetales"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Growlithe",command=lambda: pokeinfo("Growlithe"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Arcanine",command=lambda: pokeinfo("Arcanine"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Ponyta",command=lambda: pokeinfo("Ponyta"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Rapidash",command=lambda: pokeinfo("Rapidash"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Magmar",command=lambda: pokeinfo("Magmar"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Flareon",command=lambda: pokeinfo("Flareon"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Moltres",command=lambda: pokeinfo("Moltres"))
    elif (type_pokemon=="Water"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Squirtle",command=lambda: pokeinfo("Squirtle"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Wartortle",command=lambda: pokeinfo("Wartortle"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Blastoise",command=lambda: pokeinfo("Blastoise"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Psyduck",command=lambda: pokeinfo("Psyduck"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Golduck",command=lambda: pokeinfo("Golduck"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Poliwag",command=lambda: pokeinfo("Poliwag"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Poliwhirl",command=lambda: pokeinfo("Poliwhirl"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Poliwrath",command=lambda: pokeinfo("Poliwrath"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Tentacool",command=lambda: pokeinfo("Tentacool"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Tentacruel",command=lambda: pokeinfo("Tentacruel"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Slowpoke",command=lambda: pokeinfo("Slowpoke"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Slowbro",command=lambda: pokeinfo("Slowbro"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Seel",command=lambda: pokeinfo("Seel"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Dewgong",command=lambda: pokeinfo("Dewgong"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Shellder",command=lambda: pokeinfo("Shelldar"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Cloyster",command=lambda: pokeinfo("Cloyster"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Krabby",command=lambda: pokeinfo("Krabby"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Kingler",command=lambda: pokeinfo("Kingler"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Horsea",command=lambda: pokeinfo("Horsea"))
        elif (image_number==20):
            my_pokemon = Button(top1,text="Seadra",command=lambda: pokeinfo("Seadra"))
        elif (image_number==21):
            my_pokemon = Button(top1,text="Goldeen",command=lambda: pokeinfo("Goldeen"))
        elif (image_number==22):
            my_pokemon = Button(top1,text="Seaking",command=lambda: pokeinfo("Seaking"))
        elif (image_number==23):
            my_pokemon = Button(top1,text="Staryu",command=lambda: pokeinfo("Staryu"))
        elif (image_number==24):
            my_pokemon = Button(top1,text="Starmie",command=lambda: pokeinfo("Starmie"))
        elif (image_number==25):
            my_pokemon = Button(top1,text="Magikarp",command=lambda: pokeinfo("Magikarp"))
        elif (image_number==26):
            my_pokemon = Button(top1,text="Gyarados",command=lambda: pokeinfo("Gyarados"))
        elif (image_number==27):
            my_pokemon = Button(top1,text="Lapras",command=lambda: pokeinfo("Lapras"))
        elif (image_number==28):
            my_pokemon = Button(top1,text="Vaporeon",command=lambda: pokeinfo("Vaporeon"))
        elif (image_number==29):
            my_pokemon = Button(top1,text="Omanyte",command=lambda: pokeinfo("Omanyte"))
        elif (image_number==30):
            my_pokemon = Button(top1,text="Omastar",command=lambda: pokeinfo("Omastar"))
        elif (image_number==31):
            my_pokemon = Button(top1,text="Kabuto",command=lambda: pokeinfo("Kabuto"))
        elif (image_number==32):
            my_pokemon = Button(top1,text="Kabutops",command=lambda: pokeinfo("Kabutops"))
    elif (type_pokemon=="Electric"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Pikachu",command=lambda: pokeinfo("Pikachu"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Raichu",command=lambda: pokeinfo("Raichu"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Magnemite",command=lambda: pokeinfo("Magnemite"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Magneton",command=lambda: pokeinfo("Magneton"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Voltorb",command=lambda: pokeinfo("Voltorb"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Electrode",command=lambda: pokeinfo("Electrode"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Electabuzz",command=lambda: pokeinfo("Electabuzz"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Jolteon",command=lambda: pokeinfo("Jolteon"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Zapdos",command=lambda: pokeinfo("Zapdos"))
    elif (type_pokemon=="Poison"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo("Bulbasaur"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Ivysaur",command=lambda: pokeinfo("Ivysaur"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Venasaur",command=lambda: pokeinfo("Venasaur"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Weedle",command=lambda: pokeinfo("Weedle"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Kakuna",command=lambda: pokeinfo("Kakuna"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Beedrill",command=lambda: pokeinfo("Beedrill"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Ekans",command=lambda: pokeinfo("Ekans"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Arbok",command=lambda: pokeinfo("Arbok"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Nidoran_f",command=lambda: pokeinfo("Nidoran_f"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Nidorina",command=lambda: pokeinfo("Nidorina"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Nidoqueen",command=lambda: pokeinfo("Nidoqueen"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Nidoran_m",command=lambda: pokeinfo("Nidoran_m"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Nidorino",command=lambda: pokeinfo("Nidorino"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Nidoking",command=lambda: pokeinfo("Nidoking"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Zubat",command=lambda: pokeinfo("Zubat"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Golbat",command=lambda: pokeinfo("Golbat"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Oddish",command=lambda: pokeinfo("Oddish"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Gloom",command=lambda: pokeinfo("Gloom"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Vileplume",command=lambda: pokeinfo("Vileplume"))
        elif (image_number==20):
            my_pokemon = Button(top1,text="Venonat",command=lambda: pokeinfo("Venonat"))
        elif (image_number==21):
            my_pokemon = Button(top1,text="Venomoth",command=lambda: pokeinfo("Venomoth"))
        elif (image_number==22):
            my_pokemon = Button(top1,text="Bellsprout",command=lambda: pokeinfo("Bellsprout"))
        elif (image_number==23):
            my_pokemon = Button(top1,text="Weepinbell",command=lambda: pokeinfo("Weepinbell"))
        elif (image_number==24):
            my_pokemon = Button(top1,text="Victreebell",command=lambda: pokeinfo("Victreebell"))
        elif (image_number==25):
            my_pokemon = Button(top1,text="Grimer",command=lambda: pokeinfo("Grimer"))
        elif (image_number==26):
            my_pokemon = Button(top1,text="Muk",command=lambda: pokeinfo("Muk"))
        elif (image_number==27):
            my_pokemon = Button(top1,text="Gastly",command=lambda: pokeinfo("Gastly"))
        elif (image_number==28):
            my_pokemon = Button(top1,text="Haunter",command=lambda: pokeinfo("Haunter"))
        elif (image_number==29):
            my_pokemon = Button(top1,text="Gengar",command=lambda: pokeinfo("Gengar"))
        elif (image_number==30):
            my_pokemon = Button(top1,text="Koffing",command=lambda: pokeinfo("Koffing"))
        elif (image_number==31):
            my_pokemon = Button(top1,text="Weezing",command=lambda: pokeinfo("Weezing"))
    elif (type_pokemon=="Bug"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Caterpie",command=lambda: pokeinfo("Caterpie"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Metapod",command=lambda: pokeinfo("Metapod"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Butterfree",command=lambda: pokeinfo("Butterfree"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Weedle",command=lambda: pokeinfo("Weedle"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Kakuna",command=lambda: pokeinfo("Kakuna"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Beedrill",command=lambda: pokeinfo("Beedrill"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Paras",command=lambda: pokeinfo("Paras"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Parasect",command=lambda: pokeinfo("Parasect"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Venonat",command=lambda: pokeinfo("Venonat"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Venomoth",command=lambda: pokeinfo("Venomoth"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Scyther",command=lambda: pokeinfo("Scyhther"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Pinsir",command=lambda: pokeinfo("Pinsir"))
    elif (type_pokemon=="Psychic"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Abra",command=lambda: pokeinfo("Abra"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Kadabra",command=lambda: pokeinfo("Kadabra"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Alakazam",command=lambda: pokeinfo("Alakazam"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Slowpoke",command=lambda: pokeinfo("Slowpoke"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Slowbro",command=lambda: pokeinfo("Slowbro"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Drowzee",command=lambda: pokeinfo("Drowzee"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Hypno",command=lambda: pokeinfo("Hypno"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Exeggcute",command=lambda: pokeinfo("Exeggcute"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Exeggutor",command=lambda: pokeinfo("Exeggutor"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Mr. Mime",command=lambda: pokeinfo("Mr. Mime"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Jynx",command=lambda: pokeinfo("Jynx"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Mewtwo",command=lambda: pokeinfo("Mewtwo"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Mew",command=lambda: pokeinfo("Mew"))
    elif (type_pokemon=="Normal"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Pidgey",command=lambda: pokeinfo("Pidgey"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Pidgeotto",command=lambda: pokeinfo("Pidgeotto"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Pidgeot",command=lambda: pokeinfo("Pidgeot"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Rattata",command=lambda: pokeinfo("Rattata"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Raticate",command=lambda: pokeinfo("Raticate"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Spearow",command=lambda: pokeinfo("Spearow"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Fearow",command=lambda: pokeinfo("Fearow"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Jigglypuff",command=lambda: pokeinfo("Jigglypuff"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Wigglytuff",command=lambda: pokeinfo("Wigglytuff"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Meowth",command=lambda: pokeinfo("Meowth"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Persian",command=lambda: pokeinfo("Persian"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Farfetch'd",command=lambda: pokeinfo("Farfetch'd"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Doduo",command=lambda: pokeinfo("Doduo"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Dodrio",command=lambda: pokeinfo("Dodrio"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Lickitung",command=lambda: pokeinfo("Lickitung"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Chansey",command=lambda: pokeinfo("Chansey"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Kangaskhan",command=lambda: pokeinfo("Kangaskhan"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Tauros",command=lambda: pokeinfo("Tauros"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Ditto",command=lambda: pokeinfo("Ditto"))
        elif (image_number==20):
            my_pokemon = Button(top1,text="Eevee",command=lambda: pokeinfo("Eevee"))
        elif (image_number==21):
            my_pokemon = Button(top1,text="Porygon",command=lambda: pokeinfo("Porygon"))
        elif (image_number==22):
            my_pokemon = Button(top1,text="Snorlax",command=lambda: pokeinfo("Snorlax"))
    elif (type_pokemon=="Fighting"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Mankey",command=lambda: pokeinfo("Mankey"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Primeape",command=lambda: pokeinfo("Primeape"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Poliwrath",command=lambda: pokeinfo("Poliwrath"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Machop",command=lambda: pokeinfo("Machop"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Machoke",command=lambda: pokeinfo("Machoke"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Machamp",command=lambda: pokeinfo("Machamp"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Hitmonlee",command=lambda: pokeinfo("Hitmonlee"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Hitmonchan",command=lambda: pokeinfo("Hitmonchan"))
    elif (type_pokemon=="Flying"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Charizard",command=lambda: pokeinfo("Charizard"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Butterfree",command=lambda: pokeinfo("Butterfree"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Pidgey",command=lambda: pokeinfo("Pidgey"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Pidgeotto",command=lambda: pokeinfo("Pidgeotto"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Pidgeot",command=lambda: pokeinfo("Pidgeot"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Spearow",command=lambda: pokeinfo("Spearow"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Fearow",command=lambda: pokeinfo("Fearow"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Zubat",command=lambda: pokeinfo("Zubat"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Golbat",command=lambda: pokeinfo("Golbat"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Farfetch'd",command=lambda: pokeinfo("Farfetch'd"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Doduo",command=lambda: pokeinfo("Doduo"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Dodrio",command=lambda: pokeinfo("Dodrio"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Scyther",command=lambda: pokeinfo("Scyther"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Gyarados",command=lambda: pokeinfo("Gyarados"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Aerodactyl",command=lambda: pokeinfo("Aerodactyl"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Articuno",command=lambda: pokeinfo("Articuno"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Zapdos",command=lambda: pokeinfo("Zapdos"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Moltres",command=lambda: pokeinfo("Moltres"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Dragonite",command=lambda: pokeinfo("Dragonite"))
    elif (type_pokemon=="Ground"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Sandshrew",command=lambda: pokeinfo("Sandshrew"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Sandslash",command=lambda: pokeinfo("Sandslash"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Nidoqueen",command=lambda: pokeinfo("Nidoqueen"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Nidoking",command=lambda: pokeinfo("NNidoking"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Diglett",command=lambda: pokeinfo("Diglett"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Dugtrio",command=lambda: pokeinfo("Dugtrio"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Geodude",command=lambda: pokeinfo("Geodude"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Graveler",command=lambda: pokeinfo("Graveler"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Golem",command=lambda: pokeinfo("Golem"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Onix",command=lambda: pokeinfo("Onix"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Cubone",command=lambda: pokeinfo("Cubone"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Marowak",command=lambda: pokeinfo("Marowak"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Rhyhorn",command=lambda: pokeinfo("Rhyhorn"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Rhydon",command=lambda: pokeinfo("Rhydon"))
    elif (type_pokemon=="Rock"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Geodude",command=lambda: pokeinfo("Geodude"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Graveler",command=lambda: pokeinfo("Graveler"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Golem",command=lambda: pokeinfo("Golem"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Onix",command=lambda: pokeinfo("Onix"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Rhyhorn",command=lambda: pokeinfo("Rhyhorn"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Rhydon",command=lambda: pokeinfo("Rhydon"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Omanyte",command=lambda: pokeinfo("Omanyte"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Omastar",command=lambda: pokeinfo("Omastar"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Kabuto",command=lambda: pokeinfo("Kabuto"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Kabutops",command=lambda: pokeinfo("Kabutops"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Aerodactyl",command=lambda: pokeinfo("Aerodactyl"))
    elif (type_pokemon=="Ice"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Dewgong",command=lambda: pokeinfo("Dewgong"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Cloyster",command=lambda: pokeinfo("Cloyster"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Jynx",command=lambda: pokeinfo("Jynx"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Lapras",command=lambda: pokeinfo("Lapras"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Articuno",command=lambda: pokeinfo("Articuno"))
    elif (type_pokemon=="Ghost"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Gastly",command=lambda: pokeinfo("Gastly"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Haunter",command=lambda: pokeinfo("Haunter"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Gengar",command=lambda: pokeinfo("Gengar"))
    elif (type_pokemon=="Steel"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Magnemite",command=lambda: pokeinfo("Magnemite"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Magneton",command=lambda: pokeinfo("Magneton"))
    elif (type_pokemon=="Dragon"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Dratini",command=lambda: pokeinfo("Dratini"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Dragonair",command=lambda: pokeinfo("Dragonair"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Dragonite",command=lambda: pokeinfo("Dragonite"))
    my_pokemon.grid(row=1,column=3)
    my_btn_forward = Button(top1,text=">>",command=lambda: forward(image_number+1,list,type_pokemon))
    my_btn_backward = Button(top1,text="<<",command=lambda: backward(image_number-1,list,type_pokemon))
    if (image_number==len(list)):
        my_btn_forward = Button(top1,text=">>",state=DISABLED)
    MyLabel1 = Label(top1,image=myImg1)
    my_btn_forward.grid(row=1,column=2)
    my_btn_backward.grid(row=1,column=0)
    MyLabel1.grid(row=0,column=0,columnspan=3)
def backward(image_number,list,type_pokemon):
    global top1
    global MyLabel1
    global my_btn_forward
    global my_btn_backward
    global my_pokemon

    MyLabel1.grid_forget()
    my_pokemon.grid_forget()
    myImg1 = list[image_number-1]
    if (type_pokemon=="Grass"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo("Bulbasaur",1,"Grass",list))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Ivysaur",command=lambda: pokeinfo("Ivysaur"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Venasaur",command=lambda: pokeinfo("Venasaur"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Oddish",command=lambda: pokeinfo("Oddish"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Gloom",command=lambda: pokeinfo("Gloom"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Vileplume",command=lambda: pokeinfo("Vileplume"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Paras",command=lambda: pokeinfo("Paras"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Parasect",command=lambda: pokeinfo("Parasect"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Bellsprout",command=lambda: pokeinfo("Bellsprout"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Weepinbell",command=lambda: pokeinfo("Weepinbell"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Victreebell",command=lambda: pokeinfo("Victreebell"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Exeggcute",command=lambda: pokeinfo("Exeggcute"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Exeggutor",command=lambda: pokeinfo("Exeggutor"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Tangela",command=lambda: pokeinfo("Tangela"))
    elif (type_pokemon=="Fire"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Charmander",command=lambda: pokeinfo("Charmander"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Charmeleon",command=lambda: pokeinfo("Charmeleon"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Charizard",command=lambda: pokeinfo("Charizard"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Vulpix",command=lambda: pokeinfo("Vulpix"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Ninetales",command=lambda: pokeinfo("Ninetales"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Growlithe",command=lambda: pokeinfo("Growlithe"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Arcanine",command=lambda: pokeinfo("Arcanine"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Ponyta",command=lambda: pokeinfo("Ponyta"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Rapidash",command=lambda: pokeinfo("Rapidash"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Magmar",command=lambda: pokeinfo("Magmar"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Flareon",command=lambda: pokeinfo("Flareon"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Moltres",command=lambda: pokeinfo("Moltres"))
    elif (type_pokemon=="Water"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Squirtle",command=lambda: pokeinfo("Squirtle"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Wartortle",command=lambda: pokeinfo("Wartortle"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Blastoise",command=lambda: pokeinfo("Blastoise"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Psyduck",command=lambda: pokeinfo("Psyduck"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Golduck",command=lambda: pokeinfo("Golduck"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Poliwag",command=lambda: pokeinfo("Poliwag"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Poliwhirl",command=lambda: pokeinfo("Poliwhirl"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Poliwrath",command=lambda: pokeinfo("Poliwrath"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Tentacool",command=lambda: pokeinfo("Tentacool"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Tentacruel",command=lambda: pokeinfo("Tentacruel"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Slowpoke",command=lambda: pokeinfo("Slowpoke"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Slowbro",command=lambda: pokeinfo("Slowbro"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Seel",command=lambda: pokeinfo("Seel"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Dewgong",command=lambda: pokeinfo("Dewgong"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Shellder",command=lambda: pokeinfo("Shelldar"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Cloyster",command=lambda: pokeinfo("Cloyster"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Krabby",command=lambda: pokeinfo("Krabby"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Kingler",command=lambda: pokeinfo("Kingler"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Horsea",command=lambda: pokeinfo("Horsea"))
        elif (image_number==20):
            my_pokemon = Button(top1,text="Seadra",command=lambda: pokeinfo("Seadra"))
        elif (image_number==21):
            my_pokemon = Button(top1,text="Goldeen",command=lambda: pokeinfo("Goldeen"))
        elif (image_number==22):
            my_pokemon = Button(top1,text="Seaking",command=lambda: pokeinfo("Seaking"))
        elif (image_number==23):
            my_pokemon = Button(top1,text="Staryu",command=lambda: pokeinfo("Staryu"))
        elif (image_number==24):
            my_pokemon = Button(top1,text="Starmie",command=lambda: pokeinfo("Starmie"))
        elif (image_number==25):
            my_pokemon = Button(top1,text="Magikarp",command=lambda: pokeinfo("Magikarp"))
        elif (image_number==26):
            my_pokemon = Button(top1,text="Gyarados",command=lambda: pokeinfo("Gyarados"))
        elif (image_number==27):
            my_pokemon = Button(top1,text="Lapras",command=lambda: pokeinfo("Lapras"))
        elif (image_number==28):
            my_pokemon = Button(top1,text="Vaporeon",command=lambda: pokeinfo("Vaporeon"))
        elif (image_number==29):
            my_pokemon = Button(top1,text="Omanyte",command=lambda: pokeinfo("Omanyte"))
        elif (image_number==30):
            my_pokemon = Button(top1,text="Omastar",command=lambda: pokeinfo("Omastar"))
        elif (image_number==31):
            my_pokemon = Button(top1,text="Kabuto",command=lambda: pokeinfo("Kabuto"))
        elif (image_number==32):
            my_pokemon = Button(top1,text="Kabutops",command=lambda: pokeinfo("Kabutops"))
    elif (type_pokemon=="Electric"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Pikachu",command=lambda: pokeinfo("Pikachu"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Raichu",command=lambda: pokeinfo("Raichu"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Magnemite",command=lambda: pokeinfo("Magnemite"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Magneton",command=lambda: pokeinfo("Magneton"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Voltorb",command=lambda: pokeinfo("Voltorb"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Electrode",command=lambda: pokeinfo("Electrode"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Electabuzz",command=lambda: pokeinfo("Electabuzz"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Jolteon",command=lambda: pokeinfo("Jolteon"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Zapdos",command=lambda: pokeinfo("Zapdos"))
    elif (type_pokemon=="Poison"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo("Bulbasaur"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Ivysaur",command=lambda: pokeinfo("Ivysaur"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Venasaur",command=lambda: pokeinfo("Venasaur"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Weedle",command=lambda: pokeinfo("Weedle"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Kakuna",command=lambda: pokeinfo("Kakuna"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Beedrill",command=lambda: pokeinfo("Beedrill"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Ekans",command=lambda: pokeinfo("Ekans"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Arbok",command=lambda: pokeinfo("Arbok"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Nidoran_f",command=lambda: pokeinfo("Nidoran_f"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Nidorina",command=lambda: pokeinfo("Nidorina"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Nidoqueen",command=lambda: pokeinfo("Nidoqueen"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Nidoran_m",command=lambda: pokeinfo("Nidoran_m"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Nidorino",command=lambda: pokeinfo("Nidorino"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Nidoking",command=lambda: pokeinfo("Nidoking"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Zubat",command=lambda: pokeinfo("Zubat"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Golbat",command=lambda: pokeinfo("Golbat"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Oddish",command=lambda: pokeinfo("Oddish"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Gloom",command=lambda: pokeinfo("Gloom"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Vileplume",command=lambda: pokeinfo("Vileplume"))
        elif (image_number==20):
            my_pokemon = Button(top1,text="Venonat",command=lambda: pokeinfo("Venonat"))
        elif (image_number==21):
            my_pokemon = Button(top1,text="Venomoth",command=lambda: pokeinfo("Venomoth"))
        elif (image_number==22):
            my_pokemon = Button(top1,text="Bellsprout",command=lambda: pokeinfo("Bellsprout"))
        elif (image_number==23):
            my_pokemon = Button(top1,text="Weepinbell",command=lambda: pokeinfo("Weepinbell"))
        elif (image_number==24):
            my_pokemon = Button(top1,text="Victreebell",command=lambda: pokeinfo("Victreebell"))
        elif (image_number==25):
            my_pokemon = Button(top1,text="Grimer",command=lambda: pokeinfo("Grimer"))
        elif (image_number==26):
            my_pokemon = Button(top1,text="Muk",command=lambda: pokeinfo("Muk"))
        elif (image_number==27):
            my_pokemon = Button(top1,text="Gastly",command=lambda: pokeinfo("Gastly"))
        elif (image_number==28):
            my_pokemon = Button(top1,text="Haunter",command=lambda: pokeinfo("Haunter"))
        elif (image_number==29):
            my_pokemon = Button(top1,text="Gengar",command=lambda: pokeinfo("Gengar"))
        elif (image_number==30):
            my_pokemon = Button(top1,text="Koffing",command=lambda: pokeinfo("Koffing"))
        elif (image_number==31):
            my_pokemon = Button(top1,text="Weezing",command=lambda: pokeinfo("Weezing"))
    elif (type_pokemon=="Bug"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Caterpie",command=lambda: pokeinfo("Caterpie"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Metapod",command=lambda: pokeinfo("Metapod"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Butterfree",command=lambda: pokeinfo("Butterfree"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Weedle",command=lambda: pokeinfo("Weedle"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Kakuna",command=lambda: pokeinfo("Kakuna"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Beedrill",command=lambda: pokeinfo("Beedrill"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Paras",command=lambda: pokeinfo("Paras"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Parasect",command=lambda: pokeinfo("Parasect"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Venonat",command=lambda: pokeinfo("Venonat"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Venomoth",command=lambda: pokeinfo("Venomoth"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Scyther",command=lambda: pokeinfo("Scyhther"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Pinsir",command=lambda: pokeinfo("Pinsir"))
    elif (type_pokemon=="Psychic"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Abra",command=lambda: pokeinfo("Abra"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Kadabra",command=lambda: pokeinfo("Kadabra"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Alakazam",command=lambda: pokeinfo("Alakazam"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Slowpoke",command=lambda: pokeinfo("Slowpoke"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Slowbro",command=lambda: pokeinfo("Slowbro"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Drowzee",command=lambda: pokeinfo("Drowzee"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Hypno",command=lambda: pokeinfo("Hypno"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Exeggcute",command=lambda: pokeinfo("Exeggcute"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Exeggutor",command=lambda: pokeinfo("Exeggutor"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Mr. Mime",command=lambda: pokeinfo("Mr. Mime"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Jynx",command=lambda: pokeinfo("Jynx"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Mewtwo",command=lambda: pokeinfo("Mewtwo"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Mew",command=lambda: pokeinfo("Mew"))
    elif (type_pokemon=="Normal"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Pidgey",command=lambda: pokeinfo("Pidgey"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Pidgeotto",command=lambda: pokeinfo("Pidgeotto"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Pidgeot",command=lambda: pokeinfo("Pidgeot"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Rattata",command=lambda: pokeinfo("Rattata"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Raticate",command=lambda: pokeinfo("Raticate"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Spearow",command=lambda: pokeinfo("Spearow"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Fearow",command=lambda: pokeinfo("Fearow"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Jigglypuff",command=lambda: pokeinfo("Jigglypuff"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Wigglytuff",command=lambda: pokeinfo("Wigglytuff"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Meowth",command=lambda: pokeinfo("Meowth"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Persian",command=lambda: pokeinfo("Persian"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Farfetch'd",command=lambda: pokeinfo("Farfetch'd"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Doduo",command=lambda: pokeinfo("Doduo"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Dodrio",command=lambda: pokeinfo("Dodrio"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Lickitung",command=lambda: pokeinfo("Lickitung"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Chansey",command=lambda: pokeinfo("Chansey"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Kangaskhan",command=lambda: pokeinfo("Kangaskhan"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Tauros",command=lambda: pokeinfo("Tauros"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Ditto",command=lambda: pokeinfo("Ditto"))
        elif (image_number==20):
            my_pokemon = Button(top1,text="Eevee",command=lambda: pokeinfo("Eevee"))
        elif (image_number==21):
            my_pokemon = Button(top1,text="Porygon",command=lambda: pokeinfo("Porygon"))
        elif (image_number==22):
            my_pokemon = Button(top1,text="Snorlax",command=lambda: pokeinfo("Snorlax"))
    elif (type_pokemon=="Fighting"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Mankey",command=lambda: pokeinfo("Mankey"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Primeape",command=lambda: pokeinfo("Primeape"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Poliwrath",command=lambda: pokeinfo("Poliwrath"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Machop",command=lambda: pokeinfo("Machop"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Machoke",command=lambda: pokeinfo("Machoke"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Machamp",command=lambda: pokeinfo("Machamp"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Hitmonlee",command=lambda: pokeinfo("Hitmonlee"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Hitmonchan",command=lambda: pokeinfo("Hitmonchan"))
    elif (type_pokemon=="Flying"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Charizard",command=lambda: pokeinfo("Charizard"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Butterfree",command=lambda: pokeinfo("Butterfree"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Pidgey",command=lambda: pokeinfo("Pidgey"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Pidgeotto",command=lambda: pokeinfo("Pidgeotto"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Pidgeot",command=lambda: pokeinfo("Pidgeot"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Spearow",command=lambda: pokeinfo("Spearow"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Fearow",command=lambda: pokeinfo("Fearow"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Zubat",command=lambda: pokeinfo("Zubat"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Golbat",command=lambda: pokeinfo("Golbat"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Farfetch'd",command=lambda: pokeinfo("Farfetch'd"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Doduo",command=lambda: pokeinfo("Doduo"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Dodrio",command=lambda: pokeinfo("Dodrio"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Scyther",command=lambda: pokeinfo("Scyther"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Gyarados",command=lambda: pokeinfo("Gyarados"))
        elif (image_number==15):
            my_pokemon = Button(top1,text="Aerodactyl",command=lambda: pokeinfo("Aerodactyl"))
        elif (image_number==16):
            my_pokemon = Button(top1,text="Articuno",command=lambda: pokeinfo("Articuno"))
        elif (image_number==17):
            my_pokemon = Button(top1,text="Zapdos",command=lambda: pokeinfo("Zapdos"))
        elif (image_number==18):
            my_pokemon = Button(top1,text="Moltres",command=lambda: pokeinfo("Moltres"))
        elif (image_number==19):
            my_pokemon = Button(top1,text="Dragonite",command=lambda: pokeinfo("Dragonite"))
    elif (type_pokemon=="Ground"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Sandshrew",command=lambda: pokeinfo("Sandshrew"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Sandslash",command=lambda: pokeinfo("Sandslash"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Nidoqueen",command=lambda: pokeinfo("Nidoqueen"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Nidoking",command=lambda: pokeinfo("NNidoking"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Diglett",command=lambda: pokeinfo("Diglett"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Dugtrio",command=lambda: pokeinfo("Dugtrio"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Geodude",command=lambda: pokeinfo("Geodude"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Graveler",command=lambda: pokeinfo("Graveler"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Golem",command=lambda: pokeinfo("Golem"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Onix",command=lambda: pokeinfo("Onix"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Cubone",command=lambda: pokeinfo("Cubone"))
        elif (image_number==12):
            my_pokemon = Button(top1,text="Marowak",command=lambda: pokeinfo("Marowak"))
        elif (image_number==13):
            my_pokemon = Button(top1,text="Rhyhorn",command=lambda: pokeinfo("Rhyhorn"))
        elif (image_number==14):
            my_pokemon = Button(top1,text="Rhydon",command=lambda: pokeinfo("Rhydon"))
    elif (type_pokemon=="Rock"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Geodude",command=lambda: pokeinfo("Geodude"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Graveler",command=lambda: pokeinfo("Graveler"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Golem",command=lambda: pokeinfo("Golem"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Onix",command=lambda: pokeinfo("Onix"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Rhyhorn",command=lambda: pokeinfo("Rhyhorn"))
        elif (image_number==6):
            my_pokemon = Button(top1,text="Rhydon",command=lambda: pokeinfo("Rhydon"))
        elif (image_number==7):
            my_pokemon = Button(top1,text="Omanyte",command=lambda: pokeinfo("Omanyte"))
        elif (image_number==8):
            my_pokemon = Button(top1,text="Omastar",command=lambda: pokeinfo("Omastar"))
        elif (image_number==9):
            my_pokemon = Button(top1,text="Kabuto",command=lambda: pokeinfo("Kabuto"))
        elif (image_number==10):
            my_pokemon = Button(top1,text="Kabutops",command=lambda: pokeinfo("Kabutops"))
        elif (image_number==11):
            my_pokemon = Button(top1,text="Aerodactyl",command=lambda: pokeinfo("Aerodactyl"))
    elif (type_pokemon=="Ice"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Dewgong",command=lambda: pokeinfo("Dewgong"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Cloyster",command=lambda: pokeinfo("Cloyster"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Jynx",command=lambda: pokeinfo("Jynx"))
        elif (image_number==4):
            my_pokemon = Button(top1,text="Lapras",command=lambda: pokeinfo("Lapras"))
        elif (image_number==5):
            my_pokemon = Button(top1,text="Articuno",command=lambda: pokeinfo("Articuno"))
    elif (type_pokemon=="Ghost"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Gastly",command=lambda: pokeinfo("Gastly"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Haunter",command=lambda: pokeinfo("Haunter"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Gengar",command=lambda: pokeinfo("Gengar"))
    elif (type_pokemon=="Steel"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Magnemite",command=lambda: pokeinfo("Magnemite"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Magneton",command=lambda: pokeinfo("Magneton"))
    elif (type_pokemon=="Dragon"):
        if (image_number==1):
            my_pokemon = Button(top1,text="Dratini",command=lambda: pokeinfo("Dratini"))
        elif (image_number==2):
            my_pokemon = Button(top1,text="Dragonair",command=lambda: pokeinfo("Dragonair"))
        elif (image_number==3):
            my_pokemon = Button(top1,text="Dragonite",command=lambda: pokeinfo("Dragonite"))
    my_pokemon.grid(row=1,column=3) 
    my_btn_forward = Button(top1,text=">>",command=lambda: forward(image_number+1,list,type_pokemon))
    my_btn_backward = Button(top1,text="<<",command=lambda: backward(image_number-1,list,type_pokemon))
    if (image_number==1):
        my_btn_backward = Button(top1,text="<<",state=DISABLED)
    MyLabel1 = Label(top1,image=myImg1)
    my_btn_forward.grid(row=1,column=2)
    my_btn_backward.grid(row=1,column=0)
    MyLabel1.grid(row=0,column=0,columnspan=3)
def clicked():
    if (pokemon.get()=="Grass"):
        global myImg1
        global top1
        global my_btn_backward
        global my_btn_forward
        global my_btn_quit
        global MyLabel1
        global my_Images_grass
        global my_pokemon

        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/001_Bulbasaur.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/002_Ivysaur.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/003_Venasaur.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/043_Oddish.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/044_Gloom.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/045_Vileplume.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/046_Paras.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/047_Parasect.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/69_Bellsprout.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/70_Weepinbell.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/71_Victreebell.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/103_Exeggcute.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/104_Exeggutor.png"))
        myImg14 = ImageTk.PhotoImage(Image.open("Pokemon/Grass/114_Tangela.png"))
        my_Images_grass = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8
                           ,myImg9,myImg10,myImg11,myImg12,myImg13,myImg14]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_grass,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_grass,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo("Bulbasaur",1,"Grass",my_Images_grass))
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Fire"):
        global my_Images_fire
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/4_Charmander.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/5_Charmeleon.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/6_Charizard.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/37_Vulpix.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/38_Ninetales.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/58_Growlithe.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/59_Arcanine.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/77_Ponyta.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/78_Rapidash.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/126_Magmar.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/136_Flareon.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Fire/146_Moltres.png"))
        my_Images_fire = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8
                           ,myImg9,myImg10,myImg11,myImg12]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_fire,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_fire,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Charmander",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Water"):
        global my_Images_water
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Water/7_Squirtle.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Water/8_Wartortle.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Water/9_Blastoise.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Water/54_Psyduck.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Water/55_Golduck.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Water/60_Poliwag.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Water/61_Poliwhirl.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Water/62_Poliwrath.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Water/72_Tentacool.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Water/73_Tentacruel.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Water/79_Slowpoke.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Water/80_Slowbro.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Water/86_Seel.png"))
        myImg14 = ImageTk.PhotoImage(Image.open("Pokemon/Water/87_Dewgong.png"))
        myImg15 = ImageTk.PhotoImage(Image.open("Pokemon/Water/90_Shellder.png"))
        myImg16 = ImageTk.PhotoImage(Image.open("Pokemon/Water/91_Cloyster.png"))
        myImg17 = ImageTk.PhotoImage(Image.open("Pokemon/Water/98_Krabby.png"))
        myImg18 = ImageTk.PhotoImage(Image.open("Pokemon/Water/99_Kingler.png"))
        myImg19 = ImageTk.PhotoImage(Image.open("Pokemon/Water/116_Horsea.png"))
        myImg20 = ImageTk.PhotoImage(Image.open("Pokemon/Water/117_Seadra.png"))
        myImg21 = ImageTk.PhotoImage(Image.open("Pokemon/Water/118_Goldeen.png"))
        myImg22 = ImageTk.PhotoImage(Image.open("Pokemon/Water/119_Seaking.png"))
        myImg23 = ImageTk.PhotoImage(Image.open("Pokemon/Water/120_Staryu.png"))
        myImg24 = ImageTk.PhotoImage(Image.open("Pokemon/Water/121_Starmie.png"))
        myImg25 = ImageTk.PhotoImage(Image.open("Pokemon/Water/129_Magikarp.png"))
        myImg26 = ImageTk.PhotoImage(Image.open("Pokemon/Water/130_Gyarados.png"))
        myImg27 = ImageTk.PhotoImage(Image.open("Pokemon/Water/131_Lapras.png"))
        myImg28 = ImageTk.PhotoImage(Image.open("Pokemon/Water/134_Vaporeon.png"))
        myImg29 = ImageTk.PhotoImage(Image.open("Pokemon/Water/138_Omanyte.png"))
        myImg30 = ImageTk.PhotoImage(Image.open("Pokemon/Water/139_Omastar.png"))
        myImg31 = ImageTk.PhotoImage(Image.open("Pokemon/Water/140_Kabuto.png"))
        myImg32 = ImageTk.PhotoImage(Image.open("Pokemon/Water/141_Kabutops.png"))
        my_Images_water = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8
                           ,myImg9,myImg10,myImg11,myImg12,myImg13,myImg14,myImg15,
                           myImg16,myImg17,myImg18,myImg19,myImg20,myImg21,myImg22,
                           myImg23,myImg24,myImg25,myImg26,myImg27,myImg28,myImg29,
                           myImg30,myImg31,myImg32]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_water,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_water,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Squirtle",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Electric"):
        global my_Images_electric
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/25_Pikachu.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/26_Raichu.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/81_Magnemite.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/82_Magneton.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/100_Voltorb.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/101_Electrode.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/125_Electabuzz.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/135_Jolteon.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/145_Zapdos.png"))
        my_Images_electric = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,myImg9]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_electric,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_electric,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Pikachu",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Poison"):
        global my_Images_poison
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/1_Bulbasaur.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/2_Ivysaur.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/3_Venasaur.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/13_Weedle.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/14_Kakuna.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/15_Beedrill.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/23_Ekans.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/24_Arbok.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/29_Nidoran_f.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/30_Nidorina.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/31_Nidoqueen.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/32_Nidoran_m.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/33_Nidorino.png"))
        myImg14 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/34_Nidoking.png"))
        myImg15 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/41_Zubat.png"))
        myImg16 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/42_Golbat.png"))
        myImg17 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/43_Oddish.png"))
        myImg18 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/44_Gloom.png"))
        myImg19 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/45_Vileplume.png"))
        myImg20 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/48_Venonat.png"))
        myImg21 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/49_Venomoth.png"))
        myImg22 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/69_Bellsprout.png"))
        myImg23 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/70_Weepinbell.png"))
        myImg24 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/71_Victreebell.png"))
        myImg25 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/88_Grimer.png"))
        myImg26 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/89_Muk.png"))
        myImg27 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/92_Gastly.png"))
        myImg28 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/93_Haunter.png"))
        myImg29 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/94_Gengar.png"))
        myImg30 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/109_Koffing.png"))
        myImg31 = ImageTk.PhotoImage(Image.open("Pokemon/Poison/110_Weezing.png"))
        my_Images_poison = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8
                           ,myImg9,myImg10,myImg11,myImg12,myImg13,myImg14,myImg15,
                           myImg16,myImg17,myImg18,myImg19,myImg20,myImg21,myImg22,
                           myImg23,myImg24,myImg25,myImg26,myImg27,myImg28,myImg29,
                           myImg30,myImg31]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_poison,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_poison,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Bulbasaur",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Bug"):
        global my_Images_bug
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/10_Caterpie.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/11_Metapod.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/12_Butterfree.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/13_Weedle.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/14_Kakuna.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/15_Beedrill.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/46_Paras.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/47_Parasect.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/48_Venonat.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/49_Venomoth.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/123_Scyther.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Bug/127_Pinsir.png"))
        my_Images_bug = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,
                         myImg9,myImg10,myImg11,myImg12]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_bug,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_bug,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Caterpie",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Psychic"):
        global my_Images_psychic
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/63_Abra.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/64_Kadabra.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/65_Alakazam.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/79_Slowpoke.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/80_Slowbro.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/96_Drowzee.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/97_Hypno.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/102_Exeggcute.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/103_Exeggutor.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/122_Mr. Mime.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/124_Jynx.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/150_Mewtwo.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Psychic/151_Mew.png"))
        my_Images_psychic = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,
                         myImg9,myImg10,myImg11,myImg12,myImg13]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_psychic,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_psychic,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Abra",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Normal"):
        global my_Images_normal
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/016_Pidgey.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/017_Pidgeotto.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/018_Pidgeot.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/019_Rattata.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/020_Raticate.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/021_Spearow.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/022_Fearow.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/039_Jigglypuff.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/040_Wigglytuff.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/052_Meowth.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/053_Persian.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/083_Farfetch'd.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/084_Doduo.png"))
        myImg14 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/085_Dodrio.png"))
        myImg15 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/108_Lickitung.png"))
        myImg16 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/113_Chansey.png"))
        myImg17 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/115_Kangaskhan.png"))
        myImg18 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/128_Tauros.png"))
        myImg19 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/132_Ditto.png"))
        myImg20 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/133_Eevee.png"))
        myImg21 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/137_Porygon.png"))
        myImg22 = ImageTk.PhotoImage(Image.open("Pokemon/Normal/143_Snorlax.png"))
        my_Images_normal = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,
                         myImg9,myImg10,myImg11,myImg12,myImg13,myImg14,myImg15,myImg16
                         ,myImg17,myImg18,myImg19,myImg20,myImg21,myImg22]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_normal,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_normal,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Pidgey",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Fighting"):
        global my_Images_fighting
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/056_Mankey.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/057_Primeape.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/62_Poliwrath.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/066_Machop.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/067_Machoke.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/068_Machamp.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/106_Hitmonlee.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Fighting/107_Hitmonchan.png"))
        my_Images_fighting = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_fighting,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_fighting,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Mankey",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Flying"):
        global my_Images_flying
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/6_Charizard.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/12_Butterfree.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/016_Pidgey.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/017_Pidgeotto.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/018_Pidgeot.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/021_Spearow.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/022_Fearow.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/41_Zubat.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/42_Golbat.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/083_Farfetch'd.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/084_Doduo.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/085_Dodrio.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/123_Scyther.png"))
        myImg14 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/130_Gyarados.png"))
        myImg15 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/142_Aerodactyl.png"))
        myImg16 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/144_Articuno.png"))
        myImg17 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/145_Zapdos.png"))
        myImg18 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/146_Moltres.png"))
        myImg19 = ImageTk.PhotoImage(Image.open("Pokemon/Flying/149_Dragonite.png"))
        my_Images_flying = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,
                         myImg9,myImg10,myImg11,myImg12,myImg13,myImg14,myImg15,myImg16
                         ,myImg17,myImg18,myImg19]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_flying,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_flying,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        my_pokemon = Button(top1,text="Charizard",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Ghost"):
        global my_Images_ghost
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Ghost/92_Gastly.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Ghost/93_Haunter.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Ghost/94_Gengar.png"))
        my_Images_ghost = [myImg1,myImg2,myImg3]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_ghost,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_ghost,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Gastly",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Ice"):
        global my_Images_ice
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Ice/87_Dewgong.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Ice/91_Cloyster.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Ice/124_Jynx.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Ice/131_Lapras.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Ice/144_Articuno.png"))
        my_Images_ice = [myImg1,myImg2,myImg3,myImg4,myImg5]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_ice,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_ice,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Dewgong",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Ground"):
        global my_Images_ground
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/027_Sandshrew.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/028_Sandslash.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/31_Nidoqueen.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/34_Nidoking.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/050_Diglett.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/051_Dugtrio.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/074_Geodude.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/075_Graveler.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/076_Golem.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/095_Onix.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/104_Cubone.png"))
        myImg12 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/105_Marowak.png"))
        myImg13 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/111_Rhyhorn.png"))
        myImg14 = ImageTk.PhotoImage(Image.open("Pokemon/Ground/112_Rhydon.png"))
        my_Images_ground = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,
                         myImg9,myImg10,myImg11,myImg12,myImg13,myImg14]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_ground,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_ground,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Sandshrew",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Rock"):
        global my_Images_rock
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/074_Geodude.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/075_Graveler.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/076_Golem.png"))
        myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/095_Onix.png"))
        myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/111_Rhyhorn.png"))
        myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/112_Rhydon.png"))
        myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/138_Omanyte.png"))
        myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/139_Omastar.png"))
        myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/140_Kabuto.png"))
        myImg10 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/141_Kabutops.png"))
        myImg11 = ImageTk.PhotoImage(Image.open("Pokemon/Rock/142_Aerodactyl.png"))
        my_Images_rock = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7,myImg8,
                         myImg9,myImg10,myImg11]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_rock,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_rock,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Geodude",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Steel"):
        global my_Images_steel
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Steel/81_Magnemite.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Steel/82_Magneton.png"))
        my_Images_steel = [myImg1,myImg2]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_steel,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_steel,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Magnemite",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Dragon"):
        global my_Images_dragon
        top1 = Toplevel()
        top1.geometry("400x400")
        myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Dragon/147_Dratini.png"))
        myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Dragon/148_Dragonair.png"))
        myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Dragon/149_Dragonite.png"))
        my_Images_dragon = [myImg1,myImg2,myImg3]
        my_btn_forward = Button(top1,text=">>",command=lambda: forward(2,my_Images_dragon,pokemon.get()))
        my_btn_backward = Button(top1,text="<<",command=lambda: backward(2,my_Images_dragon,pokemon.get()),state=DISABLED)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_pokemon = Button(top1,text="Dratini",command=lambda: pokeinfo())
        my_pokemon.grid(row=1,column=3)
        my_btn_backward.grid(row=1,column=0)
        my_btn_forward.grid(row=1,column=2)
        my_btn_quit.grid(row=1,column=1)
        MyLabel1 = Label(top1,image=myImg1)
        MyLabel1.grid(row=0,column=0,columnspan=4)
    elif (pokemon.get()=="Dark"):
        top1 = Toplevel()
        top1.geometry("400x400")
        myLabel_limit = Label(top1,text="There are no Dark type pokemon available in Kanto region")
        myLabel_limit.grid(row=0,column=0,columnspan=3)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_btn_quit.grid(row=1,column=1)
    elif (pokemon.get()=="Fairy"):
        top1 = Toplevel()
        top1.geometry("400x400")
        my_Label_gen4 = Label(top1,text="Fairy type was introduced in Generation 4 so not displaying in this section")
        my_Label_gen4.grid(row=0,column=0,columnspan=3)
        my_btn_quit = Button(top1,text="Exit Program",command=top1.destroy)
        my_btn_quit.grid(row=1,column=1)
pokemon = StringVar()
pokemon.set("Normal")
for text,mode in TYPES:
    Radiobutton(root,text=text,variable=pokemon,value=mode).pack(anchor=W)
myButton = Button(root,text="Display Pokemon",command=clicked)
myButton.pack()
my_Button_quit_main = Button(root,text="Exit Program",command=root.quit)
my_Button_quit_main.pack()

root.mainloop()