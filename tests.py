import unittest
import tempfile
import os

import sizzle

# Constants
test_folder_path = tempfile.mkdtemp()
test_output_path = os.path.join(test_folder_path, 'output')
test_files = [
    '33.jpg',
    '23_12.jpg',
    'haunted cabinet 2.jpg',
    'spooky.jpg',
    '23-11-332.jpg',
    'test-table-1.jpg'
]
expected_dirs = [
    '33',
    '23',
    'spooky',
    'haunted_cabinet',
    'test_table'
]

expected_file_paths = [
    '33/33/jpg',
    '23/23_12.jpg',
    '23_11/23_11_332.jpg',
    'haunted_cabinet/haunted_cabinet_2.jpg',
    'spooky/spooky.jpg',
    'test_table/test_table_1.jpg'
]

class TestSizzle(unittest.TestCase):
    def setUp(self):
        # Creates some test files
        for file in test_files:
            open(os.path.join(test_folder_path, file), 'a').close()

    def test_sizzle(self):
        os.chdir(test_folder_path)
        sizzle.set_testing_globals(test_folder_path)
        # print("test folder path {}".format(test_folder_path))
        sizzle.main()
        # print(os.listdir(test_output_path))

        for dir in expected_dirs:
            # print(os.path.join(test_output_path, dir))
            # print(os.path.isdir(os.path.join(test_output_path, dir)))
            assert os.path.isdir(os.path.join(test_output_path, dir)) == True
