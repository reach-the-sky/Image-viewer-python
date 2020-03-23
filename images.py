from tkinter import *
import os
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
root = Tk()
root.configure(bg="#FE642E")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
frame = LabelFrame(root,height = root.winfo_screenheight()-150,width = root.winfo_screenwidth()-50)
frame.grid(row=0,column=0,padx=10,pady=10,columnspan=5)
frame.grid_propagate(0)
root.title("Application to view images")
root.iconbitmap('bitmap.ico')
root.filename = filedialog.askopenfilename(initialdir="c:/",title= "open the image")
def filename_split_find(s):
    c = s.count("/")
    updated_s = []
    temp = 0
    for _ in s:
        if (_ == "/"):
            temp += 1
            if (temp == c):
                break
        updated_s.append(_)
    updated_s = "".join(updated_s)
    return updated_s
updated_s = filename_split_find(root.filename)
list_images = []
for _ in os.listdir(updated_s):
    if (".jpg" in _) or (".png" in _):
        list_images.append(updated_s + "/" + _)
n=0
def forward():
    global n,lab_img,img,list_images,max_size_of_image,status_label,frame
    n=(n+1)%(len(list_images))
    lab_img.grid_forget()
    status_label.grid_forget()
    status_label = Label(root, text="image " + str(n+1) +" of " + str(len(list_images)))
    status_label.grid(row=2, column=4)
    img1 = Image.open(list_images[n])
    width_image, height_image = img1.size
    size_of_image = size_of_image_fixer(width_image, height_image)
    img2 = img1.resize(size_of_image)
    img = ImageTk.PhotoImage(img2)
    lab_img = Label(frame,image=img,anchor = CENTER)
    lab_img.grid(row=0,column=0,columnspan=5)

def backward():
    global n,lab_img,img,list_images,max_size_of_image,status_label,frame
    n=(n-1)%(len(list_images))
    lab_img.grid_forget()
    status_label.grid_forget()
    status_label = Label(root, text="image " + str(n+1) +" of " + str(len(list_images)))
    status_label.grid(row=2, column=4)
    img1 = Image.open(list_images[n])
    width_image, height_image = img1.size
    size_of_image = size_of_image_fixer(width_image, height_image)
    img2 = img1.resize(size_of_image)
    img = ImageTk.PhotoImage(img2)
    lab_img = Label(frame,image=img,anchor = CENTER)
    lab_img.grid(row=0,column=0,columnspan=5)
def wquit():
    answer_of_question = messagebox.askquestion("Popup", "Are you sure you want to exit the program")
    if(answer_of_question == "yes"):
        root.quit()
def size_of_image_fixer(width,height):
    if(height > (root.winfo_screenheight()-155)):
        width = int((root.winfo_screenheight() - 155) * width / height)
        height = root.winfo_screenheight()-155
    if(width > (root.winfo_screenwidth()-45)):
        height = int((root.winfo_screenwidth()-45)*height/width)
        width = root.winfo_screenwidth()-45
    updated_size = (width,height)
    return updated_size

img1 = Image.open(list_images[0])
width_image,height_image = img1.size
size_of_image =  size_of_image_fixer(width_image,height_image)
img2 = img1.resize(size_of_image)
img = ImageTk.PhotoImage(img2)
lab_img = Label(frame,image=img,padx=100,pady=100,anchor="center")
lab_img.grid(row=0,column=2,columnspan=5)
status_label = Label(root, text = "image 1 of " + str(len(list_images)))
status_label.grid(row=2,column=4)
exit = ttk.Button(root,text= " Exit",command=wquit)
exit.grid(row=1,column=2)
next_img = ttk.Button(root,text = ">>",command=forward)
next_img.grid(row=1,column=3)
previous_img = ttk.Button(root,text = "<<",command=backward)
previous_img.grid(row=1,column=1)

root.mainloop()