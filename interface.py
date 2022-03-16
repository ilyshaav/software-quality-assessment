from tkinter import *
import textCompression

window1 = Tk()
window1.title("Сжиматор текста")
window1.geometry('600x450')


def interCompr():
    res = format(txt_window1.get())

    if textCompression.Compressor.checkLen(res): 
        comprText = textCompression.Compressor.textCompression(res)
        lbl_window1.configure(text=comprText)
    else:
        lbl_window1.configure(text="ваш текст болеe 30 знаков, повторите ввод")
        txt_window1.delete(0, len(res))

btn_add_window1 = Button(window1, text="произвести сжатие", command=interCompr)
btn_add_window1.grid(column=0, row=1)

txt_window1 = Entry(window1, width=30)
txt_window1.grid(column=0, row=0)

lbl_window1 = Label(window1, text="вывод сжатого текста")
lbl_window1.grid(column=1, row=0)

window1.mainloop()
