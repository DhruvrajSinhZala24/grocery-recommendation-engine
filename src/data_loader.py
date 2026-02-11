import pandas as pd
import os
from config import DATA_PATH

def load_data():
    orders = pd.read_csv(os.path.join(DATA_PATH, "orders.csv"))
    order_products = pd.read_csv(os.path.join(DATA_PATH, "order_products__prior.csv"))
    products = pd.read_csv(os.path.join(DATA_PATH, "products.csv"))

    print("Data Loaded Successfully")
    print(f"Orders: {orders.shape}")
    print(f"Order Products: {order_products.shape}")
    print(f"Products: {products.shape}")

    return orders, order_products, products
