import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mom": "me"}

@app.get("/my_name")
def my_name():
    data = "Theraphat Thamprayot ป่อนป้อน"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name_2(name,last_name):
    data = "{} {}".format(name, last_name)
    return data

@app.get("/samakan")
def samakan(s,t):
    data = (f'V= {float(s)/float(t):.2f}')
   
    return data

@app.get("/series")
async def series(r1,r2,r3):
    parallel = (f'parallel = {float(r1)+float(r2)+float(r3):.2f}')
    serial = (f'serial = {1/float(r1)+1/float(r2)+1/float(r3)**-1:.2f}')
    return  serial,parallel 

print("pond")



if __name__ == "__main__":
    uvicorn.run(app, host="192.168.90.190", port=8080)