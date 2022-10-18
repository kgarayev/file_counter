# Add the code for the file counter script that you wrote in the course.
import pathlib, pprint, csv

# find the path to the current directory
path = pathlib.Path().cwd()

# moves one type of files into a dedicated folder
def move_filetype(path, type):
    # create a new folder
    new_path = pathlib.Path(str(path)+ '/' + type)
    new_path.mkdir(exist_ok=True)

    for filepath in path.iterdir():
        # filter for text files only
        if filepath.suffix == type:
            # create a new path for each file
            new_filepath = new_path.joinpath(filepath.name)
            # move the file there
            filepath.replace(new_filepath)
    
    return new_path

# counts various types of files in the given directory
def file_counter(path):
    # create a dictionary to record all the files
    count = {}

    for filepath in path.iterdir():
        # filter for various file types and record the count
        if filepath.suffix in count:
            count[filepath.suffix] += 1
        else:
            count[filepath.suffix] = 1
    
    types = count.keys()

    with open("filecounts.csv", "w") as csvfile:
        countwriter = csv.DictWriter(csvfile, fieldnames=types)
        countwriter.writeheader()
        countwriter.writerow(count)

    pprint.pprint(count)
    return count

# moves files more than or equal to quant into a dedicated folder given a dictionary of files
def move_files(path, quant: int, file_record: dict):
    # iterate through the dictionary
    for key in file_record:
        # filer the filetypes that have quant or more files 
        if file_record[key]>=quant:
            # move the filetype into its dedicated folder
            move_filetype(path, key)
    
    return 

file_counter(path)
#move_filetype(path, '.txt')
#move_files(path, 5, file_counter(path))

#file_in = open("all_files.txt", "r")
#contents = file_in.read()
#file_in.close()
#print(type(contents))
#dassag = dict(contents)

