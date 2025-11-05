"""
Sales Analytics Dashboard
Comprehensive data science project analyzing sales data with interactive visualizations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Generate sample sales data
def generate_sales_data(n=1000):
    """Generate synthetic sales data for demonstration"""
    np.random.seed(42)
    
    dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
    dates = np.random.choice(dates, n)
    
    data = {
        'date': dates,
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books', 'Sports'], n),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n),
        'salesperson_id': np.random.randint(1, 21, n),
        'quantity': np.random.randint(1, 100, n),
        'unit_price': np.random.uniform(10, 500, n),
        'discount': np.random.uniform(0, 0.3, n),
    }
    
    df = pd.DataFrame(data)
    df['total_sales'] = df['quantity'] * df['unit_price'] * (1 - df['discount'])
    df['profit'] = df['total_sales'] * np.random.uniform(0.1, 0.4, n)
    
    # Sort by date
    df = df.sort_values('date').reset_index(drop=True)
    
    return df

# Load or generate data
print("Loading sales data...")
df = generate_sales_data(2000)
print(f"Dataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())

# Data Exploration
print("\n" + "="*50)
print("DATA EXPLORATION")
print("="*50)

print("\nDataset Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Feature Engineering
print("\n" + "="*50)
print("FEATURE ENGINEERING")
print("="*50)

df['year'] = pd.to_datetime(df['date']).dt.year
df['month'] = pd.to_datetime(df['date']).dt.month
df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek
df['quarter'] = pd.to_datetime(df['date']).dt.quarter

# Create visualizations
def create_visualizations(df):
    """Create comprehensive visualizations"""
    
    # 1. Sales Over Time
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Monthly sales trend
    monthly_sales = df.groupby(['year', 'month'])['total_sales'].sum().reset_index()
    monthly_sales['date'] = pd.to_datetime(monthly_sales[['year', 'month']].assign(day=1))
    axes[0, 0].plot(monthly_sales['date'], monthly_sales['total_sales'], marker='o')
    axes[0, 0].set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Total Sales ($)')
    axes[0, 0].grid(True, alpha=0.3)
    plt.setp(axes[0, 0].xaxis.get_majorticklabels(), rotation=45)
    
    # Sales by Category
    category_sales = df.groupby('product_category')['total_sales'].sum().sort_values(ascending=False)
    axes[0, 1].bar(category_sales.index, category_sales.values, color='steelblue')
    axes[0, 1].set_title('Total Sales by Product Category', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Product Category')
    axes[0, 1].set_ylabel('Total Sales ($)')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Sales by Region
    region_sales = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)
    axes[1, 0].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', startangle=90)
    axes[1, 0].set_title('Sales Distribution by Region', fontsize=14, fontweight='bold')
    
    # Profit Margin Analysis
    df['profit_margin'] = (df['profit'] / df['total_sales']) * 100
    category_margin = df.groupby('product_category')['profit_margin'].mean().sort_values(ascending=False)
    axes[1, 1].barh(category_margin.index, category_margin.values, color='green')
    axes[1, 1].set_title('Average Profit Margin by Category', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('Profit Margin (%)')
    
    plt.tight_layout()
    plt.savefig('sales_analysis_overview.png', dpi=300, bbox_inches='tight')
    print("\nSales analysis overview saved as 'sales_analysis_overview.png'")
    plt.close()
    
    # 2. Correlation Heatmap
    numeric_cols = ['quantity', 'unit_price', 'discount', 'total_sales', 'profit', 'profit_margin']
    corr_matrix = df[numeric_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
    print("Correlation heatmap saved as 'correlation_heatmap.png'")
    plt.close()
    
    # 3. Top Salespersons
    top_salespersons = df.groupby('salesperson_id').agg({
        'total_sales': 'sum',
        'profit': 'sum'
    }).sort_values('total_sales', ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(top_salespersons))
    width = 0.35
    
    ax.bar(x - width/2, top_salespersons['total_sales'], width, label='Total Sales', color='steelblue')
    ax.bar(x + width/2, top_salespersons['profit'], width, label='Profit', color='green')
    
    ax.set_xlabel('Salesperson ID')
    ax.set_ylabel('Amount ($)')
    ax.set_title('Top 10 Salespersons by Sales and Profit', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(top_salespersons.index)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('top_salespersons.png', dpi=300, bbox_inches='tight')
    print("Top salespersons analysis saved as 'top_salespersons.png'")
    plt.close()

# Create visualizations
create_visualizations(df)

# Predictive Modeling
print("\n" + "="*50)
print("PREDICTIVE MODELING")
print("="*50)

# Prepare features
feature_cols = ['quantity', 'unit_price', 'discount', 'year', 'month', 'quarter']
X = df[feature_cols].copy()
y = df['total_sales'].copy()

# Encode categorical variables
X = pd.get_dummies(X, columns=[], drop_first=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
print("\nTraining Random Forest model...")
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
rf_model.fit(X_train, y_train)

# Predictions
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# Evaluate model
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
test_mae = mean_absolute_error(y_test, y_test_pred)

print(f"\nModel Performance:")
print(f"Training R² Score: {train_r2:.4f}")
print(f"Test R² Score: {test_r2:.4f}")
print(f"Test RMSE: ${test_rmse:.2f}")
print(f"Test MAE: ${test_mae:.2f}")

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\nFeature Importance:")
print(feature_importance)

# Plot feature importance
plt.figure(figsize=(10, 6))
sns.barplot(data=feature_importance, x='importance', y='feature', palette='viridis')
plt.title('Feature Importance in Sales Prediction', fontsize=14, fontweight='bold')
plt.xlabel('Importance')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
print("\nFeature importance plot saved as 'feature_importance.png'")
plt.close()

# Prediction vs Actual
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_test_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Sales ($)')
plt.ylabel('Predicted Sales ($)')
plt.title('Actual vs Predicted Sales', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prediction_vs_actual.png', dpi=300, bbox_inches='tight')
print("Prediction vs actual plot saved as 'prediction_vs_actual.png'")
plt.close()

# Generate Summary Report
print("\n" + "="*50)
print("SUMMARY REPORT")
print("="*50)

total_sales = df['total_sales'].sum()
total_profit = df['profit'].sum()
avg_profit_margin = (df['profit'] / df['total_sales']).mean() * 100

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit Margin: {avg_profit_margin:.2f}%")
print(f"Best Performing Category: {df.groupby('product_category')['total_sales'].sum().idxmax()}")
print(f"Best Performing Region: {df.groupby('region')['total_sales'].sum().idxmax()}")
print(f"Top Salesperson: {df.groupby('salesperson_id')['total_sales'].sum().idxmax()}")

# Save processed data
df.to_csv('sales_data_processed.csv', index=False)
print("\nProcessed data saved as 'sales_data_processed.csv'")

print("\n" + "="*50)
print("ANALYSIS COMPLETE!")
print("="*50)
print("\nGenerated files:")
print("- sales_analysis_overview.png")
print("- correlation_heatmap.png")
print("- top_salespersons.png")
print("- feature_importance.png")
print("- prediction_vs_actual.png")
print("- sales_data_processed.csv")

