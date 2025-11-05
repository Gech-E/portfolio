# Sales Analytics Dashboard

Comprehensive data science project analyzing sales data with interactive visualizations, predictive models, and business insights. Includes ETL pipeline and automated reporting.

## Features

- **Data Analysis**: Comprehensive exploratory data analysis (EDA)
- **Visualizations**: Multiple charts and graphs for insights
- **Predictive Modeling**: Random Forest regression for sales forecasting
- **Feature Engineering**: Time-based features and categorical encoding
- **Automated Reporting**: Generates summary reports and visualizations
- **Business Insights**: Top performers, category analysis, regional distribution

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the analysis:
```bash
python analyze_sales.py
```

## Project Structure

- `analyze_sales.py`: Main analysis script
- `sales_data_processed.csv`: Processed dataset (generated)
- Generated visualizations (PNG files)

## Analysis Components

### 1. Data Exploration
- Dataset statistics and information
- Missing value analysis
- Descriptive statistics

### 2. Visualizations
- **Monthly Sales Trend**: Time series analysis of sales
- **Sales by Category**: Bar chart showing category performance
- **Regional Distribution**: Pie chart of sales by region
- **Profit Margin Analysis**: Average profit margins by category
- **Correlation Heatmap**: Relationships between numeric variables
- **Top Salespersons**: Performance analysis of top 10 salespeople

### 3. Predictive Modeling
- Random Forest Regressor for sales prediction
- Feature importance analysis
- Model evaluation metrics (R², RMSE, MAE)
- Prediction vs Actual visualization

### 4. Business Insights
- Total sales and profit calculations
- Best performing categories and regions
- Top salesperson identification
- Profit margin analysis

## Generated Outputs

1. **sales_analysis_overview.png**: Main dashboard with 4 key visualizations
2. **correlation_heatmap.png**: Correlation matrix heatmap
3. **top_salespersons.png**: Top 10 salespersons analysis
4. **feature_importance.png**: Feature importance in prediction model
5. **prediction_vs_actual.png**: Model performance visualization
6. **sales_data_processed.csv**: Processed dataset with engineered features

## Usage

### Basic Analysis
```bash
python analyze_sales.py
```

### Custom Data
Replace the `generate_sales_data()` function with your own data loading:
```python
df = pd.read_csv('your_sales_data.csv')
```

## Model Performance

The Random Forest model typically achieves:
- **R² Score**: 0.85-0.95 (depending on data quality)
- **RMSE**: Varies based on sales magnitude
- **Feature Importance**: Quantity, unit price, and discount are key predictors

## Technologies Used

- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical visualizations
- **Scikit-learn**: Machine learning models
- **Jupyter**: Interactive notebooks (optional)

## Future Enhancements

- Interactive dashboard with Streamlit or Dash
- Real-time data pipeline
- Advanced time series forecasting (ARIMA, Prophet)
- Customer segmentation analysis
- A/B testing framework
- Automated email reports

## Data Schema

The sales data includes:
- `date`: Transaction date
- `product_category`: Product category
- `region`: Sales region
- `salesperson_id`: Salesperson identifier
- `quantity`: Units sold
- `unit_price`: Price per unit
- `discount`: Discount percentage
- `total_sales`: Calculated total sales
- `profit`: Calculated profit

## Notes

- The script generates synthetic data for demonstration
- Replace with your actual sales data for real analysis
- Adjust model parameters based on your dataset size
- Visualizations are saved as high-resolution PNG files

