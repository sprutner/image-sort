def main():

        for filename in files:
                splits = filename.split('.')
                if not isJpg(splits):
                        continue
                else:
                        splits.pop(-1)
                        for index, word in enumerate(splits):
                                if remove_numbers(word):
                                        word = ''

                splits2 = splits[0].split()
                folder_name = ' '.join(splits2[:-1])
                fileset.add(folder_name)

        create_directories(fileset)
        copy_files(fileset)


def isJpg(split_string):
        if split_string[-1] == 'jpg':
                return True

def remove_numbers(word):
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

main()



