#Code adapted from code at"https://www.codespeedy.com/how-to-create-a-pdf-viewer-using-python/"

# Importing required modules
from tkinter import *
from PIL import Image,ImageTk
from pdf2image import convert_from_path
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pdf_file", required=True,
	help="PDF file name to open")
args = vars(ap.parse_args())


def handle_keypress(event):
	print("keypress")

def get_scroll_pos(event):
    a,b = scrollbar.get()
    print("A: " + str(a) + " B: " + str(b))

def pdf_viewer():
	# Creating Tk container
	tk = Tk()	
	#tk.wm_iconbitmap("icon.ico") # for an icon on the gui canvas
	tk.title("Gesture Control PDF Viewer")

	# initial_height of pdf
	img_width = 800
	img_height = 900

	# Creating the frame for PDF Viewer
	pdf_frame = Frame(master=tk)
	pdf_frame.pack(fill=BOTH,expand=True)

	# Adding Scrollbar to the PDF frame
	scrol_y = Scrollbar(master=pdf_frame,orient=VERTICAL)

	# Adding text widget for inserting images
	pdf = Text(master=pdf_frame, width=img_width, height=img_height, yscrollcommand=scrol_y.set,bg="grey")
	#pdf.configure(state="disabled") # does this eliminate ability for padding?

	# Setting the scrollbar to the right side
	scrol_y.pack(side=RIGHT,fill=Y)
	scrol_y.config(command=pdf.yview)

	# Finally packing the text widget
	pdf.pack(fill=BOTH, expand=True, padx=5, pady=5)


	# Here the PDF is converted to list of images
	pages = convert_from_path(args["pdf_file"],size=(800,900))

	# Empty list for storing images
	photos = []

	# Storing the converted images into list
	for i in range(len(pages)):
	    photos.append(ImageTk.PhotoImage(pages[i]))

	# Adding all the images to the text widget

	for photo in photos:
	    pdf.image_create(END,image=photo)
	  
	    # For Seperating the pages
	    pdf.insert(END,'\n\n')

	tk.bind("<Key>", handle_keypress)
	#tk.bind("<Scroll>", get_scroll_pos)
	tk.mainloop()

if __name__== "__main__":
	print(args["pdf_file"])
	pdf_viewer()