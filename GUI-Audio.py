from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from Audios.AudioSteganocryptopy import encryptAudio, decryptAudio

def encryptAudioAction(path, message):
    encryptAudio(path.get(),message.get(),path.get().replace('.wav','_encrypted.wav'))
    messagebox.showinfo('Thông báo', 'Đã mã hóa')

def chooseFileAction(valueFile):
    pathFile = tkinter.filedialog.askopenfile().name
    valueFile.set(pathFile)

def decryptAudioAction(valueFileDe, valueContentDe):
    valueContentDe.set(decryptAudio(valueFileDe.get()))
    messagebox.showinfo('Thông báo', 'Đã giải mã')

def chooseFileDeAction(valueFileDe):
    pathFile = tkinter.filedialog.askopenfile().name
    valueFileDe.set(pathFile)

def main():
    root = Tk()
    root.geometry("370x400")
    root.title('Steganography Audio')
    root.eval('tk::PlaceWindow . center')
    root.resizable(False, False)
    lblEn = Label(root, text="Mã hóa Audio",font=("Arial", 20)).place(x=30, y=10)
    lblFile = Label(root, text="Chọn file").place(x=30, y=50)
    valueFile = StringVar()
    valueFile.set('')
    txtFile = Entry(root, textvariable=valueFile).place(x=100, y=50)
    btnFile = Button(root, text="Browse...",command=lambda: chooseFileAction(valueFile)).place(x=270, y=45)
    lblContent = Label(root, text="Nội dung").place(x=30, y=90)
    valueContent = StringVar()
    valueContent.set('')
    txtContent = Entry(root, textvariable=valueContent).place(x=100, y=90)
    btnEncrypt = Button(root, text="Mã hóa", command=lambda: encryptAudioAction(valueFile, valueContent)).place(x=100, y=120)
    # ==================================
    lblDe = Label(root, text="Giải mã Audio", font=("Arial", 20)).place(x=30, y=200)
    lblFileDe = Label(root, text="Chọn file").place(x=30, y=250)
    valueFileDe = StringVar()
    valueFileDe.set('')
    txtFileDe = Entry(root, textvariable=valueFileDe).place(x=100, y=250)
    btnFileDe = Button(root, text="Browse...", command=lambda: chooseFileDeAction(valueFileDe)).place(x=270, y=245)
    lblFileDe = Label(root, text="Nội dung").place(x=30, y=300)
    valueContentDe = StringVar()
    valueContentDe.set('')
    txtFileDe = Entry(root, textvariable=valueContentDe).place(x=100, y=300)
    btnDecrypt = Button(root, text="Giải mã", command=lambda: decryptAudioAction(valueFileDe, valueContentDe)).place(x=100, y=330)
    root.mainloop()

if __name__ == '__main__':
    main()
