from fastapi import FastAPI, HTTPException
import os

app = FastAPI()


NOTES_FOLDER = "notes"
os.makedirs(NOTES_FOLDER, exist_ok=True)  


@app.post("/notes/")
def create_note(title: str, content: str):
    file_path = os.path.join(NOTES_FOLDER, f"{title}.txt")

    if os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="Note already exists")

    with open(file_path, "w") as file:
        file.write(content)

    return {"message": f"Note '{title}' created successfully!"}


@app.get("/notes/{title}")
def read_note(title: str):
    file_path = os.path.join(NOTES_FOLDER, f"{title}.txt")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found")

    with open(file_path, "r") as file:
        content = file.read()

    return {"title": title, "content": content}


@app.put("/notes/{title}")
def update_note(title: str, content: str):
    file_path = os.path.join(NOTES_FOLDER, f"{title}.txt")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found")

    with open(file_path, "w") as file:
        file.write(content)

    return {"message": f"Note '{title}' updated successfully!"}


@app.delete("/notes/{title}")
def delete_note(title: str):
    file_path = os.path.join(NOTES_FOLDER, f"{title}.txt")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Note not found")

    os.remove(file_path)

    return {"message": f"Note '{title}' deleted successfully!"}
