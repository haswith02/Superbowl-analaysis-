import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Super Bowl Dashboard", layout="wide")

# Load data
super_bowls = pd.read_csv("super_bowls.csv")
tv_data = pd.read_csv("tv_data.csv")
halftime_show = pd.read_csv("halftime_show_artists.csv")

# Sidebar
st.sidebar.title("🏈 Super Bowl Dashboard")
section = st.sidebar.radio("Go to", ["Game Results", "TV Viewership", "Halftime Shows", "Summary"])

# Section 1: Game Results
if section == "Game Results":
    st.title("📊 Game Results")
    st.write("Explore winners, losers, scores, and MVPs.")

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

# Section 2: TV Viewership
elif section == "TV Viewership":
    st.title("📺 TV Viewership Over Time")
    st.write("Explore how TV viewership and ad cost changed over the years.")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=tv_data, x="super_bowl", y="avg_us_viewers", marker="o", ax=ax)
    ax.set_title("Average US Viewers Per Super Bowl")
    ax.set_xlabel("Super Bowl")
    ax.set_ylabel("Avg Viewers (millions)")
    st.pyplot(fig)

# Section 3: Halftime Shows
elif section == "Halftime Shows":
    st.title("🎤 Halftime Show Artists")
    st.write("Top artists who performed at the Super Bowl halftime shows.")

    top_artists = halftime_show['musician'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=top_artists.values, y=top_artists.index, palette="viridis", ax=ax2)
    ax2.set_title("Top 10 Most Frequent Halftime Show Performers")
    ax2.set_xlabel("Number of Performances")
    ax2.set_ylabel("Artist")
    st.pyplot(fig2)

# Section 4: Summary
elif section == "Summary":
    st.title("📌 Summary & Highlights")
    st.write("""
    - The Super Bowl is one of the most-watched events on TV.
    - Advertisement costs have increased significantly over the years.
    - A few artists like Beyoncé and Bruno Mars have performed multiple times.
    - MVP quarterbacks often play a crucial role in determining the game outcome.
    """)
    st.markdown("---")
   

