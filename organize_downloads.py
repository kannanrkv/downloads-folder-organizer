import os
from pathlib import Path

def organize_downloads(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        ext = Path(file).suffix.lower().replace('.', '')
        if not ext:
            ext = "others"

        target_folder = os.path.join(folder_path, ext)
        os.makedirs(target_folder, exist_ok=True)
        os.rename(file_path, os.path.join(target_folder, file))

    print("✅ Downloads organized by file type!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Organize your downloads folder by file type.")
    parser.add_argument("path", help="Path to your downloads folder (e.g. C:/Users/You/Downloads)")
    args = parser.parse_args()

    organize_downloads(args.path)
