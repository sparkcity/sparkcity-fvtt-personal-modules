import os
import re

def select_until_num_or_under(text):
    # Matches everything up to the first digit or underscore
    match = re.match(r'^[^0-9_]*', text)
    return match.group(0)

def rename_images():
    # Define common image extensions to look for
    image_extensions = ('.webp')
    
    # Get all files in the current working directory
    # os.listdir() returns only filenames, not full paths
    files = [f for f in os.listdir('.') if f.lower().endswith(image_extensions)]
    
    # Sort files to ensure a predictable order
    files.sort()
    count = 0
    
    for index, filename in enumerate(files, start=1):
        # Extract the original file extension
        extension = os.path.splitext(filename)[1]

        if select_until_num_or_under(filename) == "kenku":
            
            # Define the new name format (e.g., image1.jpg, image2.jpg)
            new_name = f"kenku{count}{extension}"
            
            # Rename the file
            try:
                os.rename(filename, new_name)
                print(f"Renamed: {filename} -> {new_name}")
                count = count + 1
            except FileExistsError:
                print(f"Error: {new_name} already exists. Skipping {filename}.")

if __name__ == "__main__":
    rename_images()