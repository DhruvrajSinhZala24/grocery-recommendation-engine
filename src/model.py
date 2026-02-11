from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import pandas as pd
from config import MIN_SUPPORT, MIN_CONFIDENCE, MIN_LIFT

def train_model(transactions):

    print("Encoding transactions...")

    te = TransactionEncoder()
    te_array = te.fit(transactions).transform(transactions)

    basket = pd.DataFrame(te_array, columns=te.columns_)

    print("Running FP-Growth...")

    frequent_itemsets = fpgrowth(
        basket,
        min_support=MIN_SUPPORT,
        use_colnames=True
    )

    print("Generating association rules...")

    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=MIN_CONFIDENCE
    )

    # Keep single-item antecedents only
    rules = rules[
        rules["antecedents"].apply(lambda x: len(x) <= 2)
    ]

    # Filter by lift
    rules = rules[rules["lift"] >= MIN_LIFT]

    rules = rules.sort_values(by="confidence", ascending=False)

    print(f"Total Rules Generated: {len(rules)}")

    return rules
