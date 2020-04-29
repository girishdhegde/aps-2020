import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import time
import pyautogui
import re
import pickle
import shutil

paath = StringVar()


def add_textentry(vble,ROW=0,COLUMN=0,ROWSPAN=1,COLUMNSPAN=1,PADX=0,PADY=0):
	x=(Entry(root,textvariable=vble))
	x.grid(row=ROW,column=COLUMN,rowspan=ROWSPAN,padx=PADX,pady=PADY)
	return x


def add_menu():

	menu=Menu(root)

	filemenu=Menu(menu,tearoff=0)

	filemenu.add_command(label="Load frames",command=load_frames)
	filemenu.add_command(label="Convert video",command=video_to_frame)


	filemenu.add_separator()

	filemenu.add_command(label="Exit",command=exitfun)

	menu.add_cascade(label='File',menu=filemenu)



	edit=Menu(menu,tearoff=0)

	#edit.add_command(label="Create folders",command=None)
	edit.add_command(label="Load table and create folder",command=None)
	edit.add_command(label="Speed up",command=increasevideospeed)
	edit.add_command(label="Slow down",command=deccreasevideospeed)

	

	menu.add_cascade(label='Annotation',menu=edit)

	hlp=Menu(menu,tearoff=0)

	menu.add_cascade(label='Help',menu=hlp)

	About=Menu(menu,tearoff=0)

	menu.add_cascade(label='About',menu=About)

	root.config(menu=menu)


def load_frames():

	global path,finalframe,s,classfile


	path = paath.get()

	items=[]


	if os.path.exists(path) :

		if full.get() :

			items = (os.listdir(path))


			finalframe = len(items) - 1
		
		else:


			finalframe = fframe.get()


			items = ((os.listdir(path))[:finalframe])

		for i in range(len(items)):

			l.insert(i,items[i])

		for i in range(finalframe+1):
			classfile.append(-1)

add_textentry(paath,1,0)
