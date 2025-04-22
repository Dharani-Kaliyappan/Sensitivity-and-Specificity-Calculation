# Sample actual and predicted values
actual =    [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
predicted = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# Initialize counts
tp = tn = fp = fn = 0

# Calculate TP, TN, FP, FN
for a, p in zip(actual, predicted):
    if a == 1 and p == 1:
        tp += 1
    elif a == 0 and p == 0:
        tn += 1
    elif a == 0 and p == 1:
        fp += 1
    elif a == 1 and p == 0:
        fn += 1

# Calculate metrics
accuracy    = (tp + tn) / len(actual)
precision   = tp / (tp + fp) if (tp + fp) != 0 else 0
recall      = tp / (tp + fn) if (tp + fn) != 0 else 0  # sensitivity
specificity = tn / (tn + fp) if (tn + fp) != 0 else 0
f1_score    = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

# Confusion Matrix Printout
print("\n=== Confusion Matrix ===")
print("             Predicted")
print("           |   0   |   1  ")
print("       -------------------")
print(f"Actual  0 |  {tn:^3}  |  {fp:^3}")
print(f"        1 |  {fn:^3}  |  {tp:^3}")

# Metrics Matrix
print("\n=== Evaluation Metrics ===")
print("+----------------+----------+")
print("|   Metric       |  Value   |")
print("+----------------+----------+")
print(f"| Accuracy       | {accuracy:.4f} |")
print(f"| Precision      | {precision:.4f} |")
print(f"| Recall (TPR)   | {recall:.4f} |")
print(f"| Specificity    | {specificity:.4f} |")
print(f"| F1 Score       | {f1_score:.4f} |")
print("+----------------+----------+")
