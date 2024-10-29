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


#TESTING
#if __name__ == "__main__": #
    #students = import_from_file('C:\\Users\\PC\\Downloads\\attendance.csv')
    #add_student("John", "Doe")
    #edit_student("John", "Doe", "Jane", "Doe")
    #export_attendance(students, 'C:\\Users\\PC\\Downloads\\attendance.csv')
  