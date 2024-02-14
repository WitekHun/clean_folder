import os
from pathlib import Path
import shutil
import sys
from datetime import datetime

dir_list = []
images_list = []
docs_list = []
audio_list = []
video_list = []
archives_list = []
IMAGES_EXTENSIONS = [".jpeg", ".png", ".jpg", ".svg"]
VIDEO_EXTENSIONS = [".avi", ".mp4", ".mov", ".mkv"]
DOCS_EXTENSIONS = [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"]
AUDIO_EXTENSIONS = [".mp3", ".ogg", ".wav", ".amr"]
ARCHIVE_EXTENSIONS = [".zip", ".gz", ".tar"]


def time_log(func):
    # start_time = datetime.now()
    print(f"Starting function on folder {sys.argv[1]}")
    start_time = datetime.now()

    def inner(dir):
        # print(f"Starting function on folder {sys.argv[1]}")
        # start_time = datetime.now()
        result = func(dir)
        print(f"time elapsed: {datetime.now()-start_time}")
        return result

    return inner


@time_log
def files_list(dir):
    directory = Path(dir)
    sorted_path = (Path(sys.argv[1])).parent
    logs_path = os.path.join(sorted_path, "Logs")
    sorted_dir = os.path.join(sorted_path, "Sorted")
    images_dir = os.path.join(sorted_dir, "Images")
    video_dir = os.path.join(sorted_dir, "Video")
    docs_dir = os.path.join(sorted_dir, "Documents")
    audio_dir = os.path.join(sorted_dir, "Audio")
    all_list = os.listdir(sys.argv[1])
    with open(f"{logs_path}/lista.txt", "a") as fh:
        fh.write("Lista plików \n")
    with open(f"{logs_path}/first_list.txt", "a") as fh:
        fh.write(f"Pliki i foldery w Mixed os.listdir(sys.argv[1]): {str(all_list)} \n")
    for i in directory.iterdir():
        p = Path(i)

        if i.is_dir():
            if i not in dir_list:
                dir_list.append(p)
                with open(f"{logs_path}/direct_list.txt", "a") as fh:
                    fh.write(f"{dir_list} \n")
            files_list(str(p))
        else:
            with open(f"{logs_path}/file_list.txt", "a") as fh:
                fh.write(f"{os.path.join(directory, i)} Is file \n")
            if p.suffix in IMAGES_EXTENSIONS:
                add_and_move_file(images_list, os.path.join(directory, i), images_dir)
                with open(f"{logs_path}/lista.txt", "a") as fh:
                    fh.write(f"{str(i)} \n")
            elif p.suffix in VIDEO_EXTENSIONS:
                add_and_move_file(video_list, os.path.join(directory, i), video_dir)
                with open(f"{logs_path}/lista.txt", "a") as fh:
                    fh.write(f"{str(i)} \n")
            elif p.suffix in DOCS_EXTENSIONS:
                add_and_move_file(docs_list, os.path.join(directory, i), docs_dir)
                with open(f"{logs_path}/lista.txt", "a") as fh:
                    fh.write(f"{str(i)} \n")
            elif p.suffix in AUDIO_EXTENSIONS:
                add_and_move_file(audio_list, os.path.join(directory, i), audio_dir)
                with open(f"{logs_path}/lista.txt", "a") as fh:
                    fh.write(f"{str(i)} \n")
    # for i in dir_list[::-1]:
    i = 0
    while i < len(dir_list):
        if (
            dir_list[::-1][i].is_dir()
            and len([x for x in (dir_list[::-1][i]).iterdir()]) == 0
        ):
            print(f"{i} ODWROCONA LISTA KATALOGOW {dir_list[::-1][i]}")
            os.rmdir(dir_list[::-1][i])
            i += 1
        else:
            break


def add_and_move_file(array, file, directory):
    array.append(file)
    shutil.move(file, directory)


def images_file(file, directory):
    images_list.append(file)
    shutil.move(file, directory)


def audio_file(file, directory):
    audio_list.append(file)
    shutil.move(file, directory)


def video_file(file, directory):
    video_list.append(file)
    shutil.move(file, directory)


def archives_file(file, directory):
    archives_list.append(file)
    shutil.move(file, directory)


def mk_dir(dir, directory):
    if directory in os.listdir(dir):
        print(f"{dir}/{directory} already exist")
    else:
        os.mkdir(Path(f"{dir}/{directory}"))


if __name__ == "__main__":
    mk_dir((Path(sys.argv[1])).parent, "Logs")
    sorted_path = os.path.join(((Path(sys.argv[1])).parent), "Sorted")
    mk_dir((Path(sys.argv[1])).parent, "Sorted")
    mk_dir(sorted_path, "Images")
    mk_dir(sorted_path, "Videos")
    mk_dir(sorted_path, "Documents")
    mk_dir(sorted_path, "Audio")
    mk_dir(sorted_path, "Archives")
    files_list(sys.argv[1])
