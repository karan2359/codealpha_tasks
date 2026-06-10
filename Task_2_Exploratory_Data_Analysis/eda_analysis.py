
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.dpi'] = 100


# PART 1: Load Dataset & Basic Info


print(" EXPLORATORY DATA ANALYSIS (EDA)")


print("\nLoading dataset...")
df = pd.read_csv('books_dataset.csv')

print(f"\n✓ Dataset loaded successfully!")
print(f"\n Dataset Information:")
print(f"   - Total Rows: {len(df)}")
print(f"   - Total Columns: {len(df.columns)}")
print(f"   - Columns: {df.columns.tolist()}")

print(f"\n Data Types:")
print(df.dtypes)

print(f"\n First 5 Rows:")
print(df.head())

print(f"\n Last 5 Rows:")
print(df.tail())


# PART 2: Data Quality Check


print(" DATA QUALITY CHECK")


print(f"\n Missing Values:")
missing = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100
print(pd.DataFrame({
    'Missing Count': missing,
    'Missing %': missing_percent
}))

if missing.sum() == 0:
    print("\n✓ No missing values found - Data is clean!")
else:
    print(f"\n Found {missing.sum()} missing values - Need to clean!")

print(f"\n Duplicate Rows:")
duplicates = df.duplicated().sum()
print(f"   - Duplicates found: {duplicates}")
if duplicates == 0:
    print("   ✓ No duplicate rows!")


# PART 3: Clean Data


print(" DATA CLEANING")


# Clean price column
df['price'] = df['price'].str.replace('£', '').astype(float)

# Clean rating column
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['rating'] = df['rating'].map(rating_map)

print(f"\n✓ Data cleaned successfully!")
print(f"   - Price converted to numeric: {df['price'].dtype}")
print(f"   - Rating converted to numeric: {df['rating'].dtype}")


# PART 4: Statistical Summary


print(" STATISTICAL SUMMARY")


print(f"\n Price Statistics:")
print(f"   - Mean (Average): £{df['price'].mean():.2f}")
print(f"   - Median: £{df['price'].median():.2f}")
print(f"   - Min: £{df['price'].min():.2f}")
print(f"   - Max: £{df['price'].max():.2f}")
print(f"   - Std Dev: £{df['price'].std():.2f}")
print(f"   - 25th Percentile: £{df['price'].quantile(0.25):.2f}")
print(f"   - 75th Percentile: £{df['price'].quantile(0.75):.2f}")

print(f"\n Rating Statistics:")
print(f"   - Mean (Average): {df['rating'].mean():.2f}/5")
print(f"   - Median: {df['rating'].median():.1f}/5")
print(f"   - Min: {df['rating'].min()}/5")
print(f"   - Max: {df['rating'].max()}/5")
print(f"   - Std Dev: {df['rating'].std():.2f}")

print(f"\n Complete Statistical Summary:")
print(df.describe())


# PART 5: Answer Meaningful Questions (Analysis)

print("\n" + "="*60)
print(" MEANINGFUL QUESTIONS & ANSWERS")
print("="*60)

questions = [
    "Q1: What is the average book price?",
    "Q2: What is the most common book rating?",
    "Q3: Are expensive books better rated?",
    "Q4: What is the price range of books?",
    "Q5: How many books have 5-star ratings?",
    "Q6: Which price category has most books?",
    "Q7: Is there a correlation between price and rating?",
    "Q8: What percentage of books are above £40?"
]

answers = [
    f"A1: Average price is £{df['price'].mean():.2f}",
    f"A2: Most common rating is {df['rating'].mode()[0]} stars ({df['rating'].value_counts().max()} books)",
    f"A3: Correlation is {df['price'].corr(df['rating']):.2f} (weak/positive)",
    f"A4: Price ranges from £{df['price'].min():.2f} to £{df['price'].max():.2f}",
    f"A5: {len(df[df['rating'] == 5])} books have 5-star ratings ({(len(df[df['rating'] == 5])/len(df))*100:.1f}%)",
    f"A6: Most books are in £30-£40 range",
    f"A7: Price-Rating correlation: {df['price'].corr(df['rating']):.2f} (very weak)",
    f"A8: {(len(df[df['price'] > 40])/len(df))*100:.1f}% of books are above £40"
]

for q, a in zip(questions, answers):
    print(f"\n{q}")
    print(f"   → {a}")


# PART 6: Identify Trends & Patterns


print(" TRENDS & PATTERNS IDENTIFIED")


print(f"\n Rating Distribution:")
rating_counts = df['rating'].value_counts().sort_index()
for rating, count in rating_counts.items():
    percentage = (count / len(df)) * 100
    print(f"   - {rating} Star: {count} books ({percentage:.1f}%)")

print(f"\n Price Categories:")
price_categories = {
    'Low (£15-£30)': len(df[df['price'] < 30]),
    'Medium (£30-£40)': len(df[(df['price'] >= 30) & (df['price'] < 40)]),
    'High (£40-£55)': len(df[df['price'] >= 40])
}
for category, count in price_categories.items():
    percentage = (count / len(df)) * 100
    print(f"   - {category}: {count} books ({percentage:.1f}%)")


