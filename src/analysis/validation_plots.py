import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv('data/clutch_ranking.csv')

    plt.figure(figsize=(10, 6))
    top10 = df.head(10)
    sns.barplot(data=top10, x='CLUTCH_SCORE', y=top10.index, orient='h')
    plt.title('Top 10 Players by Clutch Score')
    plt.xlabel('Clutch Score')
    plt.ylabel('Player Rank')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='TS%', y='CLUTCH_SCORE')
    plt.title('Clutch Score vs True Shooting %')
    plt.xlabel('TS%')
    plt.ylabel('Clutch Score')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
