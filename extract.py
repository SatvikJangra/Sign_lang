import os
import shutil


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if (fullPath.endswith('.webp')):
                allFiles.append(fullPath)

    return allFiles


project_path = r'D:\SIGN_LANG'
dirname = os.path.join(project_path, 'path_to_giphy.com')  # Replace 'path_to_giphy.com' with the correct path
dest = os.path.join(project_path, 'gif_extract', 'gif_data')

data = getListOfFiles(dirname)
for i in range(len(data)):
    fname = dest + str(i) + ".webp"
    shutil.copyfile(data[i], fname)
