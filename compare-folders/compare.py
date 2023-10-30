import os

def list_files(folder, exclusions):
    """Return a set of all file paths in the folder, relative to the folder, excluding specified subfolders."""
    return set(
        os.path.relpath(os.path.join(dirpath, file), folder)
        for dirpath, dirnames, filenames in os.walk(folder)
        for file in filenames if not any(excl in dirpath for excl in exclusions)
    )

def compare_folders(folderA, folderB, exclusions):
    """Compare files in two folders and output differences."""
    filesA = list_files(folderA, exclusions)
    filesB = list_files(folderB, exclusions)
    
    onlyInA = filesA - filesB
    onlyInB = filesB - filesA
    commonFiles = filesA & filesB
    
    differingFiles = []
    for file in commonFiles:
        with open(os.path.join(folderA, file), 'r', errors='ignore') as fA, \
             open(os.path.join(folderB, file), 'r', errors='ignore') as fB:
            if fA.read() != fB.read():
                differingFiles.append(file)
    
    # Prepare output
    output = []

    if onlyInA or onlyInB:
        if len(onlyInA) > len(onlyInB):
            output.append(f"Folder A has {len(onlyInA) - len(onlyInB)} more files than Folder B.")
        elif len(onlyInB) > len(onlyInA):
            output.append(f"Folder B has {len(onlyInB) - len(onlyInA)} more files than Folder A.")
        
        if onlyInA:
            output.append("\nFiles only in Folder A:")
            for file in onlyInA:
                output.append(f"- {file}")
        
        if onlyInB:
            output.append("\nFiles only in Folder B:")
            for file in onlyInB:
                output.append(f"- {file}")

    if differingFiles:
        output.append("\nThe names of the files that have different content are:")
        for file in differingFiles:
            output.append(f"- {file}")
    
    if not differingFiles and not onlyInA and not onlyInB:
        output.append("\nBoth folders are identical.")

    # Print accumulated output
    for line in output:
        print(line)

if __name__ == "__main__":
    folderA = input("Enter the path for Folder A: ")
    folderB = input("Enter the path for Folder B: ")
    exclusions_input = input("Enter folder names to exclude (comma-separated): ")
    exclusions = [x.strip() for x in exclusions_input.split(",")]
    
    compare_folders(folderA, folderB, exclusions)

