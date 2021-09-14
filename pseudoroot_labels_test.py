# code source for drawing and loading the picture: https://github.com/amine0110/draw-on-an-image-tkinter/blob/main/main.py

#Just a little demo. For now if you want to try it out you'll want to have soem png's in the same directory as the script, as well as a png named 'Your_img.png'
#which will serve as the default. Then by clicking and dragging the mouse on the picture you can annotate an image. Then click upload, which will eventually
#trigger logic that uploads your annotated image to the cloud for machine learning

from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

app = Tk()
app.geometry("1500x1500")
app.title('Pseudoroot Annotate')


def get_x_and_y(event):
	global lasx, lasy
	lasx, lasy = event.x, event.y

def draw_smth(event):
	global lasx, lasy
	canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
	lasx, lasy = event.x, event.y
	
def draw_smth1(event,canvas):
	global lasx, lasy
	canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
	lasx, lasy = event.x, event.y
	
def uploadPopup(img_str):
	popup = Tk()
	popup.title('Thanks')
	str_label = Label(popup, text="Upload Complete", font=('bold', 25))
	str_label.pack()

def findPNG(list_box):
	png_s = [pth for pth in Path.cwd().iterdir() if pth.suffix == '.png']
	for png in png_s:
		list_box.insert(END, str(png).split('/')[-1])
	
def chooseImgPopup():
	popup = Tk()
	popup.title('Pseudoroot')
	str_label = Label(popup, text="Choose an Image:", font=('bold', 12))
	str_label.pack()
	listbox = Listbox(popup)
	listbox.config(width=60, height=3)
	listbox.pack()
	findPNG(listbox)
	select_button = Button(popup, text='Select Image', width=30,height=1,font=('bold', 8), command=lambda: reloadAnnotationSpace(listbox.get(ANCHOR),popup))
	select_button.pack()
	
def reloadAnnotationSpace(anchor,popup):
	global app
	popup.destroy()
	app.destroy()
	app = Tk()
	app.geometry("1500x1500")
	app.title('Pseudoroot Annotate')
	
	canvas = Canvas(app, bg='black')
	canvas.pack(anchor='nw', fill='both', expand=1)

	canvas.bind("<Button-1>", get_x_and_y)
	canvas.bind("<B1-Motion>", lambda eff: draw_smth1(eff, canvas))

	img_str = anchor
	image = Image.open(img_str)
	image = image.resize((1500,1500), Image.ANTIALIAS)
	image = ImageTk.PhotoImage(image)
	canvas.create_image(0,0, image=image, anchor='nw')
	choose_img_button = Button(canvas, text='Choose Image', width=30,height=1,font=('bold', 8), command=lambda: chooseImgPopup())
	choose_img_button.pack()
	upload_button = Button(canvas, text='Upload', width=30,height=1,font=('bold', 8), command=lambda: uploadPopup(img_str))
	upload_button.pack()


	app.mainloop()
	
	
    

canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

img_str = "Your_img.png"
image = Image.open(img_str)
image = image.resize((1500,1500), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
canvas.create_image(0,0, image=image, anchor='nw')
choose_img_button = Button(canvas, text='Choose Image', width=30,height=1,font=('bold', 8), command=lambda: chooseImgPopup())
choose_img_button.pack()
upload_button = Button(canvas, text='Upload', width=30,height=1,font=('bold', 8), command=lambda: uploadPopup(img_str))
upload_button.pack()


app.mainloop()





