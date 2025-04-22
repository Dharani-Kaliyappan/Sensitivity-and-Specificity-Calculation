# 🧮 Model Evaluation Metrics Using Pure Python

This project is a lightweight and educational implementation of essential **binary classification evaluation metrics** using **Python** 

It provides a fundamental and transparent way to understand how performance metrics are calculated from raw classification results, making it ideal for learning, teaching, testing, and validating binary classification models in restricted environments.
It calculates:
- ✅ Accuracy
- 📏 Precision
- 🎯 Sensitivity (Recall / True Positive Rate)
- 🛡️ Specificity (True Negative Rate)
- 🧠 F1 Score
- 🧾 Confusion Matrix

## 📌 Objective

The primary goal of this project is to offer a clear and concise Python-based tool that:
- Accepts predicted and actual class labels
- Computes and displays key performance metrics
- Helps users understand how metrics like **accuracy**, **precision**, **recall**, and **F1 score** are calculated at the most basic level
- Visualizes the **confusion matrix** in a text-based format, making it suitable for use in any terminal or online Python environment

## 🔍 What This Script Does

Given two lists:
- `actual`: the ground truth values (typically 0 for negative and 1 for positive)
- `predicted`: the predicted output from a classification model

The script calculates:
- ✅ **True Positives (TP)**: Correctly predicted positive cases
- ❌ **False Positives (FP)**: Incorrectly predicted as positive
- ❗ **False Negatives (FN)**: Incorrectly predicted as negative
- ✅ **True Negatives (TN)**: Correctly predicted negative cases

Based on the above, it derives the following metrics:
- **Accuracy**: `(TP + TN) / Total` — Overall effectiveness of the model
- **Precision**: `TP / (TP + FP)` — How many predicted positives were actually positive
- **Recall (Sensitivity / TPR)**: `TP / (TP + FN)` — How many actual positives were correctly identified
- **Specificity (TNR)**: `TN / (TN + FP)` — How many actual negatives were correctly identified
- **F1 Score**: `2 * (Precision * Recall) / (Precision + Recall)` — A balance between Precision and Recall
- **Confusion Matrix**: A 2×2 matrix summarizing all of the above

## 🔬 Understanding Sensitivity and Specificity

### 🎯 Sensitivity (True Positive Rate / Recall)
Sensitivity measures the model’s ability to correctly identify actual positives. In medical diagnostics, this is especially critical for detecting conditions or diseases. A high sensitivity means fewer false negatives.

**Formula:**
Sensitivity = TP / (TP + FN)

**Example Use Case:**  
If a cancer detection test has high sensitivity, it means most patients with cancer are correctly diagnosed.

### 🛡️ Specificity (True Negative Rate)
Specificity evaluates the model’s ability to correctly classify actual negatives. This is important when false positives could cause unnecessary anxiety or treatment.

**Formula:**
Specificity = TN / (TN + FP)

**Example Use Case:**  
In screening for a rare disease, a high specificity ensures healthy individuals aren’t wrongly diagnosed as ill.

Together, **sensitivity and specificity provide a balanced view** of a model’s performance, especially in **imbalanced datasets** or **high-stakes domains** such as healthcare and fraud detection.

## 🎯 Why This Project Matters

Many machine learning tutorials rely on third-party libraries to compute evaluation metrics, which may hide the underlying logic. This project strips everything down to the basics so users can:
- 👨‍💻 Understand what each metric actually measures
- 🧠 Learn how the metrics are derived from confusion matrix values
- 📊 Gain confidence in interpreting model performance manually
- 💬 Use and test the code in interviews, exams, or limited environments like online compilers

---

## 👨‍🏫 Ideal For

- 🧪 **Students and beginners** who want to learn evaluation metric computations from scratch
- 👨‍🏫 **Teachers and instructors** explaining classification performance in ML courses
- 🤖 **Developers and data scientists** who need quick evaluations without setting up libraries
- 💼 **Job candidates** preparing for ML or data science interviews and coding rounds
- 🔒 **Environments with restrictions** (e.g., online IDEs, embedded systems, or coding platforms where importing libraries is disabled)

