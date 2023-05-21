
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    print('hola')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=15400)


