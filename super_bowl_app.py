import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Super Bowl Insights", layout="wide")

# Title
st.title("🏈 The Drama Behind the Super Bowl")

# Load Data
super_bowls = pd.read_csv("super_bowls.csv")
tv_data = pd.read_csv("tv_data.csv")
halftime_show = pd.read_csv("halftime_show_artists.csv")

# Section 1: Game Results
st.header("1. Game Results")
st.write("Explore the winning and losing teams, scores, and MVPs of Super Bowl games.")

# Select relevant and correctly named columns
display_data = super_bowls[[ 
    'super_bowl', 'date', 'team_winner', 'team_loser', 
    'winning_pts', 'losing_pts', 'qb_winner_1'
]].rename(columns={
    'super_bowl': 'Super Bowl',
    'date': 'Date',
    'team_winner': 'Winner',
    'team_loser': 'Loser',
    'winning_pts': 'Winner Points',
    'losing_pts': 'Loser Points',
    'qb_winner_1': 'Winning QB'
})

st.dataframe(display_data)

# Section 2: TV Viewership Trends
st.header("2. 📺 TV Viewership Over the Years")
st.write("Viewership trends and how the Super Bowl captured audiences over time.")

# Adjusting columns to match the tv_data columns
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=tv_data, x="super_bowl", y="total_us_viewers", marker="o", ax=ax)  # Update 'viewers' column name to 'total_us_viewers'
ax.set_title("Super Bowl Viewership Over Time")
ax.set_xlabel("Super Bowl")
ax.set_ylabel("Total US Viewers (in millions)")
st.pyplot(fig)

# Section 3: 🎤 Halftime Shows
st.header("3. 🎤 Halftime Show Artists")
st.write("Explore artists who performed at the Super Bowl halftime shows.")

# Modify to include `musician` and `num_songs`
top_artists = halftime_show['musician'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_artists.values, y=top_artists.index, palette="viridis", ax=ax2)
ax2.set_title("Top 10 Most Frequent Halftime Show Performers")
ax2.set_xlabel("Number of Performances")
ax2.set_ylabel("Artist")
st.pyplot(fig2)

# Section 4: Halftime Show Song Count
st.header("4. 🎶 Number of Songs Per Halftime Show")
st.write("Explore the number of songs performed by the artists during the halftime show.")

# Calculate the total number of songs performed by the top artists
top_songs = halftime_show.groupby('musician')['num_songs'].sum().sort_values(ascending=False).head(10)
fig3, ax3 = plt.subplots()
sns.barplot(x=top_songs.values, y=top_songs.index, palette="viridis", ax=ax3)
ax3.set_title("Top 10 Artists by Total Number of Songs")
ax3.set_xlabel("Total Songs")
ax3.set_ylabel("Artist")
st.pyplot(fig3)

# Footer
st.markdown("---")
