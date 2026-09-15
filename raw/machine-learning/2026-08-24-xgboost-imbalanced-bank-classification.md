# Using XGBoost for Predicting Bank Clients' Product Subscriptions in Imbalanced Data

> Source: https://github.com/AnMol12499/DataScience-project-using-XGBoost
> Collected: 2026-08-24
> Published: Unknown

A code pattern illustrating ML classification with XGBoost on a highly imbalanced real-life dataset — Portuguese banking institution phone-call data regarding certificate-of-deposit (CD) purchases (UCI Bank Marketing dataset). XGBoost is usually a better choice compared to logistic regression and other techniques, but good classification on imbalanced data is non-trivial; this pattern demonstrates the tricks.

## Workflow

1. Dataset description and upload (data/bank.csv).
2. Exploratory analysis to understand the data.
3. Preprocessing to clean and prepare the data.
4. Naive XGBoost classification with cross-validation; plot precision-recall curve and ROC curve.
5. Tuning with weighted positive samples to improve classification performance.
6. Advanced techniques discussed: oversampling of majority class, undersampling of minority class, SMOTE algorithms.

## Implementation

Single notebook: `predict_bank_cd_subs_by_xgboost_clf_for_imbalance_dataset.ipynb`. Stack: Python, XGBoost, Scikit-learn, Pandas, Matplotlib, Seaborn. Scikit-learn ML pipelines used so training-time preparation steps apply identically to the test set.

Sample result: with positive-sample weight set to 1000 and feature-selection threshold 0.008, recall on the imbalanced positive class improved to 0.84 on test data.

Dataset: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
