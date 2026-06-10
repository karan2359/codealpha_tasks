#  Data Science Internship Projects

##  Author
**Name:** Karan Pardeshi  
**Location:** Chalisgaon Dis. Jalgaon , Maharashtra, India  
**Email:** pardeshikaran060@gmail.com


---

##  Project Overview

This repository contains completed projects from my Data Science internship, covering three key areas:
1. Web Scraping (Task 1)
2. Exploratory Data Analysis (Task 2)
3. Data Visualization (Task 3)

All projects use a **book dataset** scraped from `books.toscrape.com` containing 60 books with titles, prices, and ratings.

---


---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Main programming language |
| **BeautifulSoup4** | HTML parsing for web scraping |
| **Requests** | HTTP requests for fetching web pages |
| **Pandas** | Data manipulation and analysis |
| **Matplotlib** | Creating charts and visualizations |
| **Seaborn** | Statistical data visualization |
| **NumPy** | Numerical computations |

---

##  Task 1: Web Scraping

###  Objective
Extract book data (title, price, rating) from a public website using Python.

###  How It Works
1. Fetches webpage using `requests.get()`
2. Parses HTML with `BeautifulSoup`
3. Extracts book data using `find_all()` and `find()`
4. Scrapes 3 pages (60 books total)
5. Saves data to CSV format

###  Files
- `Task_1_web_scraping_internship/scraper.py` - Main scraping script
- `Task_1_web_scraping_internship/books_dataset.csv` - Output dataset

###  Run the Script
```bash
cd Task_1_web_scraping_internship
python scraper.py
```

###  Dataset Details
- **Total Books:** 60
- **Columns:** title, price, rating
- **Source:** https://books.toscrape.com/

###  Requirements Met
-  Used Python library (BeautifulSoup)
-  Extracted data from public web pages
-  Handled HTML structure and navigation
-  Created custom dataset (CSV)

---

##  Task 2: Exploratory Data Analysis (EDA)

###  Objective
Analyze the book dataset to identify trends, patterns, statistics, and data quality issues.

###  Key Analysis Performed
1. **Data Quality Check**
   - Missing values: 0 (clean data)
   - Duplicate rows: 0 (no duplicates)

2. **Statistical Summary**
   - Average Price: £35.00
   - Price Range: £12.84 - £57.31
   - Average Rating: 3.00/5 stars
   - Price-Rating Correlation: -0.03 (very weak)

3. **Meaningful Questions Answered**
   - Q1: What is the average book price? → £35.00
   - Q2: What is the most common rating? → 1 star (15 books)
   - Q3: Are expensive books better rated? → No (correlation: -0.03)
   - Q4: Price range? → £12.84 to £57.31
   - Q5: How many 5-star books? → 14 books (23.3%)

4. **Trends & Patterns**
   - Rating Distribution: 1 Star (25%), 2 Star (13%), 3 Star (22%), 4 Star (17%), 5 Star (23%)
   - Price Categories: Low (£15-£30): 40%, Medium (£30-£40): 20%, High (£40-£55): 40%

5. **Anomalies Detected**
   - No price outliers found (all prices within normal range)

###  Files
- `Task_2_Exploratory_Data_Analysis/eda_analysis.py` - EDA script
- `Task_2_Exploratory_Data_Analysis/eda_charts/` - 5 generated charts

###  Run the Script
```bash
cd Task_2_Exploratory_Data_Analysis
python eda_analysis.py
```

###  Charts Generated
1. `price_distribution.png` - Price histogram
2. `rating_distribution.png` - Rating bar chart
3. `price_boxplot.png` - Price statistics box plot
4. `price_vs_rating.png` - Price vs Rating scatter
5. `price_categories.png` - Price categories pie chart

###  Requirements Met
-  Asked meaningful questions about dataset
-  Explored data structure (variables, data types)
-  Identified trends, patterns, anomalies
-  Tested hypotheses with statistics
-  Detected data issues (none found - clean data)

---

##  Task 3: Data Visualization

###  Objective
Transform raw book data into professional visual charts and dashboards.

###  Visualizations Created
1. **Price Distribution (Histogram)**
   - Shows distribution of book prices
   - Most books priced between £20-£50

2. **Top 10 Most Expensive Books (Horizontal Bar)**
   - Lists highest-priced books
   - Top price: £57.31

3. **Rating Distribution (Pie Chart)**
   - Shows percentage of each rating
   - Balanced distribution across all ratings

4. **Price vs Rating (Scatter Plot)**
   - Reveals relationship between price and rating
   - Weak correlation (-0.03)

5. **Complete Dashboard**
   - All 4 charts combined in one professional view
   - Easy to understand insights

###  Files
- `Task_3_Data_Visualization/visualization.py` - Visualization script
- 5 PNG chart files in the same folder

###  Run the Script
```bash
cd Task_3_Data_Visualization
python visualization.py
```

###  Charts Generated
1. `chart1_price_distribution.png` - Price histogram
2. `chart2_top10_expensive.png` - Top 10 expensive books
3. `chart3_rating_distribution.png` - Rating pie chart
4. `chart4_price_vs_rating.png` - Price vs Rating scatter
5. `dashboard_complete.png` - Complete dashboard

###  Requirements Met
-  Transformed raw data into visual formats (charts/graphs)
-  Used Matplotlib and Seaborn tools
-  Designed visuals that enhance understanding
-  Crafted data stories supporting decision-making
-  Built portfolio with impactful visualizations

---

##  Key Insights from All Tasks

###  Price Insights
- **Average Book Price:** £35.00
- **Most Common Range:** £30-£40 (20% of books)
- **Lowest Price:** £12.84
- **Highest Price:** £57.31

###  Rating Insights
- **Average Rating:** 3.00/5 stars
- **Most Common Rating:** 1 star (25% of books)
- **5-Star Books:** 14 books (23.3%)
- **Price-Rating Correlation:** -0.03 (very weak - expensive books NOT better rated)

###  Business Insights
1. Price doesn't affect book quality (weak correlation)
2. Balanced rating distribution (no bias toward high/low ratings)
3. Most affordable books are in £15-£30 range (40% of catalog)

---

##  Learning Outcomes

### Skills Developed
- ✅ Web scraping with BeautifulSoup
- ✅ HTML parsing and data extraction
- ✅ Data cleaning and preprocessing
- ✅ Statistical analysis (mean, median, correlation)
- ✅ Data visualization (charts, dashboards)
- ✅ Python programming (Pandas, NumPy, Matplotlib, Seaborn)
- ✅ Data quality assessment

### Tools Mastered
- Python 3.13
- VS Code
- BeautifulSoup4
- Requests
- Pandas
- Matplotlib
- Seaborn

---

##  Contact

For questions or collaboration:
- **Email:** [your-email@example.com]
- **GitHub:** [your-github-profile]
- **LinkedIn:** [your-linkedin-profile]

---

##  License

This project is part of my Data Science internship completion.

---

** Completed by Karan Pardeshi | June 2026**
