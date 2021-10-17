#Nama: Patricia Dita Natasha
#NIM: 18219018

import json
from fastapi import FastAPI, HTTPException #importFastAPIclass.
with open ("menu.json","r") as read_file:
    data = json.load(read_file)
app = FastAPI() # create FastAPI instance.

@app.get("/")  # define path operation decorator.
async def root(): # Python function. The use of async is optional.
    return {"Hello": "World"}

@app.get('/menu/{item_id}')
async def read_menu(item_id: int):
      for menu_item in data['menu']:
            if menu_item['id'] == item_id:
                return menu_item
      raise HTTPException(
        status_code=404, detail=f'Item not found'
      )

@app.post('/menu/{name}')
async def post_menu(name: str):
    id=1
    if(len(data["menu"])>0):
        id = data["menu"][len(data["menu"])-1]["id"]+1
    update_data={"id":id,"name":name}
    data["menu"].append(dict(update_data))

    #menutup dulu file yang sudah dibuka agar bisa dibuka lagi untuk di write
    read_file.close()
    with open("menu.json","w") as write_file:
        json.dump(data,write_file,indent=4)
    write_file.close()

    return(update_data)
    raise HTTPException(
        status_code=404, detail=f"Item addition failed."
    )

@app.put('/menu/{item_id}/{name}')
async def update_menu(item_id: int, name: str):
      for menu_item in data['menu']:
            if menu_item['id'] == item_id:
                menu_item['name'] = name
                read_file.close()
                with open("menu.json","w") as write_file:
                    json.dump(data,write_file,indent=4)
                write_file.close()

                return {"Menu updated successfully."}
      raise HTTPException(
        status_code=404, detail=f'Menu failed to update.'
      )

@app.delete('/menu/{item_id}')
async def delete_menu(item_id: int):
      for menu_item in data['menu']:
            if menu_item['id'] == item_id:
                data["menu"].remove(menu_item)
                read_file.close()
                with open("menu.json","w") as write_file:
                    json.dump(data,write_file,indent=4)
                write_file.close()

                return {"Item deleted successfully."}
      raise HTTPException(
        status_code=404, detail=f'Item deletion failed.'
      )