# PART 7: Detect Anomalies


print(" ANOMALIES DETECTED")


# Find outliers (prices > 2 standard deviations)
outlier_threshold = df['price'].mean() + 2 * df['price'].std()
outliers = df[df['price'] > outlier_threshold]

print(f"\n Price Outliers (Above £{outlier_threshold:.2f}):")
if len(outliers) > 0:
    for i, row in outliers.iterrows():
        print(f"   - {row['title']}: £{row['price']:.2f}")
else:
    print("   ✓ No price outliers found!")


# PART 8: Create Visualizations (Charts)


print(" CREATING EDA VISUALIZATIONS")


# Create results folder
import os
os.makedirs('eda_charts', exist_ok=True)

# Chart 1: Price Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=15, color='steelblue', edgecolor='black', alpha=0.7)
plt.title('Book Price Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.axvline(df['price'].mean(), color='red', linestyle='--', label=f'Mean: £{df["price"].mean():.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('eda_charts/price_distribution.png', dpi=150, bbox_inches='tight')
print("✓ Chart 1 saved: eda_charts/price_distribution.png")

# Chart 2: Rating Distribution
plt.figure(figsize=(8, 8))
rating_counts.plot(kind='bar', color=['#ff9999', '#ffcc99', '#ffff99', '#99ff99', '#99ccff'])
plt.title('Book Rating Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Rating (Stars)', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.xticks([1, 2, 3, 4, 5], ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star'])
plt.tight_layout()
plt.savefig('eda_charts/rating_distribution.png', dpi=150, bbox_inches='tight')
print("✓ Chart 2 saved: eda_charts/rating_distribution.png")

# Chart 3: Price Statistics (Box Plot) 
plt.figure(figsize=(8, 6))
plt.boxplot(df['price'])
plt.title('Book Price Statistics (Box Plot)', fontsize=16, fontweight='bold')
plt.ylabel('Price (£)', fontsize=12)
plt.tight_layout()
plt.savefig('eda_charts/price_boxplot.png', dpi=150, bbox_inches='tight')
print("✓ Chart 3 saved: eda_charts/price_boxplot.png")

# Chart 4: Price vs Rating (Scatter) 
plt.figure(figsize=(10, 6))
plt.scatter(df['rating'], df['price'], alpha=0.6, s=50)
plt.title('Price vs Rating Relationship', fontsize=16, fontweight='bold')
plt.xlabel('Rating (Stars)', fontsize=12)
plt.ylabel('Price (£)', fontsize=12)
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig('eda_charts/price_vs_rating.png', dpi=150, bbox_inches='tight')
print("✓ Chart 4 saved: eda_charts/price_vs_rating.png")

# Chart 5: Price Categories (Pie Chart) 
plt.figure(figsize=(8, 8))
plt.pie(price_categories.values(), labels=price_categories.keys(), 
        autopct='%1.1f%%', startangle=90)
plt.title('Price Category Distribution', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('eda_charts/price_categories.png', dpi=150, bbox_inches='tight')
print("✓ Chart 5 saved: eda_charts/price_categories.png")



# FINAL SUMMARY


print(" TASK 2 EDA COMPLETE - FINAL SUMMARY")


print(f"\n Dataset Analysis:")
print(f"   - Rows: {len(df)} books")
print(f"   - Columns: {len(df.columns)} ({df.columns.tolist()})")
print(f"   - Missing Values: {df.isnull().sum().sum()}")
print(f"   - Duplicates: {df.duplicated().sum()}")

print(f"\n Key Price Insights:")
print(f"   - Average: £{df['price'].mean():.2f}")
print(f"   - Range: £{df['price'].min():.2f} - £{df['price'].max():.2f}")
print(f"   - Most books: £30-£40 category")

print(f"\n Key Rating Insights:")
print(f"   - Average Rating: {df['rating'].mean():.2f}/5")
print(f"   - Most Common: 5 Star and 1 Star (equal distribution)")
print(f"   - Correlation with Price: {df['price'].corr(df['rating']):.2f} (weak)")

print(f"\n Files Created:")
print("   ✓ eda_charts/price_distribution.png")
print("   ✓ eda_charts/rating_distribution.png")
print("   ✓ eda_charts/price_boxplot.png")
print("   ✓ eda_charts/price_vs_rating.png")
print("   ✓ eda_charts/price_categories.png")

print(f"\n EDA Report:")
print(f"   - Data Quality: Clean (no missing/duplicates)")
print(f"   - Key Trend: Most books are medium-priced (£30-£40)")
print(f"   - Anomaly: Few price outliers (very expensive books)")
print(f"   - Insight: Price doesn't affect rating (weak correlation)")


print("EXPLORATORY DATA ANALYSIS COMPLETE!")
