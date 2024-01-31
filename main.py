from pytube import YouTube
from tkinter import *
from tkinter import messagebox, ttk

tab = Tk()
tab.geometry("600x400")
tab.title("YouTube Video Downloader")
tab.configure(background='#0096DC')

#download video function
def down():
    bar['value']=0
    try:
        selected_value = selected_option.get()
        link = ent1.get()  
        ytobject = YouTube(link, on_progress_callback=on_progress)
        if selected_value=='mp3':
            video = ytobject.streams.get_audio_only()
        else:
            video = ytobject.streams.filter(res=selected_value).first()
        video.download()
        messagebox.showinfo("downloaded", "Download Completed")
    except:
        messagebox.showerror("value error", "please provide valid you tube link")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per=str(int(percentage_of_compeletion))
    pper.configure(text=per+'%')
    pper.update()

    bar['value']+=percentage_of_compeletion
    

#title label
paste_label = Label(tab, text="You Tube Video Downloader", bg='#0096DC', fg="white", font=("vardana",15, 'bold'))
paste_label.pack(pady=10)


#Paste link Label text
paste_label = Label(tab, text="Paste Your Link Here", bg='#0096DC', fg="white", font=("vardana",10))
paste_label.pack()

#Entry Widget
ent1 = Entry(tab, width=60, fg="black", bg="white", font=("vardana"), state='normal')
ent1.pack(pady=10)

#Select Quality text
paste_label = Label(tab, text="Select Quality", bg='#0096DC', fg="white", font=("vardana",10))
paste_label.pack()

#option list
options_list = ['mp3',"240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"]
selected_option = StringVar(tab)
selected_option.set("360p")
question_menu = OptionMenu(tab, selected_option, *options_list, ) 
question_menu.pack(pady=10)
question_menu.config(font=("vardana",15))

#progress percentage
pper = Label(tab, text="0%", bg='#0096DC', fg="white", font=("vardana",10))
pper.pack()

#progress bar
bar = ttk.Progressbar(tab, orient='horizontal', length=300)
bar.pack(padx=10, pady=10)

#download button
submit_button = Button(tab, text="Download", bg="white", command=down)
submit_button.pack(pady=10)
submit_button.config(font=("vardana",15))

# Start the GUI
tab.mainloop()

