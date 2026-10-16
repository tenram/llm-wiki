# Microsoft GUIDE Cybersecurity Incident Classification

> Sources: pavankethavath, 2026-10-05
> Raw: [Cybersecurity incident classification](../../raw/machine-learning/cybersecurity-incident-classification.md)

## Overview

This repository presents a machine-learning pipeline for classifying Microsoft GUIDE cybersecurity incidents as True Positive, Benign Positive, or False Positive. It frames the model as a Security Operations Center triage aid.

## Pipeline

The workflow handles missing values, extracts time features, encodes categorical values, and removes highly correlated features. It compares logistic regression, decision trees, random forests, gradient boosting, XGBoost, and LightGBM. RandomizedSearchCV tunes models, while SMOTE and class weights address class imbalance. SHAP is used for feature analysis.

## Reported Results

The repository selects a tuned XGBoost model without SMOTE and reports Macro-F1 scores of 0.91 on validation data and 0.90 on test data. It also describes a large GUIDE dataset with more than 13 million evidence records and more than one million incidents. These figures and results are repository-reported claims; independent reproduction and leakage checks are still required before operational use.

## See Also

- [XGBoost](xgboost.md)
- [XGBoost Imbalanced Classification Pattern](xgboost-imbalanced-classification-pattern.md)
