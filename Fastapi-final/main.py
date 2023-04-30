from fastapi import FastAPI
from fastapi import Header    
from pydantic import BaseModel

from fastapi.exceptions import HTTPException


class item(BaseModel):
    element: str       
class item2(BaseModel):
    expr: str       

app = FastAPI()

@app.get("/sum1n/{x}") 
async def read_item(x: int):
    sum = 0
    i = 0
    for i in range(x+1):
        sum=sum+i
    return {"result": sum}

@app.get("/fibo")
async def fibo(n: int):
    fib=[]
    fib.append(0)
    fib.append(1)
    nextn=0
    for i in range(2,n):
        nextn=fib[i-2]+fib[i-1]   
        fib.append(nextn)
    return {"result": fib}


@app.post("/reverse")
async def reverse(string: str = Header(default=None)): 
     new = ""
     for i in string:
         new=str(i)+new   
     return {"result": new}

arr=[]

@app.put("/list")
async def list(gv: item): 
    value=gv.element 
    arr.append(value)
    return  value

@app.get("/list")
async def list():
    return {"result": arr}


@app.post("/calculator")
async def calculator(gv:item2):
    value=gv.expr
    x=value.split(",")
    
    z=x[0]
    y=x[2]
    if not z.isnumeric() or  not y.isnumeric():
        raise HTTPException(400, detail={"error": "invalid"})

    arr1="+-*/"
    a=int(x[0])
    b=int(x[2])
    
    if x[1] not in arr1:
        raise HTTPException(400, detail={"error": "invalid"})

    if x[1]=="-":
        return a-b
    if x[1]=="+":
        return a+b
    if x[1]=="*":
        return a*b
    if x[1]=="/" and b!=0:
        return a/b
    raise HTTPException(403, detail={"error": "zerodiv"})
