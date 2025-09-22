# Certificate Generator Project
# TODO: Create personalized certificates using certificate_template.txt
# for each student in student_list.txt
# Replace the [STUDENT_NAME] placeholder with the actual name
# Replace the [COURSE_NAME] placeholder with the course from course_info.txt
# Replace the [DATE] placeholder with today's date
# Save the certificates in the folder "CompletedCertificates"

# Hint1: This method will help you read files: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will help you replace text: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you clean whitespace: https://www.w3schools.com/python/ref_string_strip.asp
# Hint4: Use datetime module for current date: from datetime import datetime
# Hint5: Format date nicely with: datetime.now().strftime("%B %d, %Y")

# Expected folder structure:
# /Users/adricati/Personal Development/intermediate-python-projects/22_files_dictionaries_paths/certificate_generator_project/
# ├── Input/
# │   ├── Template/
# │   │   └── certificate_template.txt
# │   ├── Course/
# │   │   └── course_info.txt
# │   └── Students/
# │       └── student_list.txt
# └── Output/
#     └── CompletedCertificates/



from datetime import datetime
# Use the full path from the project root

#read the template file
with open("22_files_dictionaries_paths/certificate_generator_project/Input/Template/certificate_template.txt", "r") as template_file:
    template_content = template_file.readlines()
    
#read the course file
with open("22_files_dictionaries_paths/certificate_generator_project/Input/Course/course_info.txt", "r") as course_file:
    course_name = course_file.read().strip()
    
#read the student names file
with open("22_files_dictionaries_paths/certificate_generator_project/Input/Students/student_list.txt", "r") as names_file:
    student_names = names_file.readlines()
    for name in student_names:
        stripped_name = name.strip()
        new_certification = ""
        for line in template_content:
            new_line = line.replace("[STUDENT_NAME]", stripped_name)
            new_line = new_line.replace("[COURSE_NAME]", course_name)
            new_line = new_line.replace("[DATE]", datetime.now().strftime("%B %d, %Y"))
            new_certification += new_line
        with open(f"22_files_dictionaries_paths/certificate_generator_project/Output/CompletedCertificates/certificate_for_{stripped_name}.txt", mode="w") as completed_certificate:
            completed_certificate.write(new_certification)


print("Certificates generated successfully!")