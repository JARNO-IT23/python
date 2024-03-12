import tkinter as tk
from tkinter import ttk, filedialog
import csv
import os


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Õpilaste Haldamise Süsteem")
        self.students = []
        self.load_students()
        self.create_gui()

    def create_gui(self):
        input_frame = ttk.LabelFrame(self.root, text="Andmete Sisestamine")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(input_frame, text="Nimi:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Isikukood:").grid(row=1, column=0, sticky="w")
        self.id_code_entry = ttk.Entry(input_frame)
        self.id_code_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Kursus:").grid(row=2, column=0, sticky="w")
        self.course_entry = ttk.Entry(input_frame)
        self.course_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Pilt:").grid(row=3, column=0, sticky="w")
        self.image_path = tk.StringVar()
        self.image_path.set("")
        ttk.Entry(input_frame, textvariable=self.image_path, state="readonly").grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(input_frame, text="Laadi üles pilt", command=self.upload_image).grid(row=3, column=2, padx=5, pady=5)

        ttk.Button(input_frame, text="Lisa Õpilane", command=self.add_student).grid(row=4, column=0, columnspan=3, pady=10)
        ttk.Button(input_frame, text="Muuda Õpilane", command=self.edit_student).grid(row=5, column=0, columnspan=3, pady=10)
        ttk.Button(input_frame, text="Salvesta Muudatused", command=self.save_changes).grid(row=5, column=4, columnspan=3, pady=10)
        ttk.Button(input_frame, text="Kustuta Õpilane", command=self.delete_student).grid(row=6, column=0, columnspan=3, pady=10)
        display_frame = ttk.LabelFrame(self.root, text="Andmete Kuvamine")
        display_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        columns = ("ID", "Nimi", "Isikukood", "Kursus", "Pilt")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.grid(row=0, column=0, padx=5, pady=5)
       

        self.refresh_treeview()

    def add_student(self, edit_index=None):
        name, id_code, course, image_path = self.name_entry.get(), self.id_code_entry.get(), self.course_entry.get(), self.image_path.get()
        if name and id_code and course:
            if edit_index is not None:
                self.students[edit_index] = (edit_index + 1, name, id_code, course, image_path)
            else:
                student_id = len(self.students) + 1
                student = (student_id, name, id_code, course, image_path)
                self.students.append(student)

            image_extension = os.path.splitext(image_path)[1]
            image_save_path = f"{id_code}{image_extension.lower()}"
            self.save_image(image_path, image_save_path)

            self.save_to_csv()
            self.refresh_treeview()
            self.name_entry.delete(0, tk.END)
            self.id_code_entry.delete(0, tk.END)
            self.course_entry.delete(0, tk.END)
            self.image_path.set("")

    def edit_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            student_id = self.tree.item(selected_item, "values")[0]
            index = int(student_id) - 1
            current_student = self.students[index]

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, current_student[1])
            self.id_code_entry.delete(0, tk.END)
            self.id_code_entry.insert(0, current_student[2])
            self.course_entry.delete(0, tk.END)
            self.course_entry.insert(0, current_student[3])
            self.image_path.set(current_student[4])

            ttk.Button(input_frame, text="Lisa Õpilane", command=lambda: self.add_student(edit_index=index)).grid(row=4, column=0, columnspan=3, pady=10)
    
    def save_changes(self):
        selected_item = self.tree.selection()
        if selected_item:
            student_id = self.tree.item(selected_item, "values")[0]
            index = int(student_id) - 1
            self.add_student(edit_index=index)
    
    
    def delete_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            student_id = self.tree.item(selected_item, "values")[0]
            index = int(student_id) - 1
            self.students.pop(index)
            self.save_to_csv()
            self.refresh_treeview()

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Vali pilt", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.image_path.set(file_path)

    def save_to_csv(self):
        file_path = "students.csv"
        file_exists = os.path.exists(file_path)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nimi", "Isikukood", "Kursus", "Pilt"])
            for student in self.students:
                writer.writerow(student)

        if not file_exists:
            print(f"Loon uue faili: {file_path}")

    def save_image(self, source_path, dest_path):
        try:
            image = Image.open(source_path)
            image.save(dest_path)
        except Exception as e:
            print(f"Error saving image: {e}")

    def load_students(self):
        file_path = "students.csv"
        if os.path.exists(file_path):
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    self.students.append(tuple(row))

    def refresh_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for student in self.students:
            self.tree.insert("", tk.END, values=student)

   

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()

   
