import pyttsx3
import PyPDF2
import threading
from tkinter import Tk, Button, Label, filedialog, messagebox

# Initialize the TTS engine
player = pyttsx3.init()

# Flag to control the reading process
is_reading = False
file_selected = False

def read_pdf():
    global is_reading
    is_reading = True

    if file_selected:
        for num in range(pages):
            if not is_reading:
                break

            page = pdfreader.pages[num]
            text = page.extract_text()
            if text.strip():
                player.say(text)
                player.runAndWait()

        if is_reading:
            status_label.config(text="Finished reading the PDF.")
        else:
            status_label.config(text="Reading stopped.")
    else:
        messagebox.showerror("Error", "Please select a PDF file first.")

def select_file():
    global pdfreader, pages, file_selected
    book = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
    if book:
        pdfreader = PyPDF2.PdfReader(book)
        pages = len(pdfreader.pages)
        file_selected = True
        status_label.config(text=f"Selected file: {book.split('/')[-1]}")

def start_reading():
    if not is_reading:
        if file_selected:
            status_label.config(text="Reading the PDF...")
            read_thread = threading.Thread(target=read_pdf)
            read_thread.start()
        else:
            messagebox.showerror("Error", "Please select a PDF file first.")


# Setup the GUI
root = Tk()
root.title("PDF Reader")
root.geometry("300x200")

select_button = Button(root, text="Select PDF File", command=select_file, width=20)
select_button.pack(pady=10)

start_button = Button(root, text="Start Reading", command=start_reading, width=20)
start_button.pack(pady=10)

status_label = Label(root, text="No file selected.", wraplength=250)
status_label.pack(pady=20)

root.mainloop()
