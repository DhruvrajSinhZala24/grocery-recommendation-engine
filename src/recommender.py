import difflib
from config import TOP_N_RECOMMENDATIONS


def suggest_products(product_input, product_list):

    suggestions = difflib.get_close_matches(
        product_input,
        product_list,
        n=5,
        cutoff=0.4
    )

    return suggestions


def recommend(rules, product_list):

    user_input = input("\nEnter product(s) separated by comma (or type 'exit'): ")

    if user_input.lower() == "exit":
        return "exit"

    input_products = [p.strip().lower() for p in user_input.split(",")]

    validated_products = []

    for product in input_products:

        matches = suggest_products(product, product_list)

        if not matches:
            print(f"\n❌ '{product}' not found.")
            continue

        print(f"\n🔎 Suggestions for '{product}':")
        for i, match in enumerate(matches):
            print(f"{i+1}. {match}")

        validated_products.append(matches[0].lower())

    if not validated_products:
        print("\nNo valid products selected.")
        return

    # Collect union-based recommendations
    combined = rules[
        rules["antecedents"].apply(
            lambda x: any(
                prod in [item.lower() for item in x]
                for prod in validated_products
            )
        )
    ]

    if combined.empty:
        print("\nNo strong purchase patterns found.")
        return

    # Extract single consequent string
    combined["consequent_item"] = combined["consequents"].apply(
        lambda x: list(x)[0]
    )

    # Remove items already selected
    combined = combined[
        ~combined["consequent_item"].str.lower().isin(validated_products)
    ]

    if combined.empty:
        print("\nNo additional recommendations found.")
        return

    # Remove duplicates by keeping highest confidence
    combined = (
        combined.sort_values("confidence", ascending=False)
        .drop_duplicates(subset=["consequent_item"])
    )

    print(f"\nIf customer buys {validated_products},")
    print("they are likely to buy:\n")

    for _, row in combined.head(TOP_N_RECOMMENDATIONS).iterrows():

        consequent = row["consequent_item"]
        probability = round(row["confidence"] * 100, 2)
        lift = round(row["lift"], 2)

        print(f"- {consequent}")
        print(f"  Probability: {probability}%")
        print(f"  Lift Score: {lift}")
        print("-" * 40)
