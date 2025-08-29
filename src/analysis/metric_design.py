import pandas as pd
from scipy.stats import zscore
import numpy as np

def calculate_clutch_score(df):
    df = df.copy()

    df['TS%'] = df['PTS'] / (2 * (df['FGA'] + 0.44 * df['FTA']))
    df['TS%'] = df['TS%'].fillna(0)

    df['TOV_per_min'] = df['TOV_per_min'].replace(0, 1e-6)
    df['PTS36'] = df['PTS_per_min'] * 36

    df['WIN_PCT'] = df['WL'].apply(lambda x: 1 if x == 'W' else 0)
    win_pct = df.groupby('PLAYER_NAME')['WIN_PCT'].mean().reset_index()
    df = df.merge(win_pct, on='PLAYER_NAME', suffixes=('', '_overall'))

    features = pd.DataFrame()
    features['PTS36'] = df.groupby('PLAYER_NAME')['PTS36'].mean()
    features['TS%'] = df.groupby('PLAYER_NAME')['TS%'].mean()

    ast_avg = df.groupby('PLAYER_NAME')['AST_per_min'].mean()
    tov_avg = df.groupby('PLAYER_NAME')['TOV_per_min'].mean()
    ast_to_ratio = ast_avg / tov_avg
    ast_to_ratio = ast_to_ratio.clip(upper=10)
    features['AST_TO'] = ast_to_ratio

    features['WIN_PCT'] = df.groupby('PLAYER_NAME')['WIN_PCT_overall'].mean()

    for col in features.columns:
        if features[col].nunique() > 1:
            features[col + '_z'] = zscore(features[col])
        else:
            features[col + '_z'] = 0

    features['CLUTCH_SCORE'] = (
        0.4 * features['PTS36_z'] +
        0.3 * features['TS%_z'] +
        0.2 * features['AST_TO_z'] +
        0.1 * features['WIN_PCT_z']
    )

    return features.sort_values('CLUTCH_SCORE', ascending=False)

def main():
    df = pd.read_csv('data/expanded_clutch_dataset.csv')
    clutch_ranking = calculate_clutch_score(df)
    clutch_ranking.to_csv('data/clutch_ranking.csv')
    print(clutch_ranking.head(15))

if __name__ == "__main__":
    main()
