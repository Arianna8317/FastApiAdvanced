# Разработать API для управления списком пользователей с
# использованием базы данных SQLite. Для этого создайте
# модель User со следующими полями:
# ○ id: int (идентификатор пользователя, генерируется
# автоматически)
# ○ username: str (имя пользователя)
# ○ email: str (электронная почта пользователя)
# ○ password: str (пароль пользователя)


import uvicorn
from db import database
from fastapi import FastAPI

import users

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
app.include_router(users.router, tags=["users"])
app.include_router(users.router, tags=["products"])
app.include_router(users.router, tags=["orders"])
    

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)