#Importing libraries
from tkinter import *
from customtkinter import *
import customtkinter 
from pytube import YouTube
from tkinter import messagebox as msg


link = " " #creating a variable to store video's link
videoName = " " #creating a variable to store video's name
 #creating a variable to store video's stream



root = CTk () #creating the root window



#creatung function which creates the download tab
def downloadTab():
    global linkEntry , youtubeLogo , titleLabel , downloadButton , backButton , videoName , videoNameLabel , streams , quality
    blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", text_color="#242424")
    blank_label.place(x=190, y=440)
    youtubeLogo.destroy()
    downloadButton.destroy()
    linkEntry.destroy()
    titleLabel.destroy()
    titleLabel = CTkLabel(root, text="YouTube Video Downloader" , text_color="white" , font=("Times New Roman", 20, "bold") )
    titleLabel.place(x=135, y=20)
    youtubeLogoImage = PhotoImage(file="Elements\\youtube.png")
    youtubeLogo = CTkLabel(root, image=youtubeLogoImage , text = " ")
    youtubeLogo.place(x=119, y=40)
    videoNameLabel = CTkLabel(root, text = videoName  ,  text_color="white" , font=("Times New Roman", 15))
    videoNameLabel.place(x=35, y=250)
    stream = list(streams)
    quality = customtkinter.CTkOptionMenu(master = root , values = stream , width = 50  )
    quality.place(x=330, y=250)
    
    #creating function which back to the main tab
    def back():
        global  youtubeLogo , titleLabel ,videoNameLabel
        titleLabel.destroy()
        youtubeLogo.destroy()
        videoNameLabel.destroy()
        quality.destroy()
        mainTab()
        backButton.destroy()
    backButton = CTkButton(root, text="Back", font=("Times New Roman", 15, "bold") , width=50 , command=back)
    backButton.place(x=30, y=550)



#creating function which stores video's link and then redirects to the download tab
def Entry ():
    global link , linkEntry , videoName , streams 
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
        try :
            #blank_label = customtkinter.CTkLabel(root, text="please wait....", text_color="white")
            #blank_label.place(x=190, y=440)
            yt = YouTube(link)
            yt.streams.get_lowest_resolution()
            video = yt.streams.get_lowest_resolution()
            videoName = str(video.default_filename)
            streams = set()
            for stream in yt.streams.filter(type="video"):  # Only look for video streams to avoid None values
                streams.add(stream.resolution)
            downloadTab()  
        except:
            msg.showerror(title = "YouTube Video Downloader ", message = "An error occured (this may be caused due to bad internet connection or the video may be unavailable)")
               
       


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