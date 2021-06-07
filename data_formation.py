import pandas as pd

from riot_api_connection import riot_api

api = riot_api()

# TR PLAT LEAGUE DATA COLLECTION

api.get_all_league_entries_by_queue_tier_division()

tr_plat_i = api.get_all_league_entries_by_queue_tier_division(division='I')
tr_i = pd.DataFrame.from_dict(tr_plat_i[0], orient='index')

tr_plat_ii = api.get_all_league_entries_by_queue_tier_division(division='II')

tr_plat_iii = api.get_all_league_entries_by_queue_tier_division(division='III')

tr_plat_iv = api.get_all_league_entries_by_queue_tier_division(division='IV')

# PAST GAMES FOR ALL SUMMONERS IN TR PLAT LEAGUE

columns = pd.DataFrame.from_dict(tr_plat_i[0], orient='index').columns
tr_plat_all = pd.DataFrame(columns=columns)

tr_plat_comb = [tr_plat_i, tr_plat_ii, tr_plat_iii, tr_plat_iv]

for division in tr_plat_comb:
    for summoner in division:
        df = pd.DataFrame.from_dict(summoner, orient='index').transpose()
        tr_plat_all = pd.concat([tr_plat_all, df])

tr_plat_all.reset_index(inplace=True)




