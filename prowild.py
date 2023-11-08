import ast
import pickle
from datetime import date
import pathlib
import os
from pathlib import Path
import shutil
import hashlib

class Add:
    def __init__(self, cwd):
        self.cwd = cwd
    def reg(self):
        user = input("User: ")
        password = input("Password: ")
        file_name = 'empty.txt'
        with open(file_name, 'a') as f:
            f.write((user)+ '\n')
        hash_object = hashlib.sha256()
        hashed_password = hash_object.update(password.encode())
        hashed_password_hex = hash_object.hexdigest()
        with open(file_name, 'a') as f:
            f.write((hashed_password_hex)+ '\n')
    def add_task(self):
        task_number = input("Number of your task: ")
        task_name = input("Name of your task: ")
        task_description = input("Describe your task: ")
        task_priority = input("Priority of your task: ")
        task_dedline = input("Dedline of your task: ")
        task_status = input("Status of your task: ")
        task = f"number: {task_number} | name: {task_name} | description: {task_description} | priority: {task_priority} | dedline: {task_dedline} | status: {task_status}"
        
        with open("empty.txt", 'a') as f:
            f.write(task + "\n")

    def show_tasks(self):
        qw = Path('empty.txt')
        file_content = qw.read_text()
        print(file_content)
    def delete_task(self):
        ad = Add.show_tasks()
        index = int(input("Which task you want to delete: ")) - 1
        if 0 <= index < len(ad):
            task = ad[index]
            ad.remove_task(task)
            print("The task has been deleted")
    def todays_task(self):
        today = date.today()
        with open("empty.txt", 'r') as f:
            for i in f:
                line_split = i.split()
                if line_split == today:
                    print(line_split)



 