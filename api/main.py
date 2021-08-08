from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get('/')
async def root():
    return {"message":"Hello from AWS Lambda!"}


handler = Mangum(app=app)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)