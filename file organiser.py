import os
import pathlib
import shutil

# Dictionary mapping file categories to their extensions
fileformat = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}

# List of file types and their corresponding formats
fileTypes = list(fileformat.keys())
fileformats = list(fileformat.values())

print(fileTypes)
print(fileformats)

# Loop through files in the current directory
for file in os.scandir():
    # Check if the scanned item is a file
    if file.is_file():
        fileName = pathlib.Path(file)
        fileformatType = fileName.suffix.lower()  # Get the file extension

        src = str(fileName)  # Source file path
        dest = "other"  # Default destination folder
        if fileformatType == "":
            print(f"{src} has no file format")
        else:
            # Loop through the defined formats and find the matching folder
            for formats in fileformats:
                if fileformatType in formats:
                    folder = fileTypes[fileformats.index(formats)]  # Find the folder name
                    print(folder)
                    if not os.path.isdir(folder):
                        os.makedirs(folder)  # Create the folder if it doesn't exist
                    dest = folder  # Set the destination folder
                    break

            else:
                if not os.path.isdir("other"):
                    os.makedirs("other")  # Create the 'other' folder if it doesn't exist

        print(f"{src} moved to {dest}!")
        shutil.move(src, dest)  # Move the file to the destination folder

print("File organizer started.")
input("\nPress Enter to exit.")
