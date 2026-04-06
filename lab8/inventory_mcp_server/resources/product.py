from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pdmodels.product_model import ProductModel

inventories = [
    {
        "name": "Laptop",
        "quantity": 1000
    },
    {
        "name": "Phone",
        "quantity": 5000
    }
]


class Product:
    def read(self, pname):
        for record in inventories:
            if pname == record["name"]:
                return JSONResponse(content=jsonable_encoder(record),
                                    status_code=status.HTTP_200_OK)
        return JSONResponse(content=jsonable_encoder({'message': "There is no product with the name " + pname}),
                            status_code=status.HTTP_404_NOT_FOUND)

    def update(self, pname, value):
        for record in inventories:
            if pname == record["name"]:
                record["quantity"] = record["quantity"] - value
                return JSONResponse(content=jsonable_encoder(record),
                                    status_code=status.HTTP_200_OK)
        return JSONResponse(content=jsonable_encoder({'message': "There is no product with the name " + pname}),
                            status_code=status.HTTP_404_NOT_FOUND)


class Products:
    def create(self, p_model:ProductModel):
        record_to_be_created = p_model.model_dump(mode="json")
        pname = p_model.name
        for record in inventories:
            if pname == record["name"]:
                return JSONResponse(content=jsonable_encoder({'message': "There is no product with the name " + pname}),
                                    status_code=status.HTTP_404_NOT_FOUND)
        inventories.append(record_to_be_created)
        return JSONResponse(content=jsonable_encoder(record_to_be_created),
                            status_code=status.HTTP_201_CREATED)
