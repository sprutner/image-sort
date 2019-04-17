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

# Initialization
cwd = os.getcwd()
files = os.listdir(os.getcwd())
fileset = set({})


def main():
    """
    Makes use of functions to list the current working directory and then parses
    the contents to ignore directories and change delimiting characters to
    underscores only. Iterates over these and ignores non-supported image
    formats. Strips off the file extensions and then assumes the directory name
    is everything but the last part of the name after the last underscore. Adds
    these to a set in order to get unique directories. Creates directories in
    ./output and then finally copies the files into the directories by once
    again iterating over the parsed files list.

    Usage: Run sizzle.py in desired directroy.
    """
    parsed_files = parse_files(files, supported_image_formats)

    for filename in parsed_files:
        stripped_file = strip_file_extension(filename)
        fileset.add(get_folder_name(stripped_file))

    create_directories(fileset)
    copy_files(fileset, parsed_files)


def parse_files(file_list, image_formats):
    """
    Takes a list of files and directories as an interable, skips dirs,
    strips whitespace, and then changes all hypens and spaces
    into underscores and returns a list

    :param file_list: list of files
    :return: list of formatted file names
    """

    parsed_file_list = []

    for list_object in file_list:
        if os.path.isdir(list_object):
            continue
        elif not supported_image_file(list_object, image_formats):
            continue
        else:
            list_object.strip()
            parsed_file_list.append(format_file_name(list_object))

    return parsed_file_list


def get_folder_name(filename):
    """
    Splits a formatted filename by underscore, and then assumes everything but
    the last element composes the folder name. Uses slicing to return this as
    the folder name.

    :param filename: string, formatted filename with underscores
    :return: string, just the folder name.
    """
    split_string = filename.split('_')
    folder_name_list = split_string[:-1]
    folder_name = ' '.join(folder_name_list)

    return folder_name


def supported_image_file(filename, image_formats):
    """
    Iterates through a list of supported filetype based on the file extension
    and returns True if filename matches

    :param filename: string, name of file to match
    :param image_formats: list, support file types. Image format from memory.
    :return: Boolean
    """
    split_string = filename.split('.')
    extension = split_string[-1]
    if extension.lower() in image_formats:
        return True


def strip_file_extension(filename):
    """
    Pops off the file name from the full filename with extension
    :param filename: string, full filename
    :return: string, filename before extension
    """
    split_string = filename.split('.')

    return split_string.pop(0)


def format_file_name(file_name):
    """
    Converts hypens and spaces to underscores

    :param file_name: string, name of a file
    :return: string, formatted name of a file
    """

    for letter in file_name:
        if letter == '-' or letter == ' ':
            letter = '_'

    return file_name


def create_directories(fileset):
    """
    Creates directories based on a set of directory names if they don't already
    exist

    :param fileset: Set of strings
    :return: None
    """

    try:
        os.mkdir(os.path.join(cwd, 'output'))
        print("Created output directory")
    except OSError:
        print("Output directory already exists")

    for file in fileset:
        try:
            os.mkdir(os.path.join(cwd, 'output', file))
            print("created directory {} in ./output".format(file))
        except OSError:
            print("Directory {} already exists".format(file))


def copy_files(directories, parsed_files):
    """
    Iterates over the set of unique item names which were used to create
    directories, and then has an inner loop to iterate over the previously
    parsed file names If the beginning of the filenames match up with the
    directory name then, they are copied into the directory

    :param directories: a set of directories
    :param parsed_files: a list of parsed files
    :return: None
    """

    for directory in directories:
        for filename in parsed_files:
            if re.match("{}_.*".format(directory), filename):
                shutil.copy2(filename, os.path.join(cwd, 'output', directory))
            print("[COPIED] {} [TO] {}".format(
                filename,
                os.path.join(cwd, 'output', directory)
                )
            )

if __name__ == "__main__":
    main()
