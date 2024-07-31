from tkinter import *
from PIL import ImageTk,Image

root = Tk()

def information(number):
    top1 = Toplevel()
    if (number==5):
        myLab = Label(top1, text="Pokemon: Arceus")
        myLab.grid(row=0, column=0)
        myLabel = Label(top1, text="Information: It is the heavenly front which pours the light that shines across Hisui. Its luminance guides and protects all Pokemon. Hisuian mythology states that Arceus is the creator of the things")
        myLabel.grid(row=1, column=0)
        myLabel2 = Label(top1, text="Weakness: Fighting(x2)")
        myLabel2.grid(row=2, column=0)
    elif (number==4):
        myLab = Label(top1, text="Pokemon: Giratina")
        myLab.grid(row=0, column=0)
        myLabel = Label(top1, text="Information: There is one Hiusian verse that tells of a powerful light creating a deep shadow. I imagine that this deep shadow is Giratina.")
        myLabel.grid(row=1, column=0)
        myLabel2 = Label(top1, text="Weakness: Ghost(x2), Ice(x2), Dragon(x2), Dark(x2), Fairy(x2)")
        myLabel2.grid(row=2, column=0)
    elif (number==2):
        myLab = Label(top1, text="Pokemon: Dialga")
        myLab.grid(row=0, column=0)
        myLabel = Label(top1, text="Information: This Pokemon is revered as a deity in Hiusian legend. The birth of Dialga was what caused the vast river of time to begin flowing in our world.")
        myLabel.grid(row=1, column=0)
        myLabel2 = Label(top1, text="Weakness:  Fighting(x2), Ground(x2)")
        myLabel2.grid(row=2, column=0)
    elif (number==3):
        myLab = Label(top1, text="Pokemon: Palkia")
        myLab.grid(row=0, column=0)
        myLabel = Label(top1, text="Information: This Pokemon is feared as deity in Hiusian legend. The birth of Palkia was what caused the walls of our world to disappear, creating a sky that spans for infinity")
        myLabel.grid(row=1, column=0)
        myLabel2 = Label(top1, text="Weakness: Dragon(x2), Fairy(x2)")
        myLabel2.grid(row=2, column=0)
    elif (number==1):
        myLab = Label(top1, text="Pokemon: Rayquaza")
        myLab.grid(row=0, column=0)
        myLabel = Label(top1, text="Information: It lives in the ozone layer far above the clouds and cannot be seen from the ground")
        myLabel.grid(row=1, column=0)
        myLabel2 = Label(top1, text="Weakness: Rock(x2), Ice(x4), Dragon(x2), Fairy(x2)")
        myLabel2.grid(row=2, column=0)
    button_quit_new = Button(top1, text="Exit Window", command=top1.destroy)
    button_quit_new.grid(row=3, column=0)
def forward(image_number):
    global myLabel
    global button_backward
    global button_forward
    global button_info

    myLabel.grid_forget()
    button_info.grid_forget()
    myLabel = Label(image=myList[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    button_quit = Button(root, text="Exit Program", command=root.quit)
    if (image_number==1):
        button_info = Button(root, text="Rayquaza", command=lambda:information(1))
    elif (image_number==2):
        button_info = Button(root, text="Dialga", command=lambda:information(2))
    elif (image_number==3):
        button_info = Button(root, text="Palkia", command=lambda:information(3))
    elif (image_number==4):
        button_info = Button(root, text="Giratina", command=lambda:information(4))
    else:
        button_info = Button(root, text="Arceus", command=lambda:information(5))
    if (image_number==1):
        button_backward = Button(root, text="<<", command=lambda: backward(len(myList)))
    if (image_number==len(myList)):
        button_forward = Button(root, text=">>", command=lambda: forward(1))
    myLabel.grid(row=0, column=0, columnspan=4)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    button_info.grid(row=1, column=3)
def backward(image_number):
    global myLabel
    global button_backward
    global button_forward
    global button_info

    myLabel.grid_forget()
    button_info.grid_forget()
    myLabel = Label(image=myList[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    button_quit = Button(root, text="Exit Program", command=root.quit)
    if (image_number==1):
        button_info = Button(root, text="Rayquaza", command=lambda:information(1))
    elif (image_number==2):
        button_info = Button(root, text="Dialga", command=lambda:information(2))
    elif (image_number==3):
        button_info = Button(root, text="Palkia", command=lambda:information(3))
    elif (image_number==4):
        button_info = Button(root, text="Giratina", command=lambda:information(4))
    else:
        button_info = Button(root, text="Arceus", command=lambda:information(5))
    if (image_number==1):
        button_backward = Button(root, text="<<", command=lambda: backward(len(myList)))
    if (image_number==len(myList)):
        button_forward = Button(root, text=">>", command=lambda: forward(1))
    myLabel.grid(row=0, column=0, columnspan=4)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    button_info.grid(row=1, column=3)
root.title("Legendary Pokemon")
myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Legendary/384_Rayquaza.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Legendary/483_Dialga.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Legendary/484_Palkia.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Legendary/487_Giratina.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Legendary/493_Arceus.jpg"))

myLabel = Label(image=myImg1)
myList = [myImg1,myImg2,myImg3,myImg4,myImg5]

button_forward = Button(root, text=">>", command=lambda: forward(2))
button_backward = Button(root, text="<<", command=lambda: backward(len(myList)))
button_quit = Button(root, text="Exit Program", command=root.quit)
button_info = Button(root, text="Rayquaza", command=lambda: information(1))

myLabel.grid(row=0, column=0, columnspan=4)
button_backward.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
button_info.grid(row=1, column=3)
root.mainloop()