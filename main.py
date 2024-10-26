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

#EXPORT