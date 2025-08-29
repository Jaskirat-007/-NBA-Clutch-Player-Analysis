from nba_api.stats.endpoints import leaguedashplayerclutch
import pandas as ps
import time

def get_clutch_stats(season = "2024-25", per_mode="PerGame"):
    time.sleep(1)
    clutch = leaguedashplayerclutch.LeagueDashPlayerClutch(
        season=season,
        last_n_games=0,
        clutch_time="Last 5 Minutes",
        ahead_behind="Ahead or Behind",
        point_diff=5,
        per_mode_detailed=per_mode,
        measure_type_detailed_defense="Base"
    )
    
    dataframe = clutch.get_data_frames()[0]
    return dataframe

