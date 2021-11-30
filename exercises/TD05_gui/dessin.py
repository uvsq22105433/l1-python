import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600,600
root= tk.Tk()
root.title("TD5")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT,bg="black")
canvas.grid(row=1,column=1,rowspan=3)


def myfunction():
    print("bouton appuyé") 
button1= tk.Button(root,text="choisir une couleur",command= myfunction)
button1.grid(row=0,column=1)
button2=tk.Button(root,text="cercle",command=myfunction)
button2.grid(row=1,column=0)
button3= tk.Button(root,text="carré",command= myfunction)
button3.grid(row=2,column=0)
button4= tk.Button(root,text="croix",command= myfunction)
button4.grid(row=3, column=0)

root.mainloop()
