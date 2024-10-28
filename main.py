import csv
import os

#IMPORT
def import_from_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            cut_parts = line.strip().split(',') #delete whitespaces and create a seperator as ,
            #in the file: first name, last name
            if len(cut_parts) == 2: # <- check if theres the first name and last name in the file
                students.append
                (
                    {
                    'first_name': cut_parts[0].strip(),
                    'last_name': cut_parts[1].strip(),
                    'present': False #automatically adds false to if someone is present
                    }
                )
            else: print('something went wrong when importing the file.')
# can probably add an except to return an error if it doesnt find the file but idrk how to do that:3
            
#ADDING NEW STUDENTS AND UPDATING DATABASE

# function that adds new student to the list and saves it to the file
def add_student(first_name, last_name, filename="students.csv"):
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["first_name", "last_name", "present"])
        
        # "present" is false by default
        writer.writerow([first_name, last_name, False])
    print(f"Student {first_name} {last_name} was added to {filename}.")

# function that edits student list
def edit_student(old_first_name, old_last_name, new_first_name, new_last_name, filename="students.csv"):
    students = []
    updated = False

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["first_name"] == old_first_name and row["last_name"] == old_last_name:
                row["first_name"] = new_first_name
                row["last_name"] = new_last_name
                updated = True
            students.append(row)
    
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "present"])
        writer.writeheader()
        writer.writerows(students)
    
    if updated:
        print(f"Student: {old_first_name} {old_last_name} has been updated to {new_first_name} {new_last_name}.")
    else:
        print("The student hasn't been found")

            