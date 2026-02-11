def evaluate_rules(rules, total_products):

    total_rules = len(rules)

    unique_antecedents = rules["antecedents"].nunique()
    unique_consequents = rules["consequents"].nunique()

    coverage = round((unique_antecedents / total_products) * 100, 2)

    print("\n📊 Model Evaluation Summary")
    print("-----------------------------------")
    print(f"Total Rules Generated: {total_rules}")
    print(f"Unique Antecedent Products: {unique_antecedents}")
    print(f"Unique Consequent Products: {unique_consequents}")
    print(f"Model Coverage: {coverage}%")
    print("-----------------------------------\n")
