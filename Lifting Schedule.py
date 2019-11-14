import tkinter
import random
#Create root
root = tkinter.Tk()

#Change root window background color
root.configure(bg="white")

#Change the title
root.title("Exercise Schedule")

#Change the window size
root.geometry("925x400")

#Create a list
Chest = []
Back = []
Shoulder = []
Biceps = []
Triceps = []
Abs = []
Cardio = []

#Create functions
def clear_Chbox():
    lb_Chest.delete(0, "end")

def clear_Babox():
    lb_Back.delete(0, "end")

def clear_Shbox():
    lb_Shoulder.delete(0, "end")

def clear_Bibox():
    lb_Biceps.delete(0, "end")

def clear_Trbox():
    lb_Triceps.delete(0, "end")

def clear_Abbox():
    lb_Abs.delete(0, "end")

def clear_Cabox():
    lb_Cardio.delete(0, "end")
    
def update_chestbox():
    clear_Chbox()
    for Exercise in Chest:
        lb_Chest.insert("end", Exercise)

def update_backbox():
    clear_Babox()
    for Exercise in Back:
        lb_Back.insert("end", Exercise)

def update_shoulderbox():
    clear_Shbox()
    for Exercise in Shoulder:
        lb_Shoulder.insert("end", Exercise)

def update_bicepsbox():
    clear_Bibox()
    for Exercise in Biceps:
        lb_Biceps.insert("end", Exercise)

def update_tricepsbox():
    clear_Trbox()
    for Exercise in Triceps:
        lb_Triceps.insert("end", Exercise)

def update_absbox():
    clear_Abbox()
    for Exercise in Abs:
        lb_Abs.insert("end", Exercise)

def update_cardiobox():
    clear_Cabox()
    for Exercise in Cardio:
        lb_Cardio.insert("end", Exercise)
    
def add_Chest():
    Exercise = txt_input.get()
    if Exercise !="":
        Chest.append(Exercise)
        update_chestbox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
    txt_input.delete(0, "end")

def add_Back():
    Exercise = txt_input.get()
    if Exercise !="":
        Back.append(Exercise)
        update_backbox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
    txt_input.delete(0, "end")

def add_Shoulder():
    Exercise = txt_input.get()
    if Exercise !="":
        Shoulder.append(Exercise)
        update_shoulderbox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
    txt_input.delete(0, "end")

def add_Biceps():
    Exercise = txt_input.get()
    if Exercise !="":
        Biceps.append(Exercise)
        update_bicepsbox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
    txt_input.delete(0, "end")

def add_Triceps():
    Exercise = txt_input.get()
    if Exercise !="":
        Triceps.append(Exercise)
        update_tricepsbox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
    txt_input.delete(0, "end")

def add_Abs():
    Exercise = txt_input.get()
    if Exercise !="":
        Abs.append(Exercise)
        update_absbox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
        txt_input.delete(0, "end")

def add_Cardio():
    Exercise = txt_input.get()
    if Exercise !="":
        Cardio.append(Exercise)
        update_cardiobox()
    else:
        lbl_display["text"] = "Do Not Leave Blank."
    txt_input.delete(0, "end")

def save():
        exerciselist = open("Exercise Plan", "w")
        exerciselist.write(str(Chest))
        exerciselist.write(str(Back))
        exerciselist.write(str(Shoulder))
        exerciselist.write(str(Biceps))
        exerciselist.write(str(Triceps))
        exerciselist.write(str(Abs))
        exerciselist.write(str(Cardio))       
        exerciselist.close()

def del_all():
    global Exercise
    Chest.clear()
    Back.clear()
    Shoulder.clear()
    Biceps.clear()
    Triceps.clear()
    Abs.clear()
    Cardio.clear()
    update_chestbox()
    update_backbox()
    update_shoulderbox()
    update_bicepsbox()
    update_tricepsbox()
    update_absbox()
    update_cardiobox()

def del_one1():
    Exercise1 = lb_Chest.get("active")
    if Exercise1 in Chest:
        Chest.remove(Exercise1)
        update_chestbox()
def del_one2():
    Exercise2 = lb_Back.get("active")    
    if Exercise2 in Back:
        Back.remove(Exercise2)
        update_backbox()
def del_one3():
    Exercise3 = lb_Shoulder.get("active")
    if Exercise3 in Shoulder:
        Shoulder.remove(Exercise3)
        update_shoulderbox()
def del_one4():
    Exercise4 = lb_Biceps.get("active")
    if Exercise4 in Biceps:
        Biceps.remove(Exercise4)
        update_bicepsbox()
def del_one5():
    Exercise5 = lb_Triceps.get("active")
    if Exercise5 in Triceps:
        Triceps.remove(Exercise5)
        update_tricepsbox()
def del_one6():
    Exercise6 = lb_Cardio.get("active")
    if Exercise6 in Cardio:
        Cardio.remove(Exercise6)
        update_cardiobox()

    
def choose_randomChest():
    Exercise = random.choice(Chest)
    lbl_display["text"]=Exercise

def choose_randomBack():
    Exercise = random.choice(Back)
    lbl_display["text"]=Exercise

def choose_randomShoulder():
    Exercise = random.choice(Shoulder)
    lbl_display["text"]=Exercise

def choose_randomBiceps():
    Exercise = random.choice(Biceps)
    lbl_display["text"]=Exercise

