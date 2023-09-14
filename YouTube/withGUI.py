from pytube import YouTube
from tkinter import Tk, messagebox, Label, Button, Entry

window = Tk()
window.title("YouTube Videos Downloader")


def download():

    try:
        my_video_url = url_entry.get()
        yt = YouTube(my_video_url).streams.get_highest_resolution().download("Videos")
        messagebox.showinfo("Success", "Downloaded Successfully")

    except Exception as e:
        messagebox.showerror("Error", "Error Occurred\n" + str(e))


url_label = Label(window, text="Enter URL: ")
url_label.grid(column=0, row=0)

url_entry = Entry(window, width=40)
url_entry.grid(column=1, row=0)

download_button = Button(window, text="Download", command=download)
download_button.grid(column=2, row=0)

window.mainloop()
