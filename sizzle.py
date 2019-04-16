#!/usr/bin/python

import os
import re
import shutil

# Constants
supported_image_formats = [
    'jpg',
    'jpeg',
    'tif',
    'tiff',
    'gif'
]

# Get cwd
cwd = os.getcwd()
files = os.listdir(os.getcwd())
fileset = set({})


def main():
    parsed_files = parse_files(files)
    for filename in parsed_files:
        if not supported_image_file(filename):
            continue
        else:
            stripped_file = strip_file_extension(filename)
            item_and_folder_name = get_item_and_folder_name(stripped_file)
            # for index, word in enumerate(splits):
            #     if is_digit(word):
            #         word = ''

        # splits2 = splits[0].split()
        # folder_name = ' '.join(splits2[:-1])
        fileset.add(item_and_folder_name['folder_name'])

    create_directories(fileset)
    copy_files(fileset)


def get_item_and_folder_name(filename):
    split_string = filename.split('_')
    item_name = split_string[-1]
    folder_name_list = split_string[:-1]
    folder_name = ' '.join(folder_name_list)

    return {'folder_name': folder_name, 'item_name': item_name}


def supported_image_file(filename, image_formats=supported_image_formats):
    split_string = filename.split('.')
    extension = split_string[-1]
    if extension in image_formats:
        return True


def strip_file_extension(filename):
    split_string = filename.split('.')

    return split_string.pop(0)


def remove_file_extension(filename):
    split_file_name = filename.split('.')
    split_file_name.pop(-1)

    return split_file_name


def format_file_name(file_name):
    for letter in file_name:
        if letter == '-' or letter == ' ':
            letter = '_'

    return file_name


def parse_files(file_list):
    """
    Takes a list of files and directories as an interable, skips dirs,
    strips whitespace, and then changes all hypens and spaces
    into underscores and returns a list

    :param file_list: list
    :return: list of formatted file names
    """
    parsed_file_list = []

    for list_object in file_list:
        if os.path.isdir(list_object):
            continue
        else:
            list_object.strip()
            parsed_file_list.append(format_file_name(list_object))

    return parsed_file_list


def is_digit(word):
    if word.isdigit():
        return True


def create_directories(fileset):
    # Create output dir if not exists
    try:
        os.mkdir(os.path.join(cwd, 'output'))
        print("Created output directory")
    except:
        print("Output directory already exists")

    for file in fileset:
        try:
            os.mkdir(os.path.join(cwd, 'output', file))
            print("created directory {} in ./output".format(file))
        except:
            print("Directory {} already exists".format(file))


def copy_files(fileset):
    for item in fileset:
        for filename in os.listdir(cwd):
            if os.path.isdir(filename):
                continue
            if re.match("{}.*".format(item), filename):
                shutil.copy2(filename, os.path.join(cwd,'output', item))
                print("[COPIED] {} [TO] {}".format(
                    filename,
                    os.path.join(cwd,'output', item)
                    )
                )

if __name__ == "__main__":
    main()



