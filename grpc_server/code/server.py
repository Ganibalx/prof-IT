import asyncio
import logging
import os

import grpc

from common import getFileList, saveFile
from proto import file_server_pb2, file_server_pb2_grpc


class Greeter(file_server_pb2_grpc.GreeterServicer):
    async def GetFileList(self, request, context):
        files = await getFileList()
        for i in files:
            yield file_server_pb2.Response(message=i)
        return

    async def UploadFile(self, request_iterator, context):
        file = bytearray()
        filename = ''
        async for request in request_iterator:
            if request.metadata.filename:
                filename = request.metadata.filename
                continue
            file.extend(request.file_data)
        await saveFile(file, filename)
        return file_server_pb2.Response(message=f'{filename} успешно загружен!')

    async def DownloadFile(self, request, context):
        files = await getFileList()
        if request.filename in files:
            filepath = os.path.join(os.getcwd(), 'data', request.filename)
            with open(filepath, 'rb') as f:
                while True:
                    chunk = f.read(1024)
                    if chunk:
                        yield file_server_pb2.DownloadFileResponse(file_data=chunk)
                    else:
                        return


async def serve():
    server = grpc.aio.server()
    file_server_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(serve())