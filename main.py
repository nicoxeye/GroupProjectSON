import os
import csv

#IMPORT
def import_from_file(filename="students.csv"):
    students = []
    try:
        with open(filename, 'r', newline='') as file: #'r' read file, newline='' to manage newline characters correctly in CSV files
            for line in file:
                cut_parts = line.strip().split(',') #delete whitespaces and create a seperator as ,
                #in the file: first name, last name
                if len(cut_parts) == 2:  #no attendance provided
                    students.append({
                        'first_name': cut_parts[0].strip(),
                        'last_name': cut_parts[1].strip(),
                        'present': False  #default to False
                    })
                elif len(cut_parts) == 3:  #attendance provided
                    students.append({
                        'first_name': cut_parts[0].strip(),
                        'last_name': cut_parts[1].strip(),
                        'present': cut_parts[2].strip().lower() == 'yes'  #convert to boolean, 'yes' == True
                    })
                else: print('Something went wrong when importing the file.')
        return students
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.") #added if filenotfound exception

#EXPORT

def export_attendance(students, filename="students.csv"):
     with open(filename, 'w', newline='') as file: #'w' write file
        for student in students:
            present = 'yes' if student['present'] else 'no'
            file.write(f"{student['first_name']},{student['last_name']},{present}\n")

            
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

            
#TESTING
#if __name__ == "__main__": #
    #students = import_from_file('C:\\Users\\PC\\Downloads\\attendance.csv')
    #add_student("John", "Doe")
    #edit_student("John", "Doe", "Jane", "Doe")
    #export_attendance(students, 'C:\\Users\\PC\\Downloads\\attendance.csv')
  
