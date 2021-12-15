from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
  return {'data':'Blog list'}

@app.get('/blog/unpublished')
def unpublished():
  return {'data':'All unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
  return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
  return {'data': {'1','2'}}

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=9000)
