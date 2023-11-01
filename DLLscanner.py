import os
import ctypes

def find_missing_dlls(directory):
    missing_dlls = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dll'):
                full_path = os.path.join(root, file)
                if not os.path.isfile(full_path):
                    missing_dlls.append(full_path)
    
    return missing_dlls

def main():
    directory_to_scan = "C:\\YourDirectory"  # Change this to the directory you want to scan
    
    if not os.path.exists(directory_to_scan):
        print("Directory not found.")
        return
    
    missing_dlls = find_missing_dlls(directory_to_scan)
    
    if missing_dlls:
        print("Missing DLL files found:")
        for dll in missing_dlls:
            print("File: " + dll)
            print("Severity: High")  # You can enhance this logic based on the specific DLLs
            print("Suggested Fix: Reinstall the software that uses this DLL or restore it from a backup.")
            print()
    else:
        print("No missing DLL files found.")

if __name__ == "__main":
    main()

