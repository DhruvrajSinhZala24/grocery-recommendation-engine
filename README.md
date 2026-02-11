# 🛒 Instacart Grocery Recommendation Engine

A scalable, production-ready, rule-based product recommendation system built using **FP-Growth** on real-world Instacart grocery transaction data.

This system predicts:

> If a customer buys Product A → what other products are they likely to buy (with probability %).

---

# 📌 Problem Statement

In e-commerce platforms, cross-selling and product bundling significantly increase revenue and improve customer experience.

This project builds a **market basket–based recommendation engine** that:

- Analyzes millions of historical transactions
- Discovers frequent product combinations
- Generates statistically valid association rules
- Computes conditional probabilities
- Provides multi-product recommendations in real time

---

# 📊 Dataset Information

**Dataset:** Instacart Market Basket Dataset  
**Source:** Kaggle  

Dataset Statistics:

- 3,421,083 orders  
- 32,434,489 order-product records  
- 49,688 unique products  

Each transaction represents a real customer grocery order.

---

# 🧠 Methodology

## 1️⃣ Transaction Construction

- Merge `order_products__prior.csv` with `products.csv`
- Group by `order_id`
- Convert orders into transaction baskets

Each transaction becomes:
[product_1, product_2, product_3, ...]

---

## 2️⃣ Frequent Pattern Mining (FP-Growth)

We use **FP-Growth** instead of Apriori because:

- No candidate generation
- Faster for large datasets
- Efficient for high-dimensional sparse data
- Scales well with millions of transactions

Implementation:

```python
mlxtend.frequent_patterns.fpgrowth
```

Rules are generated using:

```python
association_rules(metric="confidence")
```

Each rule contains:

- Support
- Confidence
- Lift

---

## 📐 Mathematical Foundation

### 🔹 Support

Support(A ∩ B)  
Percentage of transactions containing both A and B.

---

### 🔹 Confidence

P(B | A) = Support(A ∩ B) / Support(A)

Interpretation:

Probability that a customer buys B given that they bought A.

---

### 🔹 Lift

Lift = P(B | A) / P(B)

Interpretation:

- Lift > 1 → Positive association  
- Lift = 1 → Independent  
- Lift < 1 → Negative association  

Higher lift indicates stronger cross-sell strength.

---

## 🔎 Recommendation Logic

The system:

- Accepts single or multiple product input
- Uses fuzzy search for typo correction
- Aggregates rule-based recommendations
- Removes duplicate suggestions
- Excludes already-selected products
- Ranks results by confidence

Multi-product input is handled using union-based aggregation for realistic cross-sell behavior.

---

## 📈 Model Evaluation

Example output:

```
Total Rules Generated: 378
Unique Antecedent Products: 161
Unique Consequent Products: 22
Model Coverage: 0.32%
```

Coverage indicates the percentage of products that have strong association rules.  
Low coverage is expected in sparse grocery datasets.

---

## 🚀 How To Run The Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy mlxtend
```

### 2️⃣ Place Dataset Files Inside `/data` Directory

Required files:

- orders.csv
- order_products__prior.csv
- products.csv

### 3️⃣ Run The Application

```bash
python src/main.py
```

---

## 💡 Example Usage

Input:

```
organic whole milk
```

Output:

```
If customer buys ['organic whole milk'],
they are likely to buy:

- Banana
  Probability: 22.63%
  Lift Score: 1.52

- Bag of Organic Bananas
  Probability: 20.13%
  Lift Score: 1.68
```

---

## ⚙ Configuration

Editable inside `config.py`:

```
MIN_SUPPORT
MIN_CONFIDENCE
MIN_LIFT
SAMPLE_SIZE
TOP_N_RECOMMENDATIONS
```

These parameters allow tuning model strength and scalability.

---

## 🏗 Project Structure

```
instacart_recommender/
│
├── data/
│   ├── orders.csv
│   ├── order_products__prior.csv
│   ├── products.csv
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── recommender.py
│   ├── evaluation.py
│   └── main.py
│
├── results/
│   └── rules.csv
│
└── README.md
```

---

## 📊 Performance

With ~100,000 sampled transactions:

- FP-Growth runtime: ~30–60 seconds
- 378 statistically strong rules generated
- Efficient memory handling
- Configurable scalability

---

## 🔮 Future Improvements

- Collaborative filtering model
- Hybrid recommendation system
- Web interface (Streamlit)
- API deployment (FastAPI)
- Real-time scoring
- Personalized recommendations per user

## 📥 Dataset Access

The dataset used in this project is the **Instacart Market Basket Analysis Dataset**.

Due to size and licensing restrictions, the dataset is not included in this repository.

You can download it from here:

👉 https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis/download?file=order_products__prior.csv

⚠️ Notes:
- A Kaggle account is required to download the dataset.
- After downloading, extract the CSV files and place them inside the `/data` directory.