def choose_randomTriceps():
    Exercise = random.choice(Triceps)
    lbl_display["text"]=Exercise

def choose_randomAbs():
    Exercise = random.choice(Abs)
    lbl_display["text"]=Exercise

def choose_randomCardio():
    Exercise = random.choice(Cardio)
    lbl_display["text"]=Exercise


def number_of_exercises():
    number_of_exercises = len(Chest + Back + Shoulder + Biceps +Triceps + Abs + Cardio)
    msg = "Number of exercises: %s" %number_of_exercises
    lbl_display["text"]=msg

lbl_title = tkinter.Label(root, text="Exercise-Plan", font=("Helvetica",11, "bold", "underline"), bg="white")
lbl_title.grid(row=0,column=3)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=1,column=3)

txt_input = tkinter.Entry(root, font=("Helvetica",9), width=15)
txt_input.grid(row=2,column=3)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=4,column=3)

btn_number_of_exercises = tkinter.Button(root, text="Number of Exercises", fg="green", font=("Helvetica",9), bg="white", command=number_of_exercises)
btn_number_of_exercises.grid(row=3,column=2)

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", font=("Helvetica",9), bg="white", command=del_all)
btn_del_all.grid(row=3,column=1)

btn_Save = tkinter.Button(root, text="Save List", fg="green", font=("Helvetica",9), bg="white", command=save)
btn_Save.grid(row=3,column=4)

btn_Exit = tkinter.Button(root, text="Exit", fg="green", font=("Helvetica",9), bg="white", command=exit)
btn_Exit.grid(row=3,column=5)

btn_add_Chest = tkinter.Button(root, text="Add Chest Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Chest)
btn_add_Chest.grid(row=12,column=0)

btn_add_Back = tkinter.Button(root, text="Add Back Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Back)
btn_add_Back.grid(row=12,column=1)

btn_add_Shoulder = tkinter.Button(root, text="Add Shoulder Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Shoulder)
btn_add_Shoulder.grid(row=12,column=2)

btn_add_Biceps = tkinter.Button(root, text="Add Biceps Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Biceps)
btn_add_Biceps.grid(row=12,column=3)

btn_add_Triceps = tkinter.Button(root, text="Add Triceps Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Triceps)
btn_add_Triceps.grid(row=12,column=4)

btn_add_Abs = tkinter.Button(root, text="Add Abs Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Abs)
btn_add_Abs.grid(row=12,column=5)

btn_add_Cardio = tkinter.Button(root, text="Add Cardio Exercise", fg="green", font=("Helvetica",9), bg="white", command=add_Cardio)
btn_add_Cardio.grid(row=12,column=6)

btn_choose_randomChest = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomChest)
btn_choose_randomChest.grid(row=13,column=0)

btn_choose_randomBack = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomBack)
btn_choose_randomBack.grid(row=13,column=1)

btn_choose_randomShoulder = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomShoulder)
btn_choose_randomShoulder.grid(row=13,column=2)

btn_choose_randomBiceps = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomBiceps)
btn_choose_randomBiceps.grid(row=13,column=3)

btn_choose_randomTriceps = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomTriceps)
btn_choose_randomTriceps.grid(row=13,column=4)

btn_choose_randomAbs = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomAbs)
btn_choose_randomAbs.grid(row=13,column=5)

btn_choose_randomCardio = tkinter.Button(root, text="Choose Random", fg="green", font=("Helvetica",9), bg="white", command=choose_randomCardio)
btn_choose_randomCardio.grid(row=13,column=6)

btn_del_one1 = tkinter.Button(root, text="Delete", fg="green", font=("Helvetica",9), bg="white", command=del_one1)
btn_del_one1.grid(row=14,column=0)

btn_del_one2 = tkinter.Button(root, text="Delete", fg="green", font=("Helvetica",9), bg="white", command=del_one2)
btn_del_one2.grid(row=14,column=1)

btn_del_one3 = tkinter.Button(root, text="Delete", fg="green", font=("Helvetica",9), bg="white", command=del_one3)
btn_del_one3.grid(row=14,column=2)

btn_del_one4 = tkinter.Button(root, text="Delete", fg="green", font=("Helvetica",9), bg="white", command=del_one4)
btn_del_one4.grid(row=14,column=3)
4
btn_del_one5 = tkinter.Button(root, text="Delete", fg="green", font=("Helvetica",9), bg="white", command=del_one5)
btn_del_one5.grid(row=14,column=4)

btn_del_one6 = tkinter.Button(root, text="Delete", fg="green", font=("Helvetica",9), bg="white", command=del_one6)
btn_del_one6.grid(row=14,column=5)

lb_Chest = tkinter.Listbox(root)
lb_Chest.grid(row=14,column=0)

lb_Back = tkinter.Listbox(root)
lb_Back.grid(row=14,column=1)

lb_Shoulder = tkinter.Listbox(root)
lb_Shoulder.grid(row=14,column=2)

lb_Biceps = tkinter.Listbox(root)
lb_Biceps.grid(row=14,column=3)

lb_Triceps = tkinter.Listbox(root)
lb_Triceps.grid(row=14,column=4)

lb_Abs = tkinter.Listbox(root)
lb_Abs.grid(row=14,column=5)

lb_Cardio = tkinter.Listbox(root)
lb_Cardio.grid(row=14,column=6)

root.mainloop()
