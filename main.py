#Importing libraries
from tkinter import *
from customtkinter import *
import customtkinter 
from pytube import YouTube
from tkinter import messagebox as msg
import os
from customtkinter import filedialog
import time
import threading



link = " " #creating a variable to store video's link
videoName = " " #creating a variable to store video's name
path = " " #creating a variable to store the path of the video





root = CTk () #creating the root window
setAudio = BooleanVar() #creating a variable to store whether the audio is set or not
isCanceled = False #creating a variable to store whether the download is canceled or not
completed = False #creating a variable to store whether the download is completed or not

def cancel ():
    global isCanceled , downloadButton , downloading , pauseButton , cancelButton , progressBar , backButton , audioOnly , quality , setAudio , completed
    isCanceled = True
    canceleingLabel = CTkLabel(root, text = "Cancelling..." , text_color="yellow" , font=("Times New Roman", 15, "bold") )
    canceleingLabel.place(x = 215, y = 360)
    if completed : 
        canceledLabel = CTkLabel(root, text = "Download Canceled!" , text_color="red" , font=("Times New Roman", 15, "bold") )
        canceledLabel.place(x = 190, y = 360)
    progressBar.set(0.0)
    downloading.destroy()
    #pauseButton.destroy()
    progressBar.destroy()
    #cancelButton.destroy()
    #downloadButton._state = NORMAL
    #downloadButton._fg_color = "green"
    #audioOnly._state = NORMAL
    #quality.configure(state = NORMAL)
    #backButton._fg_color = "#146F86"
    #backButton._state = NORMAL
    
#creating function which shows the progress of the download
def on_progress (stream , chunk , bytes_remaining) :
    global progressBar , video
    stream = video
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_comp = bytes_downloaded / total_size *100
    time.sleep(0.3)
    if progressBar :
        progressBar.set(float(percentage_of_comp)/100)
        root.update()
    


#creating the function which downloads the video
def Download ():
    global yt , quality , path , backButton , progressBar , downloading , video , done , downloadButton , audioOnly ,  temp_download_path
    
    
    #knowing if user chose to download audio or video
    if setAudio.get() == 0:
        try :
            video = yt.streams.filter(res = quality.get()).first()
            videoName = str(video.default_filename) 
        except :
            msg.showerror(title = "YouTube Video Downloader ", message = "An error occured (this may be caused due to bad internet connection)")    
        path = filedialog.asksaveasfilename(filetypes=[("Video", ".mp4")], confirmoverwrite=True,
                                        defaultextension=".mp4", title='Choose where to save video',
                                        initialfile=os.path.basename(os.path.abspath(videoName)))
    if setAudio.get() == 1:
        try :
            video = yt.streams.filter(only_audio = True).first()
            videoName = str(video.default_filename)
            temp_download_path = os.path.join(Path.home(), "Downloads", videoName)  
        except :
            msg.showerror(title = "YouTube Video Downloader ", message = "An error occured (this may be caused due to bad internet connection)")
        path = filedialog.asksaveasfilename(filetypes=[("Audio", ".mp3")], confirmoverwrite=True,
                                        defaultextension=".mp3", title='Choose where to save video',
                                         initialfile=os.path.splitext(os.path.basename(videoName))[0] + ".mp3")
        

    
    #disabliing donwload , back , quailty and audio buttons when download starts
    backButton._fg_color = "grey"
    backButton._state = DISABLED
    progressBar = CTkProgressBar(root , width = 300, height = 20)
    blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", text_color="#242424")
    blank_label.place(x=190, y=360)
    downloading = CTkLabel(root , text = "Downloading" , text_color="white" , font=("Times New Roman", 15, "bold") )
    downloading.place(x = 210, y = 360)
    progressBar.place(x = 100, y = 400)
    progressBar.set(0.0)                           
    downloadButton._state = DISABLED
    downloadButton._fg_color = "grey"
    audioOnly._state = DISABLED
    quality.configure(state = DISABLED)
    pauseButton = CTkButton(root , text="Pause" , text_color="white" ,fg_color="#E7B918" , font=("Times New Roman", 15, "bold") , width=100 )
    pauseButton.place(x = 100, y = 440)
    cancelButton = CTkButton(root , text="Cancel" , text_color="white" ,fg_color="red" , font=("Times New Roman", 15) , width=100 )
    cancelButton.place(x = 300, y = 440)
    
    
    
    #starting the download
    try :
        video.download()
        
        
        #if user didn't choose to download audio the video is donwloaded in app folder then we move it to selected path
        if audioOnly.get() == 0:
            shutil.move(videoName, path)
        
        
        #if user chose to download audio the video is donwloaded in app folder then we convert it to mp3 file and move it to selected path
        if audioOnly.get() == 1:
            base, ext = os.path.splitext(videoName)
            new_file = os.path.join(os.path.basename(base) + '.mp3')
            os.rename(videoName, new_file)
            shutil.move(new_file, path)    
    
    
    #if any error ocuurred while downloading we pop up this message
    except :
        msg.showerror(title = "YouTube Video Downloader ", message = "An error occured (this may be caused due to bad internet connection)")
    
    
    #destroying pause and cancel buttons when download is completed
    pauseButton.destroy()
    cancelButton.destroy()
    
    #returning donwload , back , quailty and audio buttons to the normal state when download is done
    downloadButton._state = NORMAL
    downloadButton._fg_color = "green"
    audioOnly._state = NORMAL
    quality.configure(state = NORMAL)
    backButton._fg_color = "#146F86"
    backButton._state = NORMAL
    
    #destroying downloading label and creating done label when download is completed
    downloading.destroy()
    done = CTkLabel(root , text = "Download Completed!" , text_color="green" , font=("Times New Roman", 15, "bold") )
    done.place(x = 190, y = 360)
    
        
    
       
            


