# pip install fastapi uvicorn
# uvicorn fastapi:app --reload

from fastapi import FastAPI

app = FastAPI()

# 根路径，返回一个简单的问候消息
@app.get("/")
def read_root():
    return {"message": "hello, shuaige"}

# 获取特定用户得信息
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"userid": user_id, "name": f"User {user_id}"}

# 创建一个新用户， 接受json格式的请求体
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/user/")
def create_user(user: User):
    return {"message": f"User {user.name} aged {user.age} created successfully"}