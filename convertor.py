import markdown
import os


# get files in a folder
def get_files(path):
    files = os.listdir(path)
    # get only files from path specified.
    files = [f for f in files if os.path.isfile(path + '/' + f)]
    return files


# get file name
def get_file_name(file_name_with_extension):
    filename, file_extension = os.path.splitext(file_name_with_extension)
    return filename


def convert_markdown(file_name):
    # read and convert the content of the file
    with open(file_name, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    file_name_no_extension = get_file_name(file_name)
    # define header and footer for the html page
    head = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{file_name_no_extension}</title>
    </head>
    <body>"""
    foot = """</body>
    </html>"""

    # create the html page
    with open(get_file_name(file_name), 'w') as f:
        f.write(head)
        f.write(html)
        f.write(foot)


if __name__ == '__main__':
    # path = 'E:\PROJECTS\python\markdown-convertor\samples'
    path = input("Enter path to directory: ")
    # get files in the directory
    files = get_files(path)
    # loop through each to get the filename
    for file_name in files:
        # convert files to html
        print(file_name)
        convert_markdown(path + "\\" + file_name)
