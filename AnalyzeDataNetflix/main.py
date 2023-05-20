import pandas as pd 
import matplotlib.pyplot as plt

# ANALYZE YOUR NETFLIX DATA 

# Data Preparation
df = pd.read_csv()

# Data Analysis
# Total watch time over time
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime format
df['Month'] = df['Date'].dt.to_period('M')  # Extract month from 'Date' column
df['Minutes'] = df['Duration'].str.extract('(\d+)').astype(int)  # Extract minutes from 'Duration' column
df['TotalMinutes'] = df.groupby('Month')['Minutes'].transform('sum')  # Calculate total minutes per month
df['CumulativeMinutes'] = df.groupby('Month')['TotalMinutes'].cumsum()  # Calculate cumulative minutes over time

# Most-Watched shows/Movies
top_watched = df['Title'].value_counts().head(10)

# Prefered genres
genre_counts = df['Genre'].value_coutns()
top_genres = genre_counts.head(5) # Get top 5 most-watched genres

# Viewing habits
day_of_week_counts = df['DayOfWeek'].value_counts().sort_index()
time_of_day_counts = df['Hour'].value_counts().sort_index()

# Step 4: Data Visualization
# Total watch time over time
plt.figure(figsize=(10, 6))
plt.plot(df['Month'].unique(), df.groupby('Month')['CumulativeMinutes'].max())
plt.xlabel('Month')
plt.ylabel('Cumulative Watch Time (minutes)')
plt.title('Netflix Watch Time Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Most-watched shows/movies
plt.figure(figsize=(10, 6))
top_watched.plot(kind='bar')
plt.xlabel('Show/Movie')
plt.ylabel('Watch Count')
plt.title('Top 10 Most-Watched Shows/Movies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Preferred genres
plt.figure(figsize=(8, 8))
top_genres.plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal')
plt.title('Top 5 Preferred Genres')
plt.tight_layout()
plt.show()

# Viewing habits
plt.figure(figsize=(10, 6))
day_of_week_counts.plot(kind='bar')
plt.xlabel('Day of Week')
plt.ylabel('Watch Count')
plt.title('Viewing Habits by Day of Week')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
time_of_day_counts.plot(kind='bar')
plt.xlabel('Hour of Day')
plt.ylabel('Watch Count')
plt.title('Viewing Habits by Time of Day')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Step 5: Presentation and Interpretation
# You can add your own interpretation and summary of the analyzed data here.
