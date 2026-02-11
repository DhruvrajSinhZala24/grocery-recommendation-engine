import pandas as pd
from config import SAMPLE_SIZE

def create_transactions(order_products, products):

    # Sample to control memory usage
    order_products = order_products.head(SAMPLE_SIZE)

    merged = order_products.merge(
        products[["product_id", "product_name"]],
        on="product_id",
        how="left"
    )

    transactions = (
        merged.groupby("order_id")["product_name"]
        .apply(list)
        .tolist()
    )

    print(f"Total Transactions Used: {len(transactions)}")

    return transactions
