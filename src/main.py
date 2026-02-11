from data_loader import load_data
from preprocessing import create_transactions
from model import train_model
from recommender import recommend
from evaluation import evaluate_rules
import os

def main():

    print("Instacart Recommendation System Starting...\n")

    orders, order_products, products = load_data()

    transactions = create_transactions(order_products, products)

    rules = train_model(transactions)

    os.makedirs("results", exist_ok=True)
    rules.to_csv("results/rules.csv", index=False)

    evaluate_rules(rules, total_products=len(products))

    print("System Ready.\n")

    product_list = products["product_name"].str.lower().tolist()

    while True:

        result = recommend(rules, product_list)

        if result == "exit":
            break


main()