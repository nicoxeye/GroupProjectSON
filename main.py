#IMPORT
def import_from_file(filepath):
    students = []
    with open(filepath, 'r') as file: #'r' read file
        for line in file:
            cut_parts = line.strip().split(',') #delete whitespaces and create a seperator as ,
            #in the file: first name, last name
            if len(cut_parts) == 2 or len(cut_parts) == 3: # <- check if theres the first name and last name in the file OR WITH ATTENDANCE ALREADY WRITTEN
                students.append({
                    'first_name': cut_parts[0].strip(),
                    'last_name': cut_parts[1].strip(),
                    'present': False #automatically adds false to if someone is present
                    })
            else: print('something went wrong when importing the file.')
    return students
# can probably add an except to return an error if it doesnt find the file but idrk how to do that:3

#EXPORT

def export_attendance(students, filepath):
     with open(filepath, 'w') as file: #'w' write file
        for student in students:
            present = 'yes' if student['present'] else 'no'
            file.write(f"{student['first_name']},{student['last_name']},{present}\n")


# TESTING
#if __name__ == "__main__": #
    #students = import_from_file('C:\\Users\\PC\\Downloads\\attendance.txt')
 
    #export_attendance(students, 'C:\\Users\\PC\\Downloads\\attendance.txt')