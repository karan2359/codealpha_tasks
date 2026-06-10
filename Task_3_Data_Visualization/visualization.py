# visualization.py - TASK 3: Data Visualization (100% WORKING)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.dpi'] = 100

# Load dataset
print("Loading dataset...")
df = pd.read_csv('books_dataset.csv')

print(f" Dataset loaded: {len(df)} books")
print(f"\nDataset preview:")
print(df.head())

# Clean price column (remove £ symbol)
df['price'] = df['price'].str.replace('£', '').astype(float)

# Fix rating column
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['rating'] = df['rating'].map(rating_map)

print(f"\n Data cleaned: {len(df)} valid books")

# ============================================
# CHART 1: Price Distribution
# ============================================
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='price', bins=20, kde=True, color='steelblue')
plt.title('Distribution of Book Prices', fontsize=16, fontweight='bold')
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.tight_layout()
plt.savefig('chart1_price_distribution.png', dpi=150, bbox_inches='tight')
print(" Chart 1 saved")

# ============================================
# CHART 2: Top 10 Most Expensive
# ============================================
top_10 = df.nlargest(10, 'price')
plt.figure(figsize=(12, 8))
plt.barh(top_10['title'], top_10['price'], color='coral')
plt.title('Top 10 Most Expensive Books', fontsize=16, fontweight='bold')
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Book Title', fontsize=12)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('chart2_top10_expensive.png', dpi=150, bbox_inches='tight')
print(" Chart 2 saved")


# CHART 3: Rating Distribution (Pie)

rating_counts = df['rating'].value_counts().sort_index()
labels = ['1 Star', '2 Stars', '3 Stars', '4 Stars', '5 Stars']
colors_pie = ['#ff9999', '#ffcc99', '#ffff99', '#99ff99', '#99ccff']

plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=labels, autopct='%1.1f%%', 
        startangle=90, colors=colors_pie)
plt.title('Book Rating Distribution', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('chart3_rating_distribution.png', dpi=150, bbox_inches='tight')
print(" Chart 3 saved")


# CHART 4: Price vs Rating (Scatter)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['rating'], df['price'], 
                      c=df['price'], cmap='viridis', 
                      alpha=0.6, edgecolors='black', s=100)
plt.colorbar(scatter, label='Price (£)')
plt.title('Price vs Rating Relationship', fontsize=16, fontweight='bold')
plt.xlabel('Rating (Stars)', fontsize=12)
plt.ylabel('Price (£)', fontsize=12)
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig('chart4_price_vs_rating.png', dpi=150, bbox_inches='tight')
print(" Chart 4 saved")


# CHART 5: Dashboard 

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Book Data Analysis Dashboard', fontsize=18, fontweight='bold', y=1.02)

# Chart 5a: Price Distribution 
axes[0, 0].hist(df['price'], bins=15, color='steelblue', alpha=0.7)
axes[0, 0].set_title('Price Distribution', fontweight='bold')
axes[0, 0].set_xlabel('Price (£)')
axes[0, 0].set_ylabel('Number of Books')

# Chart 5b: Rating Count 
axes[0, 1].bar(rating_counts.index, rating_counts.values, color=colors_pie)
axes[0, 1].set_title('Rating Count', fontweight='bold')
axes[0, 1].set_xlabel('Rating (Stars)')
axes[0, 1].set_ylabel('Number of Books')
axes[0, 1].set_xticks([1, 2, 3, 4, 5])
axes[0, 1].set_xticklabels(['1 Star', '2 Star', '3 Star', '4 Star', '5 Star'])

# Chart 5c: Top 10 Most Expensive 
axes[1, 0].barh(top_10['title'], top_10['price'], color='coral')
axes[1, 0].set_title('Top 10 Most Expensive', fontweight='bold')
axes[1, 0].set_xlabel('Price (£)')
axes[1, 0].invert_yaxis()

# Chart 5d: Price vs Rating 
axes[1, 1].scatter(df['rating'], df['price'], alpha=0.5, color='green', s=50)
axes[1, 1].set_title('Price vs Rating', fontweight='bold')
axes[1, 1].set_xlabel('Rating (Stars)')
axes[1, 1].set_ylabel('Price (£)')
axes[1, 1].set_xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig('dashboard_complete.png', dpi=150, bbox_inches='tight')
print(" Dashboard saved")


# Summary

print("\n" + "="*60)
print(" DATA VISUALIZATION COMPLETE!")
print("="*60)
print(f"\n Total Books: {len(df)}")
print(f" Average Price: £{df['price'].mean():.2f}")
print(f" Lowest Price: £{df['price'].min():.2f}")
print(f" Highest Price: £{df['price'].max():.2f}")
print(f" Average Rating: {df['rating'].mean():.1f}/5")
print(f"\n Files Created:")
print("   chart1_price_distribution.png")
print("   chart2_top10_expensive.png")
print("   chart3_rating_distribution.png")
print("   chart4_price_vs_rating.png")
print("   dashboard_complete.png")
print("\n COMPLETE!")