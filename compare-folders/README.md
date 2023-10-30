# Folder Comparison Tool

This Python script allows users to compare the contents of two directories, taking into account both file names and their contents. It provides an option to exclude specific subfolders from the comparison.

## Features
- **File Name Comparison**: Identifies files that are unique to each folder.
- **Content Comparison**: Detects files with the same name but differing content across the two folders.
- **Subfolder Exclusion**: Allows users to specify subfolders to exclude from the comparison.

## Prerequisites
Ensure you have Python 3.x installed on your system.

## Usage

1. **Run the Script**:
    ```bash
    python compare.py
    ```

2. **Provide Inputs**:
    - Enter the path for Folder A.
    - Enter the path for Folder B.
    - Specify folder names to exclude from the comparison (comma-separated, e.g., `temp, logs, backup`).

3. **View Results**: The script will process the folders and display the comparison results.

## Important Notes
- The comparison only indicates if files with the same name have differing content; it doesn't detail the specific differences.
- The exclusion functionality works on folder names and not paths. So, if "temp" is provided, all folders named "temp" will be excluded irrespective of their location in the directory tree.
- The script reads files as text. Binary files might require a different handling approach. Also, processing very large files might slow down the comparison.

