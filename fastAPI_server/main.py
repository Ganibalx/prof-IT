from fastapi import FastAPI, Depends, UploadFile
from starlette.responses import RedirectResponse

from common import grpc_client, grpc_get_file_list, upload_iterfile, grpc_download_file

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.get('/getfilelist')
async def get_file_list(client=Depends(grpc_client)):
    return await grpc_get_file_list(client)


@app.post('/upload')
async def upload_file(file: UploadFile, client=Depends(grpc_client)):
    response = await client.UploadFile(upload_iterfile(file))
    return response.message


@app.get('/download/{filename}')
async def download_file(filename: str, client=Depends(grpc_client)):
    return await grpc_download_file(filename, client)