#making a thread for download function to avoid overloading        
def downloadThreading ():
    global t , isCanceled
    t = threading.Thread(target=Download)
    t.start()
    if isCanceled :
        sys.exit()
        


    
#creating function which selects audio only
def audio() :
    global quality , setAudio , audioOnly
    if setAudio.get() == 1:
            quality.configure(state = DISABLED)
    else :
        quality.configure(state = NORMAL)



#creatung function which creates the download tab
def downloadTab():
    global linkEntry , youtubeLogo , titleLabel , downloadButton , backButton , videoName , videoNameLabel , streams , quality , setAudio ,audioOnly , audioOnlyText , downloadButton
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
    
    #to take a new line if the video name is too long to avoid bugs
    if len(videoName) > 40 :
        videoName = videoName[:40] + "\n" + videoName[40:]
    if len(videoName) > 80 :
        videoName = videoName[:80] + "\n" + videoName[80:]
    
    videoNameLabel = CTkLabel(root, text = videoName  ,  text_color="white" , font=("Times New Roman", 15))
    videoNameLabel.place(x=35, y=250)
    stream = list(streams)
    quality = customtkinter.CTkOptionMenu(master = root , values = stream , width = 50  )
    quality.place(x=330, y=250)
    audioOnlyText = CTkLabel(root, text = "Audio Only" , text_color="white" , font=("Times New Roman", 15))
    audioOnlyText.place(x=400, y=220)
    audioOnly = customtkinter.CTkCheckBox(master = root , text = " " , width = 10 , height = 1 , state = "normal" , command = audio , variable = setAudio )
    audioOnly.place(x=420, y=250)
    downloadButton = customtkinter.CTkButton(root , text="Download" , text_color="white" ,fg_color="green" , font=("Times New Roman", 15, "bold") , command = downloadThreading , width=150 )
    downloadButton.place(x=187, y=500)
    
    #creating function which back to the main tab
    def back():
        global  youtubeLogo , titleLabel ,videoNameLabel , backButton 
        titleLabel.destroy()
        youtubeLogo.destroy()
        videoNameLabel.destroy()
        quality.destroy()
        audioOnlyText.destroy()
        audioOnly.destroy()
        downloadButton.destroy()
        progressBar.destroy()
        downloading.destroy()
        done.destroy()
        mainTab()
        backButton.destroy()
    backButton = CTkButton(root, text="Back", font=("Times New Roman", 15, "bold") , width=50 , command=back)
    backButton.place(x=30, y=550)



#creating function which stores video's link and then redirects to the download tab
def Entry ():
    global link , linkEntry , videoName , streams , yt
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
            yt = YouTube(link , on_progress_callback = on_progress)
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