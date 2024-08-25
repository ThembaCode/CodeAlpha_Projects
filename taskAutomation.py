import os
import shutil

# Define the paths and mapping for organization
DOWNLOAD_FOLDER = "/path/to/your/download/folder"
ORGANIZED_FOLDER = "/path/to/organized/folder"

# Define how to organize files by extension or keywords
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}

def organize_files():
    for filename in os.listdir(DOWNLOAD_FOLDER):
        # Get the full path of the file
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Identify the category based on extension
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                # Create category folder if it doesn't exist
                category_folder = os.path.join(ORGANIZED_FOLDER, category)
                os.makedirs(category_folder, exist_ok=True)
                
                # Move the file to the appropriate folder
                shutil.move(file_path, os.path.join(category_folder, filename))
                moved = True
                break
        
        if not moved:
            # Optionally, move uncategorized files to a 'Miscellaneous' folder
            misc_folder = os.path.join(ORGANIZED_FOLDER, "Miscellaneous")
            os.makedirs(misc_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(misc_folder, filename))

# Run the organization function
organize_files()
