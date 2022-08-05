import os
import shutil
import tempfile
from pathlib import Path

final_dir_name = str(input('What is the name and volume of the manga you '
                         'are compiling (ex: chainsaw man volume 1): '))

# final_dir_name = final_dir_name.replace(" ", "-")
# final_dir_name = "Chainsaw Man Volume " + final_dir_name

# get basic download path to access downloaded files
downloads_path = str(Path.home() / "Downloads")

# make new directory path in downloads from given name and volume
final_dir_path = os.path.join(downloads_path, final_dir_name)

# makes a new directory from new path - kinda unnecessary
os.mkdir(final_dir_path)


# self-explanatory; choose what chapters you want in said volume
chapter_start = int(input('What Chapter are you starting at: '))
chapter_end = int(input('What Chapter are you ending at: '))

# Give the general download name that can be iterated through for each chapter
general_download_name = str(input("What is the name of the downloaded compressed files "
                                  "including file type and a # symbol for the chapter number "
                                  "(ex: chainsaw-man-#.zip): "))

# general_download_name = "chainsaw-man-#.zip"

gen_download_path = str(input('Enter the path to find the downloaded files: '))

# Creates path to general download name
# gen_download_path = os.path.join(downloads_path, general_download_name)

gen_download_path = os.path.join(gen_download_path, general_download_name)

# Below turned out useless rip
# Iterable for counting files in each chapter. Saves to list in preparation to rename
# for chapter in range(chapter_end - chapter_start + 1):
#     chapter_num = str(chapter + 1)
#
#     # Replace general download path with specific chapter path
#     iter_dir_path = gen_download_path.replace("#", chapter_num)
#
#     # make a temp directory to count the # of files in chapter
#     with tempfile.TemporaryDirectory() as count_dir:
#
#         # unpack files into temp directory
#         shutil.unpack_archive(iter_dir_path, count_dir)
#
#         # count files in temp directory
#         count = len(os.listdir(count_dir))
#         chapter_page_count.append(count)
#
# print(chapter_page_count)

pic_count = 0

for chapter in range(chapter_start, chapter_end + 1):
    chapter_num = str(chapter)
    iter_dir_path = gen_download_path.replace("#", chapter_num)

    # make a temp directory to unpack files for rename/move
    with tempfile.TemporaryDirectory() as rename_dir:

        # unpack files into temp directory
        shutil.unpack_archive(iter_dir_path, rename_dir)

        for pic in os.listdir(rename_dir):

            # Get path for pic
            old_name = os.path.join(rename_dir, str(pic))

            # Create new path for pic in final directory and changing name to pic count
            new_name = os.path.join(final_dir_path, str(pic_count) + ".png")

            # Rename path (moves file)
            os.rename(old_name, new_name)

            pic_count += 1

archive = shutil.make_archive(final_dir_path, 'zip', final_dir_path)
print(archive)


# convert file type from .zip to .cbz
base = os.path.splitext(archive)[0]

os.rename(archive, base + '.cbz')
