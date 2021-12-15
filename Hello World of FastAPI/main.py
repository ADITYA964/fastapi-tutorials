from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
def index():
  return {'data':{'name':'Aditya'}}

@app.get('/about')
def about():
  return {'data':'About page.'}

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=9000)
  
