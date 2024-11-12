
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter
from PIL import ImageTk,Image
import CartoonImage
import Filter
from Filter import *
from CartoonImage import *
import cv2
import PIL.Image, PIL.ImageTk

main = tkinter.Tk()
main.title("Cartooning Of An Image")
main.geometry("1000x500")
global image_file



def uploadImage():
    global image_file
    image_file = askopenfilename(initialdir = "images")
    datasetpath.config(text=image_file)
    #cv_img = cv2.cvtColor(cv2.imread(image_file), cv2.COLOR_BGR2RGB)
    #img = ImageTk.PhotoImage(Image.open(image_file))  
    #label.config(image=img)
    
def uploadVideo():
    wf = Filter()
    c = CartoonImage()
    videofile = askopenfilename(initialdir = "videos")
    video = cv2.VideoCapture(videofile)
    while(True):
        ret, frame = video.read()
        print(ret)
        if ret == True:
            #cartoon1 = wf.createCartoon(frame)
            #cartoon2 = c.createCartoon(cartoon1)
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img_gray = cv2.medianBlur(img_gray, 7)
            edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
            ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
            cartoon2 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            cv2.imshow('Cartoon Video', cartoon2)
            if cv2.waitKey(3) & 0xFF == ord('q'):
                break
        else:
                break
    video.release()
    cv2.destroyAllWindows()    
            
    
    
def createCartoon():
    img_rgb = cv2.imread(image_file)

    wf = Filter()
    cartoon1 = wf.createCartoon(img_rgb)
    cv2.imshow("cartoon1", cartoon1)
    cv2.imwrite("output/cartoon1.jpg",cartoon1)
        
    c = CartoonImage()
    cartoon2 = c.createCartoon(img_rgb)
    cv2.imwrite("output/cartoon2.jpg",cartoon2)
    cv2.imshow("cartoon2", cartoon2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

uploadbutton = Button(main, text="Upload Image", command=uploadImage)
uploadbutton.place(x=350,y=100)

videobutton = Button(main, text="Upload Video", command=uploadVideo)
videobutton.place(x=500,y=100)

datasetpath = Label(main)
datasetpath.place(x=350,y=150)

cartoonbutton = Button(main, text="Cartoonify An Image", command=createCartoon)
cartoonbutton.place(x=350,y=200)

img = ImageTk.PhotoImage(Image.open("title.jpg"))  
label = Label(main, image=img)
label.place(x=250,y=250)

main.config(bg='brown')
main.mainloop()
