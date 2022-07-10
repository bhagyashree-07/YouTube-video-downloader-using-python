#Importing all required libraries

from tkinter import * #Importing all the modules from tkinter
from tkinter import ttk #used to design GUI
from tkinter import filedialog, messagebox #to ask where to download the file
from pytube import YouTube  #install pytube3 by >>pip install pytube3

# we have to go with this code 
Folder_Name = ""

# to select file location
def openLocation():
    global Folder_Name
    Folder_Name =filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
        
    else:
        locationError.config(text="Please Choose Folder!!", fg="red")
        
# To download video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    
    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)
        
        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
            
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
             
      
        else:
            ytdError.config(text = "Paste the Link again !!", fg="red")
            
    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed")
    messagebox.showinfo("Thank you!","Download completed..")

# for GUI we have to follow the following steps :::             
root = Tk() #create object of tkinter
root.title("YouTube Video Dowloader")

root.geometry("500x550")  #set window
root.columnconfigure(0, weight=1) #set all content in center

#YouTube Download link label
ytdLabel = Label(root, text="Enter the URL of the Video", font =("arial", 15, "bold"), padx= 10, pady= 10)
ytdLabel.grid()

#Entry box

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable = ytdEntryVar)
ytdEntry.grid()

#error msg
ytdError = Label(root, fg="Green", font=("arial", 12), padx= 10, pady= 10)
ytdError.grid()

#Asking save file label
saveLabel = Label(root, text="Save the Video File", font=("arial", 15, "bold"), padx= 10, pady= 10)
saveLabel.grid()

#button of save file
saveEntry = Button(root, width=10, bg="Blue", fg="white", text="Choose Path",command =openLocation)
saveEntry.grid()


# Error msg location 
locationError = Label(root, fg="Green", font=("jost", 12), padx= 10, pady= 10)
locationError.grid()

#Download Quality
ytdQuality = Label(root, text="Select Quality", font=("arial", 15, "bold"), padx= 10, pady= 10)
ytdQuality.grid()

#combobox
choices = ["720p","144p", "Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()

dwn = Label(root, text="Click on Download Button", font=("arial", 15, "bold"), padx= 10, pady= 10)
dwn.grid()

#download button
downloadbtn = Button(root, text="Download", width=10, bg="Blue", fg="white", command=DownloadVideo)
downloadbtn.grid()


developerlabel = Label(root, text="Bhagyashree Rajguru", font=("arial", 13, "bold"), padx= 10, pady= 60)
developerlabel.grid()

root.mainloop()

# now after making GUI we have to make it functionallll so ....