# image-sort your directories

If you have a mess of image files for multiple listings in
one directory and need to create directories and then
sort the images into the directories, let this script
do that for you

This will parse the filenames and then create the appropriate
directories and then copy the files inside of them

All hypens and spaces will be converted to underscores.
Use of demarcations besides hypens, underscores, or spaces 
in filenames is currently not supported. 

## Easy Installation

Copy paste the following into your terminal

```bash
git clone https://github.com/sprutner/image-sort
bash image-sort/install
```

This clones this repo and adds an alias into your bash_profile or zprofile depending on your shell.

Open a new terminal window and image-sort should now be installed.

## Usage
1) Navigate to your desired directory from the command-line
1) Run `image-sort` from the command line
