# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf
## Model Details
Model Name: Census Income Prediction Model

Version: 1.0

Date: 07/06/2024

Model Type: Random Forest Classification

## Intended Use
Primary intended uses: For use through a machine learning pipeline and FASTAPI environment. 
The model encodes categorical features and uses the file "train_model" to evaluate performance metrics on salary. 
The model selected is Random Forest Classification and will predict if an individual earns under or over 50k per year.

Primary intended users: The model was developed for WGU's Data Scientist Nanodegree.

Out-of-scope uses: Production outside the specified dataset. Dataset is not for distribution.

## Training Data

Dataset: census.csv 
The census data from 1994 contains demographic information on individuals such a occupation, sex, marital status, education, and age. The data was cleaned, and encoded in pre-processing. 80% of the data is reserved for training.

## Evaluation Data

Dataset: census.csv
The evaluation data is the census data as well. 20% of this data was reserved for the evaluation portion.


## Metrics

Best performance metrics returned: Precision: 0.7454 | Recall: 0.6365 | F1: 0.6867

Full Metrics documented in slice_output.txt

## Ethical Considerations

Data: The dataset does not use any sensitive data.
Human life: The model is intended only to predict if an individual earns under or over 50k per year.
Bias may be introduced since there are some individuals that are overrepresented or underrepresented in our data.

## Caveats and Recommendations

The ideal characteristics for this model should be in the census.csv format. 
To use this model for other years, update the values based on additional data retained for the year.
