import os

path = os.getcwd()
DataPath = os.path.join(path, 'Data')

CwdFileList = os.listdir(path)
DataFileList = os.listdir(DataPath)


for file in DataFileList:
    print(
        f'file: {file:<20}  size: {os.path.getsize(os.path.join(DataPath, file)):>5} kb')
