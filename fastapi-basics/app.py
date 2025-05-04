from fastapi import FastAPI

app = FastAPI()



# Decorators used to define your paths
@app.get('/')
def greet():
  return {"message":"Hello"}


@app.get('/items/{item_id}')
def read_item(item_id: int, q : str = None):
  return {
    "item_id" : item_id,
    "query": q
  }
  

  

from pydantic import BaseModel

class Item(BaseModel):
  name:str
  price: float
  is_offer: bool = False

@app.post('/items')
def create_item(item: Item):
  return {"item_received": item}  



#Postman
#default route

#get post put patch 


#Create Read Update and Delete

#get
# get some response - Read

#post 
# Used to send informartion to the server- Create

#put 
# Used to update the available entry - Update

#patch 
# used for deleting any of the entry from the server - Delete
