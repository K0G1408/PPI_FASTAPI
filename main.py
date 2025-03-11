from fastapi import FastAPI

app = FastAPI()

@app.get("/nombres")
async def obtener_nombres():
    return ["Juan", "María", "Pedro"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
