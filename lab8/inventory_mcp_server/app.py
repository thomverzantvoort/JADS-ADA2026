import uvicorn
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from pdmodels.product_model import ProductModel
from resources.product import Product, Products

app = FastAPI()

product = Product()
products = Products()


@app.post("/products", operation_id="add_product", description="Add a product to the inventory")
def create_products(p_model: ProductModel):
    return products.create(p_model)


@app.get('/products/{pname}', operation_id="check_product_inventory",
         description="Get a product from the inventory. A product has a unique name.")
def get_product(pname: str):
    return product.read(pname)

@app.put('/products/{pnmae}/quantity', operation_id="update_product_quantity_available",
         description="Update the available quantity of a product by reducing the ordered quantity. A product has a unique name.")
def update_product(pname: str, ordered_quantity: int):
    return product.update(pname, ordered_quantity)


# --- MCP Integration ---
mcp = FastApiMCP(
    app,
    name="Inventory Management MCP Server",
    description="Tools for managing product inventories deliveries.",
    describe_all_responses=True,
    describe_full_response_schema=True,
    # Only expose the endpoints with these operation_ids
    include_operations=[
        "add_product",
        "check_product_inventory",
        "update_product_quantity_available",
    ]
)
mcp.mount_http(app, mount_path="/mcp")
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5001, reload=True)
