import os
import time


def file_organizer(src_path: str, dst_path: str) -> None:
    def copy_file(src: str, dst: str) -> None:
        """ Copy files from source to destination """
        try:
            with open(src, 'rb') as src_file, open(os.path.join(dst, os.path.basename(src)), 'wb') as dst_file:
                dst_file.write(src_file.read())
        except FileExistsError:
            pass
        except PermissionError:
            print(f"ERROR: Permission denied to access {dst}")
        except Exception as e:
            print(f"ERROR: An error occurred: {e}")

    photos_format = ['.jpg', '.png', '.jpeg']
    videos_format = ["mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov"]
    files_to_organize = [files for files in os.listdir(src_path)]
    years = []

    for file_name in files_to_organize:
        mod_time = time.ctime(os.path.getmtime(os.path.join(src_path, file_name)))
        year = mod_time[20:len(mod_time):1]
        if year not in years:
            years.append(year)

    try:
        os.chdir(dst_path)
        os.mkdir("Organized_Files")
        print("\"Organized files\" folder created")
    except FileExistsError:
        pass

    for year in years:
        for file_name in files_to_organize:
            os.chdir(dst_path + r"\Organized_Files")

            try:
                os.mkdir(year)
            except FileExistsError:
                pass

            os.chdir(year)
            for ext in photos_format:
                if file_name.lower().endswith(ext):
                    try:
                        os.mkdir("Photos")
                        print(f"\"Photos\" folder {year} created")
                    except FileExistsError:
                        pass

            for ext in videos_format:
                if file_name.lower().endswith(ext):
                    try:
                        os.mkdir("Videos")
                        print(f"\"Videos\" folder {year} created")
                    except FileExistsError:
                        pass

    # The below code will copy/paste the files from the src_path to dst_path
    file_number = 0
    for file_name in files_to_organize:
        mod_time = time.ctime(os.path.getmtime(os.path.join(src_path, file_name)))
        cur_file_year = mod_time[20:len(mod_time):1]

        if os.path.isfile(os.path.join(src_path, file_name)):
            for year in years:
                for ext in photos_format:
                    if file_name.lower().endswith(ext) and year == cur_file_year:
                        copy_file(os.path.join(src_path, file_name),
                                  (os.path.join(dst_path + r"\Organized_Files", year)) + r"\Photos")

                for ext in videos_format:
                    if file_name.lower().endswith(ext) and year == cur_file_year:
                        copy_file(os.path.join(src_path, file_name),
                                  (os.path.join(dst_path + r"\Organized_Files", year)) + r"\Videos")
            file_number += 1
            print(f"File {file_number} moved successfully")


file_organizer(r"Enter the source path here (absolute path)", r"Enter the destination path here (absolute path)")
