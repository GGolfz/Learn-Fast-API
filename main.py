import enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = []
id = 1

class Note(BaseModel):
    name: str
    description: str

@app.get("/notes/")
async def getNotes():
    return data

@app.post("/notes/")
async def createNote(note: Note):
    data.append({"id":id,**note.dict()})
    return data

@app.put("/notes/{note_id}")
async def editNote(note_id,note:Note):
    for index,el in enumerate(data):
        if el["id"] == int(note_id):
            data[index]["name"] = note.name
            data[index]["description"] = note.description
            print(el["id"])
            break
    return data

@app.delete("/notes/{note_id}")
async def deleteNote(note_id):
    target = -1
    for index,el in enumerate(data):
        if el["id"] == int(note_id):
            target = index
            break
    if target != -1:
        data.remove(data[target])
    return data