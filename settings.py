from tkinter import *
from tkinter.ttk import *

from root import *


class Settings():
    def __init__(self) -> None:
        self.frame_settings = Frame(root)
        self.init_settings()

    def init_settings(self):
        # MAXIMUM PAGE
        var1 = DoubleVar(value=200)
        self.page_label = Label(self.frame_settings, text="Maximum pages : ", font=("Times New Roman", 10))
        self.page = Spinbox(self.frame_settings, width=22,from_=1, to=1000, textvariable=var1)
        self.page_desc = Label(self.frame_settings, text="Maximum pages numbers allowed", font=("Times New Roman", 10))

        # MUTATION RATE
        var2 = DoubleVar(value=50)
        self.rate_label = Label(self.frame_settings, text="Mutation rate : ", font=("Times New Roman", 10))
        self.rate = Spinbox(self.frame_settings, width=22,from_=1, to=100, textvariable=var2)

        # ELITISM
        self.elitism_label = Label(self.frame_settings, text="Elitism : ", font=("Times New Roman", 10))
        self.elitism = Combobox(self.frame_settings, width=22, textvariable=StringVar(), state='readonly')
        self.elitism['values'] = ("True", "False")
        self.elitism.current(0)

        # INITIAL POPULATION
        var3 = DoubleVar(value=50)
        self.initial_label = Label(self.frame_settings, text="Initial population : ", font=("Times New Roman", 10))
        self.initial = Spinbox(self.frame_settings,width=22, from_=1, to=1000, textvariable=var3)
        self.initial_desc = Label(self.frame_settings, text="Numbers of subject combinations", font=("Times New Roman", 10))

        # NUMBER OF GEN
        var4 = DoubleVar(value=100)
        self.number_label = Label(self.frame_settings, text="Number of generation : ", font=("Times New Roman", 10))
        self.number = Spinbox(self.frame_settings, width=22,from_=1, to=500, textvariable=var4)
        self.number_desc = Label(self.frame_settings, text="Numbers of iterations", font=("Times New Roman", 10))

        # # ERROR
        # self.err = Message(self.frame_settings, text="",fg="red", font=("Times New Roman", 10), width=200)

        self.submitBtn = Button(self.frame_settings,text="OK", command=self.submit)

    # LOAD SETTING DENGAN GRID
    def show_settings(self):
        self.frame_settings.pack()
        self.frame_settings.columnconfigure(0, weight=1)
        self.frame_settings.columnconfigure(1, weight=1)
        self.frame_settings.columnconfigure(2, weight=1)
        self.frame_settings.columnconfigure(3, weight=1)
        self.frame_settings.columnconfigure(4, weight=1)

        self.page_label.grid(row=0, column=0, sticky=W, pady=2)
        self.page.grid(row=0, column=1, columnspan=2,sticky=W, pady=2, ipadx=20)
        self.page_desc.grid(row=0, column=2, columnspan=2,sticky=W, pady=2, padx=3)

        self.rate_label.grid(row=1, column=0, sticky=W, pady=2)
        self.rate.grid(row=1, column=1, columnspan=2,sticky=W, pady=2, ipadx=20)

        self.elitism_label.grid(row=2, column=0, sticky=W, pady=2)
        self.elitism.grid(row=2, column=1, columnspan=2,sticky=W, pady=2, ipadx=20)

        self.initial_label.grid(row=3, column=0, sticky=W, pady=2)
        self.initial.grid(row=3, column=1, columnspan=2,sticky=W, pady=2, ipadx=20)
        self.initial_desc.grid(row=3, column=2, columnspan=2, sticky=W, pady=2, padx=3)

        self.number_label.grid(row=4, column=0, sticky=W, pady=2)
        self.number.grid(row=4, column=1, sticky=W, pady=2, ipadx=20)
        self.number_desc.grid(row=4, column=2, columnspan=2,sticky=W, pady=2, padx=3)

        # self.err.grid(row=6, column=0, columnspan=2, sticky=W, pady=2)

        self.submitBtn.grid(row=5, column=0, columnspan=2, sticky=W, pady=2)

    def hide_settings(self):
        self.frame_settings.pack_forget()

    def submit(self):
        max_pages = int(self.page.get())
        mutationRate = float(self.rate.get())
        elitism = self.elitism.get()
        initial_population_size = int(self.initial.get())
        number_of_generation = int(self.number.get())

        self.set_var(max_pages, mutationRate, elitism,
                     initial_population_size, number_of_generation)

        print(max_pages, mutationRate, elitism,
              initial_population_size, number_of_generation)

        if(not self.page.get().isdigit()):
            self.err.config(text="ERROR")
        
        if elitism == "True":
            elitism = True
        else:
            elitism = False

    def set_var(self, maxpage, mutation, elitism_, init_pop, number_gen):
        KBplusRW.max_pages = maxpage
        KBplusRW.mutationRate = mutation
        KBplusRW.elitism = elitism_
        KBplusRW.initial_population_size = init_pop
        KBplusRW.number_of_generation = number_gen

        print("Test di KB",  KBplusRW.max_pages,  KBplusRW.mutationRate,  KBplusRW.elitism,
              KBplusRW.initial_population_size, KBplusRW.number_of_generation)
