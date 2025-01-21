# ft_linear_regression

# Linear Regression Model with Graphs

## Overview

This project implements a simple linear regression model to predict car prices based on mileage. It uses gradient descent for training and normalizes the data for better performance. The project also visualizes the training process and saves important plots (error progression and regression line) in a dedicated directory.

## Files and Directories

- **`trainModel.py`**: Main script to train the model.
- **`estimatePrice.py`**: Contains the `estimatePrice` function to calculate predictions.
- **`data.csv`**: Dataset file with mileage and price columns used for training the model.
- **`theta.csv`**: File where the trained model parameters (`theta0` and `theta1`) are saved.
- **`graphs/`**: Directory where the generated plots are saved.

## Features

1. **Data Normalization**: Normalizes mileage and price to improve training.
2. **Gradient Descent**: Optimizes the model parameters (`theta0` and `theta1`).
3. **Visualization**:
   - Error progression during training (`error_plot.png`).
   - Regression line plotted against the data (`regression_plot.png`).
4. **Model Evaluation**: Computes the model's precision as a percentage using test data.

## Usage

### Prerequisites

- Python 3.6+
- Required Python libraries: `matplotlib`, `csv`

Install any missing dependencies using:

```bash
pip install matplotlib
```

### Training the Model

Run the `trainModel` function to train the model and save the results:

```python
trainModel("data.csv", 0.1, 100)
```

- **Arguments**:
  - `data_file` (str): Path to the dataset CSV file.
  - `learning_rate` (float): Step size for gradient descent.
  - `iterations` (int): Number of iterations for training.

### Evaluating the Model

Use the `evaluateModelBasic` function to calculate the model's precision on test data:

```python
evaluateModelBasic("test_data.csv", "theta.csv")
```

- **Arguments**:
  - `test_data_file` (str): Path to the test dataset CSV file.
  - `theta_file` (str): Path to the file containing trained model parameters.

### Output Files

1. **`graphs/error_plot.png`**: Visualizes the reduction in error during training.
2. **`graphs/regression_plot.png`**: Shows the regression line against the dataset.
3. **`theta.csv`**: Contains the final model parameters in the format `theta0,theta1`.

## Example Directory Structure

```
project/
├── trainModel.py
├── estimatePrice.py
├── data.csv
├── test_data.csv
├── theta.csv
├── graphs/
│   ├── error_plot.png
│   └── regression_plot.png
```
