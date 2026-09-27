from tkinter import *
from tkinter import ttk, messagebox

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()
    age = age_entry.get()
    section = section_entry.get()

    if name == "" or grade == "" or age == "" or section == "":
        messagebox.showwarning("Warning", "Please fill in all the feilds")
        return

    student_table.insert("", END, values=(name, grade, age, section))

    messagebox.showinfo("Success", "Student added successfully!")
    clear_fields()

def update_student():
    selected = student_table. focus ()
        
    if selected == "":
        messagebox.showwarning("Warning", "Please select a student to update.")
        return
        
    student_table. item(
        selected,
        values=(
            name_entry.get(),
            grade_entry.get (),
            age_entry.get (),
            section_entry.get ()
        )
    )

    messagebox. showinfo("Success", "student record updated!")
    clear_fields ()

def delete_student() :
    selected = student_table.focus ()

    if selected == "":
        messagebox.showwarning ("Warning", "Please select a student to delete.")
        return

    student_table.delete (selected)

    messagebox.showinfo("Deleted", "Student record deleted!")
    clear_fields ()

def clear_fields () :
    name_entry.delete (0, END)
    grade_entry.delete(0, END)
    age_entry.delete(0,END)
    section_entry.delete (0, END)

def select_student (event) :
    selected = student_table.focus ()

    if selected == "":
        return

    data = student_table.item(selected)
    values = data["values"]

    clear_fields ()

    name_entry.insert (0, values [0])
    grade_entry. insert (0, values [1])
    age_entry.insert (0, values [2])
    section_entry.insert(0, values[3])

root = Tk()

root.title("Student Management System")
root.geometry("850x550")
root.config(bg="#e8f1f8")

title = Label (
    root,
    text="Student Management System",
    font=("Arial", 24, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=15
)

title.pack (fill=X)

form_frame = Frame (root, bg="#e8f1f8")
form_frame.pack (pady=20)

Label (
    form_frame,
    text="Student Name:",
    font=("Arial", 12),
    bg="#e8f1f8"
).grid(row=0, column=0, padx=10, pady=10)

name_entry = Entry(
    form_frame,
    font=("Arial", 12),
    width=25
)

name_entry.grid(row=0, column=1, padx=10, pady=10)

Label (
    form_frame,
    text="Grade:",
    font=("Arial", 12),
    bg="#e8f1f8"
).grid(row=0, column=2, padx=10, pady=10)

grade_entry = Entry(
    form_frame,
    font=("Arial", 12),
    width=15
)

grade_entry.grid(row=0, column=3, padx=10, pady=10)

Label (
    form_frame,
    text="Age:",
    font=("Arial", 12),
    bg="#e8f1f8"
).grid(row=1, column=0, padx=10, pady=10)

age_entry = Entry(
    form_frame,
    font=("Arial", 12),
    width=25
)

age_entry.grid(row=1, column=1, padx=10, pady=10)

Label (
    form_frame,
    text="Section:",
    font=("Arial", 12),
    bg="#e8f1f8"
).grid(row=1, column=2, padx=10, pady=10)

section_entry = Entry (
    form_frame,
    font=("Arial", 12),
    width=15
)

section_entry.grid(row=1, column=3, padx=10, pady=10)

button_frame = Frame (root, bg="#e8f1f8")
button_frame.pack (pady=10)

Button(
    button_frame,
    text="Add Student",
    width=15,
    bg="#27ae60",
    fg="white",
    font=("Arial", 11, "bold"),
    command = add_student
).grid(row=0, column=0, padx=8)

Button (
    button_frame,
    text="Update",
    width=15,
    bg="#2980b9",
    fg="white",
    font=("Arial", 11, "bold"),
    command = update_student
).grid(row=0, column=1, padx=8)

Button (
    button_frame,
    text="Delete",
    width=15,
    bg="#c0392b",
    fg="white",
    font=("Arial", 11, "bold"),
    command = delete_student
).grid(row=0, column=2, padx=8)

Button (
    button_frame,
    text="Clear",
    width=15,
    bg="#7f8c8d",
    fg="white",
    font=("Arial", 11, "bold"),
    command = clear_fields
).grid(row=0, column=3, padx=8)

table_frame = Frame (root)
table_frame.pack (pady=20)

columns = ("Name", "Grade", "Age", "Section")
student_table = ttk.Treeview (
    table_frame,
    columns=columns,
    show="headings",
    height=10
)

student_table.heading("Name", text="Student Name")
student_table.heading("Grade", text="Grade")
student_table.heading("Age", text="Age")
student_table.heading("Section", text="Section")

student_table.column("Name", width=250)
student_table.column("Grade", width=150)
student_table.column("Age", width=100)
student_table.column("Section", width=150)

student_table.pack ()

student_table.bind(
    "<ButtonRelease-1>",
    select_student
)

student_table.insert (
    "",
    END,
    values=("Ava Liu", "9", "14", "A")
)
student_table.insert (
    "",
    END,
    values=("Sissi Song", "9", "14", "B")
)

student_table.insert (
    "",
    END,
    values=("Zoey Masuda", "9", "14", "B")
)

root.mainloop()