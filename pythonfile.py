import os
import random
import subprocess

# Specify the path to the local directory containing the Git repository
repo_directory = '/home/samael-theflamingsword003/GIT-Everyday/GIT-everyday/GIT-everyday'

# Specify the path to the directory containing the files you want to choose from
source_directory = '/home/samael-theflamingsword003/LEETCODE/CODES'

# Change to the Git repository directory
os.chdir(repo_directory)

# List all files in the source directory
source_files = os.listdir(source_directory)

# Choose a random file from the source directory
random_file = random.choice(source_files)

# Read the content of the random file in binary mode
with open(os.path.join(source_directory, random_file), 'rb') as file:
    lines = file.readlines()

# Initialize the Git repository (if not already)
subprocess.run(['git', 'init'])

# Loop through each line and commit it
for line in lines:
    # Decode bytes to string using UTF-8, ignoring errors
    line_text = line.decode('utf-8', errors='ignore')
    
    # Add the line to a new file (e.g., "temp.txt")
    with open('temp.txt', 'w', encoding='utf-8') as temp_file:
        temp_file.write(line_text)

    # Add the new file to the staging area
    subprocess.run(['git', 'add', 'temp.txt'])

    # Commit the change with the line as the commit message
    subprocess.run(['git', 'commit', '-m', f'Add line: {line_text.strip()}'])

# Clean up the temporary file
os.remove('temp.txt')
