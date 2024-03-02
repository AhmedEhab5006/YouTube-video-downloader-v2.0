#Importing libraries
from tkinter import *
from customtkinter import *
import customtkinter 
from pytube import *


link = " " #creating a variable to store video's link

root = CTk () #creating the root window



#creatung function which creates the download tab
def downloadTab():
    global linkEntry , youtubeLogo , titleLabel , downloadButton , backButton
    blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", text_color="#242424")
    blank_label.place(x=190, y=440)
    youtubeLogo.destroy()
    downloadButton.destroy()
    linkEntry.destroy()
    titleLabel.destroy()
    
    
    
    #creating function which back to the main tab
    def back():
        mainTab()
        backButton.destroy()
    backButton = CTkButton(root, text="Back", font=("Times New Roman", 15, "bold") , width=50 , command=back)
    backButton.place(x=30, y=550)



#creating function which stores video's link and then redirects to the download tab
def Entry ():
    global link
    global linkEntry
    link = linkEntry.get()
    if link == "":
        errorLabel = CTkLabel(root, text = "Please enter a link" , text_color="red" , font=("Times New Roman", 17, "bold") )
        errorLabel.place(x=190, y=440)
    elif "www.youtube.com" not in link:
        blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", text_color="#242424")
        blank_label.place(x=190, y=440)
        errorLabel = CTkLabel(root, text = "Invalid link" , text_color="red" , font=("Times New Roman", 17, "bold") )
        errorLabel.place(x=218, y=440)
    else :
        downloadTab()    
       


#creating function which creates the main window of the app       
def mainTab (): 
        global linkEntry , youtubeLogo , titleLabel , downloadButton 
        youtubeLogoImage = PhotoImage(file="Elements\\youtube.png")
        youtubeLogo = customtkinter.CTkLabel(root , image=youtubeLogoImage , text = "" )
        youtubeLogo.place(x=120, y=150)
        titleLabel = customtkinter.CTkLabel(root , text="YouTube Video Downloader" , text_color="white" , font=("Times New Roman", 20, "bold") )
        titleLabel.place(x=136, y=130)
        linkEntry = customtkinter.CTkEntry(root , placeholder_text="Enter YouTube Video Link" , text_color="white" , font=("Times New Roman", 15, "bold") , width=400  )
        linkEntry.place(x=55, y=370)
        downloadButton = customtkinter.CTkButton(root , text="Download" , text_color="white" ,fg_color="green" , command = Entry , font=("Times New Roman", 15, "bold") , width=150 )
        downloadButton.place(x=187, y=490)
       



#customizing our root window        
root.title("YouTube Video Downloader")
root.geometry("500x600")
root.resizable(False, False)
customtkinter.set_appearance_mode("Dark")
customtkinter.deactivate_automatic_dpi_awareness()
root.iconbitmap("Elements\\icon.ico")
version = customtkinter.CTkLabel(root , text = "v1.0" , text_color="grey" , font=("Times New Roman", 10, "bold") )
version.place(x=480, y=580)
madeBy = customtkinter.CTkLabel(root , text = "Made by Ahmed Ehab" , text_color="grey" , font=("Times New Roman", 10, "bold") )
madeBy.place(x=400, y=560)
mainTab()
root.mainloop()