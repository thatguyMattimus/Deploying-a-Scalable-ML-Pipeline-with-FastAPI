# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- Model Organizer/Developer - Matthew Martin
- Date Created 11/22/25
- Model Version 1.0
- Linear Regression Model from scikit-learn using Liblinear Solver with 5000 max iterations.
- Please contact Repo owner for questions.

## Intended Use

Prediction model to determine if income is above or below $50k from the census data.
## Training Data

Census Income data available from the UC Irvine Machine Learning Repository [here](https://archive.ics.uci.edu/dataset/20/census+income).

Extracted by Barry Becker from the 1994 Census database.

48842 instances and 14 features such as age, workclass, education, maritial-status, occupation, relationship, race and sex.

## Evaluation Data

Dataset was split into training and test data using an 80/20 split. Training was used to fit the regression model while test data was held for model evaluation.

## Metrics

Overall model performance:

**Precision: 0.7281 | Recall: 0.2693 | F1: 0.3931**

## Ethical Considerations

After using an ad-hoc approach to checking biases, the plotted graphs from the slice_output.txt does not appear to show any extreme biases towards any particular groups of people.

## Caveats and Recommendations

With the nature of ad-hoc approach to checking biases, a more in depth exploration of bias using Aequitas would be recommended as the data set contains a large amount of data that is subject to bias in relation to Salary.