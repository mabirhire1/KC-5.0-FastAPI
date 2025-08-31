from fastapi import FastAPI, HTTPException
from models import Contact

app = FastAPI()

contacts = {}

@app.post("/contacts/")
def create_contact(contact: Contact):
    if contact.name in contacts:
        raise HTTPException(status_code=400, detail="Contact already exists")
    contacts[contact.name] = contact.dict()
    return {"message": f"Contact '{contact.name}' added"}

@app.get("/contacts/")
def read_contacts(name: str = None):
    if name: 
        if name not in contacts:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contacts[name]
    return contacts  

@app.put("/contacts/{name}")
def update_contact(name: str, contact: Contact):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    contacts[name] = contact.dict()
    return {"message": f"Contact '{name}' updated"}


@app.delete("/contacts/{name}")
def delete_contact(name: str):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    del contacts[name]
    return {"message": f"Contact '{name}' deleted"}
