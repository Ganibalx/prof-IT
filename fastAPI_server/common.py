import os
import grpc
from starlette.responses import FileResponse

from proto import file_server_pb2_grpc, file_server_pb2


async def grpc_client():
    channel = grpc.aio.insecure_channel('localhost:50051')
    return file_server_pb2_grpc.GreeterStub(channel)


async def grpc_get_file_list(client):
    result = []
    async for file in client.GetFileList(file_server_pb2.GetList()):
        result.append(file.message)
    return result


async def upload_iterfile(file, chunk_size=1024):
    metadata = file_server_pb2.MetaData(filename=file.filename)
    yield file_server_pb2.UploadFileRequest(metadata=metadata)
    while True:
        chunk = file.file.read(chunk_size)
        if chunk:
            yield file_server_pb2.UploadFileRequest(file_data=chunk)
        else:
            return


async def grpc_download_file(filename, client):
    file = bytearray()
    files = await grpc_get_file_list(client)
    if filename in files:
        filepath = os.path.join(os.getcwd(), 'download', filename)
        async for entry_response in client.DownloadFile(file_server_pb2.MetaData(filename=filename)):
            file.extend(entry_response.file_data)
        with open(filepath, 'wb') as f:
            f.write(file)
        return FileResponse(path=filepath, media_type="application/octet-stream")
    else:
        return {"message": "Файл отсутствует на сервере"}

