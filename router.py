from fastapi import FastAPI,File,UploadFile,APIRouter,Response
api=APIRouter()

@api.post("/dummy-app/")
def test_dummy_app(response:Response,req_id:str=None,file:UploadFile=File(...)):
    resp={"request_id":1256,"application":" Dummy App","Status":"Ok"}
    return resp 