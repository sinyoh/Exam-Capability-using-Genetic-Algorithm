from tkinter import *
from tkinter.ttk import *

from root import *

# TODO: ADRIAN
class Home():
    def __init__(self):
        self.frame_home = Frame(root)
        self.init_home()
        self.show_home()
        self.i = 0

    def init_home(self):
        # ! UI DESIGN
        # NAME
        self.name_label = Label(self.frame_home, text="Name : ", font=("Times New Roman", 10))
        self.name = Entry(self.frame_home, width=14)

        # WEIGHT
        self.weight_label = Label(self.frame_home, text="Weight : ", font=("Times New Roman", 10))
        self.weight = Spinbox(self.frame_home, width=10, from_=1, to=100)
        self.weight_desc = Label(self.frame_home, text="Number of page", font=("Times New Roman", 10))

        # VALUE
        self.value_label = Label(self.frame_home, text="Value : ", font=("Times New Roman", 10))
        self.value = Spinbox(self.frame_home, width=10, from_=1, to=100)
        self.value_desc = Label(self.frame_home, text="How much value on the test", font=("Times New Roman", 10))

        # TYPE
        self.type_label = Label(self.frame_home, text="Type : ", font=("Times New Roman", 10))
        self.type = Combobox(self.frame_home, width=12,textvariable=StringVar(), state='readonly')
        self.type['values'] = ("0 (Mudah dipahami)","1 (Normal)", "2 (Susah dipahami)")
        self.type.current(0)

        # BUTTONS
        self.err = Message(self.frame_home, text="", fg="red",font=("Times New Roman", 10), width=200)
        self.deleteBtn = Button(self.frame_home, text="Delete", command=self.delete_subject)
        self.sumbitBtn = Button(self.frame_home, text="Submit", command=self.submit)
        self.runBtn = Button(self.frame_home, text="Run", command=self.GA)
        self.clearBtn = Button(self.frame_home, text="Clear List", command=self.clear_subject)

        self.separator = Separator(self.frame_home, orient='horizontal')

        # TODO: DISPLAY UI
        # LABEL
        self.message = Label(self.frame_home, text="Subjects : ", font=("Times New Roman", 16))

        self.name_ui = Label(self.frame_home, text="Name",font=("Times New Roman", 10))
        self.name_list = Listbox(self.frame_home, height=10, width=15, bg="grey", activestyle='dotbox', font=("Times New Roman", 14), fg="yellow", selectmode=MULTIPLE)

        self.weight_ui = Label(self.frame_home, text="Weight", font=("Times New Roman", 10))
        self.weight_list = Listbox(self.frame_home, height=10, width=15, bg="grey",activestyle='dotbox', font=("Times New Roman", 14), fg="yellow")

        self.value_ui = Label(self.frame_home, text="Value",font=("Times New Roman", 10))
        self.value_list = Listbox(self.frame_home, height=10, width=15, bg="grey",activestyle='dotbox', font=("Times New Roman", 14), fg="yellow")

        self.type_ui = Label(self.frame_home, text="Type",font=("Times New Roman", 10))
        self.type_list = Listbox(self.frame_home, height=10, width=15, bg="grey", activestyle='dotbox', font=("Times New Roman", 14), fg="yellow")

    def show_home(self):
        self.frame_home.pack()
        self.frame_home.columnconfigure(0, weight=1)
        self.frame_home.columnconfigure(1, weight=1)
        self.frame_home.columnconfigure(2, weight=1)
        self.frame_home.columnconfigure(3, weight=1)
        self.frame_home.columnconfigure(4, weight=1)

        # TODO: MAIN UI
        self.name_label.grid(row=0, column=0, sticky=W, pady=2)
        self.name.grid(row=0, column=1, columnspan=2,sticky=W, pady=2, ipadx=20)

        self.weight_label.grid(row=1, column=0, sticky=W, pady=2)
        self.weight.grid(row=1, column=1, sticky=W, pady=2, ipadx=20)
        self.weight_desc.grid(row=1, column=2, columnspan=2,sticky=W, pady=2, padx=3)

        self.value_label.grid(row=2, column=0, sticky=W, pady=2)
        self.value.grid(row=2, column=1, sticky=W, pady=2, ipadx=20)
        self.value_desc.grid(row=2, column=2, columnspan=2, sticky=W, pady=2, padx=3)

        self.type_label.grid(row=3, column=0, sticky=W, pady=2)
        self.type.grid(row=3, column=1, columnspan=2,sticky=W, pady=2, ipadx=20)

        self.err.grid(row=4, column=2, columnspan=2, sticky=W, pady=2, padx=30)
        self.sumbitBtn.grid(row=4, column=0, columnspan=2, sticky=W, pady=2)
        self.deleteBtn.grid(row=4, column=0, columnspan=2,sticky=W, pady=2, padx=80)
        self.runBtn.grid(row=4, column=0, columnspan=3,sticky=W, pady=2, padx=160)
        self.clearBtn.grid(row=4, column=0, columnspan=4,sticky=W, pady=2, padx=240)

        self.separator.grid(row=5, column=0, sticky=EW,rowspan=1, columnspan=4)

        # TODO: DISPLAY UI
        self.message.grid(row=6, column=0, sticky=W, pady=4)

        self.name_ui.grid(row=7, column=0, pady=2)
        self.name_list.grid(row=8, column=0, pady=2, padx=2)

        self.weight_ui.grid(row=7, column=1, pady=2)
        self.weight_list.grid(row=8, column=1, pady=2, padx=2)

        self.value_ui.grid(row=7, column=2, pady=2)
        self.value_list.grid(row=8, column=2, pady=2, padx=2)

        self.type_ui.grid(row=7, column=3, pady=2)
        self.type_list.grid(row=8, column=3, pady=2, padx=2)

    def hide_home(self):
        self.frame_home.pack_forget()

    def display(self, _name, _weight, _value, _type):
        self.err.configure(text="")

        self.name_list.insert(self.i, _name)
        self.weight_list.insert(self.i, _weight)
        self.value_list.insert(self.i, _value)
        self.type_list.insert(self.i, _type)

    def submit(self):
        _name = self.name.get()
        _weight = self.weight.get()
        _value = self.value.get()
        _type = self.type.get()

        if len(_name) == 0 or len(_type) == 0:
            self.err.configure(text="Semua input harus diisi!")
            return
        elif (not _weight.isdigit()) or (not _value.isdigit()):
            self.err.configure(text="Weight dan Value harus angka!")
            return

        if _type[0] == "0":
            _type = 0
        elif _type[0] == "1":
            _type = 1
        else:
            _type = 2

        KBplusRW.subjects.append(KBplusRW.subject(
            _name, int(_weight), int(_value), _type))

        self.display(_name, _weight, _value, _type)
        self.i += 1

    def delete_subject(self):
        subjToDel = self.name_list.curselection()
        if len(subjToDel) == 0:
            self.err.configure(text="Pilih nama subject yang akan dihapus")
            return

        for subj in subjToDel[::-1]:
            self.name_list.delete(subj)
            self.weight_list.delete(subj)
            self.value_list.delete(subj)
            self.type_list.delete(subj)
            KBplusRW.subjects.pop(subj)
            print(KBplusRW.subjects)

    def clear_subject(self):
        def confirmClear():
            self.name_list.delete(0, END)
            self.weight_list.delete(0, END)
            self.value_list.delete(0, END)
            self.type_list.delete(0, END)
            KBplusRW.subjects.clear()
            conf.destroy()

        conf = Toplevel()
        conf.geometry("170x100")
        conf.title("Clear Confirmation")
        Label(conf, text="Delete all subjects from the list?").grid(row=0, column=0, pady=5)
        Button(conf, text="Cancel", command=conf.destroy).grid(row=1, column=0, pady=2)
        Button(conf, text="Confirm", command=confirmClear).grid(row=2, column=0, pady=2)
        conf.mainloop()

    def GA(self):
        popul = KBplusRW.population()
        for i in range(KBplusRW.initial_population_size):
            popul.chromosome.append(KBplusRW.chromosome())

        popul.totalVal()
        popul.hitungRoulette()
        
        for i in range(KBplusRW.number_of_generation):
            popul = KBplusRW.tournament(popul)

        output = Tk()
        output.geometry("500x350")
        output.title("hasil")

        # ! RESULT
        print("Most Optimal Solution")
        biggest = popul.chromosome[0].evaluate()
        for i in popul.chromosome:
            if biggest <= i.evaluate():
                biggest = i.evaluate()
                solution = i
        solution.print()
       
        # TODO: TABLE OUTPUT (NICHO)
        arrayHasil = [["Nama bab", "Weight", "Type", "Value"]]
        for i in range(len(KBplusRW.subjects)):
            if(solution.genes[i] == 1):
               
                KBplusRW.subjects[i].print()
                arrayHasil.append([
                    str(KBplusRW.subjects[i].name) + "\n",
                    str(KBplusRW.subjects[i].weight) + "\n", 
                    str(KBplusRW.subjects[i].value) + "\n",
                    str(KBplusRW.subjects[i].type) + "\n"
                ])
        

        for i in range(len(arrayHasil)):
            for j in range(len(arrayHasil[i])):
                e = Entry(output, width=20, font=("Times New Roman", 10))
                e.grid(row=i, column=j)
                e.insert(END, arrayHasil[i][j])

        # WEIGHT
        e = Entry(output, width=20, font=("Times New Roman", 10))
        e.grid(row=len(arrayHasil), column=0)
        e.insert(END,"Total weight: " + str(solution.total_weight))

        # VALUE
        e = Entry(output, width=20, font=("Times New Roman", 10))
        e.grid(row=len(arrayHasil)+1, column=0)
        e.insert(END,"Total value: " + str(solution.total_value))

        output.mainloop()
