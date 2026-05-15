from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/',summary="Main branch", tags=['Main'])
def root():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run('main:app', reload = True)

# or on terminal use command
# uvicorn main:app --reload
