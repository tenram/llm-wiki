# XGBoost Imbalanced Classification Pattern

> Sources: AnMol12499, 2026-08-24
> Raw: [Bank subscription pattern](../../raw/machine-learning/2026-08-24-xgboost-imbalanced-bank-classification.md)

## Overview

A worked code pattern for binary classification with XGBoost on highly imbalanced data: predicting bank clients' certificate-of-deposit subscriptions from the UCI Bank Marketing dataset (Portuguese phone-call records). Demonstrates that naive XGBoost underperforms on imbalanced positives and walks the fixes.

## Workflow

Exploratory analysis → preprocessing → naive XGBoost with cross-validation (ROC + precision-recall curves) → positive-sample weighting → advanced resampling discussion (oversampling majority, undersampling minority, SMOTE). Scikit-learn pipelines keep train/test preparation identical.

## Result

With positive-class weight 1000 and feature-selection threshold 0.008, recall on the imbalanced positive class reached 0.84 on test data — the headline trick being class weighting over architecture changes.

## See Also

- [XGBoost](xgboost.md)
