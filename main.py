from fastapi import FastAPI
from fastapi_admin.app import app as admin_app

app = FastAPI()
app.mount("/admin", admin_app)

@app.get('/')
async def root():
    return {"message": "Hello world2"}

