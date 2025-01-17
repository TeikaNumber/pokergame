import tkinter as tk

class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)

        self.frames["startPage"].grid(row=0,col=0,sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(parent, controller,)
        self.controller = controller
        lbl = tk.Label(self, text="Welcome To POKERGAME")
        lbl.pack()

        play_btn = tk.Button(self, text="Play", command=lambda: controller.show_frame("game"))
        info_btn = tk.Button(self, text="Info", command=lambda: controller.show_frame("info"))
        quit_btn = tk.Button(self, text="Quit", command=lambda: controller.destroy())

        play_btn.pack()
        info_btn.pack()
        quit_btn.pack()

root = App()

root.title("poker game")
root.geometry('350x200')


root.mainloop()