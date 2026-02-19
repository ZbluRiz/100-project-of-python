import csv
from pathlib import Path

def studentData(inputFile,outputFile):
    try:
        #read the file
        with open(inputFile,'r') as infile:
            reader = csv.DictReader(infile)
            studentsReport = []
            
            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math + science + english) / 3,2)
                status = "Pass" if average >= 60 else "Fail"
                
                studentsReport.append({
                    'Name': name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average' : average,
                    'Status':status
                })
            
        #write the file
        with open(outputFile,'w') as outfile:
            fieldnames = ['Name','Math','Science','English','Average','Status']
            writer = csv.DictWriter(outfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(studentsReport)
        
        print(f'Students report generated in {outputFile} succesfully')
        
    except FileNotFoundError :
        print(f"Error: file {inputFile} not found!")
    except KeyError:
        print("Invalid Column names in the input files")
    except Exception as e:
        print(f'an error occured {e}')

BASE_DIR = Path(__file__).parent
input_file = BASE_DIR / 'students.csv'
output_file = BASE_DIR / 'studentsReport.csv'

studentData(input_file,output_file)