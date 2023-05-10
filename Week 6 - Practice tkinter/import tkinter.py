import tkinter

main_window = tkinter.Tk()

print(main_window.__dict__)

label1 = tkinter.Label(main_window, text="Label 1")
label2 = tkinter.Label(main_window, text="Label 2")

Button1 = tkinter.Button(main_window, text="Button 1")
Button2 = tkinter.Button(main_window, text="Button 2")

# method positioning
label1.pack()
label2.pack()
Button1.pack()
Button2.pack()

# method menampilkan GUI
main_window.mainloop()