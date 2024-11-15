import os
import random

from proto import file_server_pb2


async def getFileList():
    for dir_path, dir_name, file_name in os.walk(os.path.join(os.getcwd(), 'data')):
        return file_name


async def rename(filename):
    filelist = await getFileList()
    if filename in filelist:
        ext = filename.split('.')[-1:][0]
        filename = filename.strip('.' + ext) + str(random.getrandbits(10)) + '.' + ext
    return filename


async def saveFile(file, filename):
    filename = await rename(filename)
    filepath = os.path.join(os.getcwd(), 'data', filename)
    with open(filepath, 'wb') as f:
        f.write(file)


