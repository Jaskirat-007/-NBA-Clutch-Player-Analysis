from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
from time import sleep

season = "2023-24"
clutch_df = pd.read_csv("data/clutch_stats.csv")

all_players = players.get_active_players()
id_map = {p['full_name']: p['id'] for p in all_players}
clutch_df['PLAYER_ID'] = clutch_df['PLAYER_NAME'].map(id_map)
clutch_df = clutch_df.dropna(subset=['PLAYER_ID'])

game_logs = []
for pid in clutch_df['PLAYER_ID'].unique():
    logs = playergamelog.PlayerGameLog(player_id=pid, season=season).get_data_frames()[0]
    logs['PLAYER_ID'] = pid
    game_logs.append(logs)
    sleep(1)

full_logs = pd.concat(game_logs, ignore_index=True)
expanded = full_logs.merge(clutch_df, on='PLAYER_ID', suffixes=('_game', '_clutch'))
expanded.to_csv("data/expanded_clutch_dataset.csv", index=False)
print(expanded.shape)
