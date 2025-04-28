from fastapi import FastAPI, status

import uvicorn
app = FastAPI()

@app.get("/ping/")
async def root():
    return {'message': 'pong',
            'statusCode': status.HTTP_200_OK
            }