# CS3-4002 - Predicting Stock Price Trends from Historical data
This case study is build on a project aimed at forecasting stock prices using simple linear regrassion on historical monthly data. This repository contains the study, deliverable, data, reference materials, etc. needed to complete the case study.
## Why this matters
Predicting stock prices is a core component of financial analytics and algorithmic trading. By learning the basics and building a lightweright model to analyze stock price trends, you will understand the foundation of financial analysis techniques that junior quant researchers and traders build off of.
## Overview
`DATA/`: CSVs of monthly stock price data from Alpha Vantage (1999-2025).

`SCRIPTS/`: Python code for API data pulling, preprocessing, model training, and evaluation.

`OUTPUT/`: Plots of predicted vs actual prices and model evaluation

`README.md`: This document

`HOOK.pdf`: Your project briefing

` RUBRIC.pdf`: Assignment criteria

`MATERIALS/`: directory containing references for deeper understanding
## How to Run
1. Clone the repository into a directory of your choosing or create a new project directory
2. Ensure you have a Python version higher than 3, preferably 3.10
3. Install the dependencies necessary: `pandas`, `requests`, `matplotlib`, `time`, `scipy`, `scikit-learn`, `requests`, `os`
4. *Optional*: Start a virtual environment using `python3 -m venv venv` then `source venve/bin/activate`. You may install depencendies afterward
5. Run `data_loading.py` and enter the stock tickers of your choice (must be stocks not ETFs)
6. Execute `data_preprocessing.py` to clean and normalize data
7. Run `model_training.py` to train and test the linear regression model, generate visualizations, and evaluate the model.

All outputs will be save to the `OUTPUT/` directory.
