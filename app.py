import uvicorn 
from fastapi import FastAPI
import router 
from router import api 



app=FastAPI(docs_url="/docs",redoc_url="/redocs",title="Dummy_api",
            version="2.0")

app.include_router(router.api)
if __name__=="__main__":
    uvicorn.run(app)