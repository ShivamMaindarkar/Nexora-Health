from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Nexora Health API running'}