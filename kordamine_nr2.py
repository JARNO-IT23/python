import tkinter as tk
from tkinter import messagebox
import csv
import os
from uuid import uuid4
from tkinter import filedialog



class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Õpilaste Haldamise Süsteem")
        self.students = []
        self.label_name = tk.Label(root, text="Nimi:")
        self.label_id = tk.Label(root, text="Isikukood:")
        self.label_course = tk.Label(root, text="Kursus:")
        self.label_image = tk.Label(root, text="Pilt:")
        self.entry_name = tk.Entry(root)
        self.entry_id = tk.Entry(root)
        self.entry_course = tk.Entry(root)
        self.entry_image = tk.Entry(root)
        self.btn_upload_image = tk.Button(root, text="Laadi üles pilt", command=self.upload_image)
        self.btn_add_student = tk.Button(root, text="Lisa õpilane", command=self.add_student)
        self.btn_show_students = tk.Button(root, text="Kuva õpilased", command=self.show_students)
        self.btn_save_data = tk.Button(root, text="Salvesta andmed", command=self.save_data)
        self.btn_search_by_id = tk.Button(root, text="Otsi ID järgi", command=self.search_by_id)
        self.btn_edit_student = tk.Button(root, text="Muuda õpilast", command=self.edit_student)
        self.btn_delete_student = tk.Button(root, text="Kustuta õpilane", command=self.delete_student)
        self.label_name.grid(row=0, column=0)
        self.label_id.grid(row=1, column=0)
        self.label_course.grid(row=2, column=0)
        self.label_image.grid(row=3, column=0)
        self.entry_name.grid(row=0, column=1)
        self.entry_id.grid(row=1, column=1)
        self.entry_course.grid(row=2, column=1)
        self.entry_image.grid(row=3, column=1)
        self.btn_upload_image.grid(row=4, column=0, columnspan=2)
        self.btn_add_student.grid(row=5, column=0, columnspan=2)
        self.btn_show_students.grid(row=6, column=0, columnspan=2)
        self.btn_save_data.grid(row=7, column=0, columnspan=2)
        self.btn_search_by_id.grid(row=8, column=0, columnspan=2)
        self.btn_edit_student.grid(row=9, column=0, columnspan=2)
        self.btn_delete_student.grid(row=10, column=0, columnspan=2)

    def upload_image(self):
        # Lae üles pilt ja kuvab see GUI-s
        file_path = filedialog.askopenfilename(title="Vali pilt", filetypes=[("Pildifailid", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = image.resize((150, 150), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo
            self.image_path = file_path

    
        

    def add_student(self):
        name = self.entry_name.get()
        student_id = str(uuid4())  
        course = self.entry_course.get()
        image_filename = f"{student_id}.png"
        self.students.append({"id": student_id, "name": name, "course": course, "image": image_filename})
        messagebox.showinfo("Info", "Õpilane lisatud edukalt!")

    def show_students(self):
        for student in self.students:
            print(f"ID: {student['id']}, Nimi: {student['name']}, Kursus: {student['course']}, Pilt: {student['image']}")
    def save_data(self):
        filename = self.ask_file_to_save()
        if filename:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nimi", "Kursus", "Pilt"])
                for student in self.students:
                    writer.writerow([student["id"], student["name"], student["course"], student["image_path"]])
            messagebox.showinfo("Info", "Andmed on edukalt salvestatud!")
    def ask_file_to_save(self):
        return filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV failid", "*.csv")])
       
    def search_by_id(self):
        search_id = self.entry_id.get()
        for student in self.students:
            if student["id"] == search_id:
                print(f"ID: {student['id']}, Nimi: {student['name']}, Kursus: {student['course']}, Pilt: {student['image']}")
                break
        else:
            messagebox.showinfo("Info", "Õpilast ID-ga {} ei leitud.".format(search_id))
    def edit_student(self):
        pass
    def delete_student(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()     