import pandas as pd

from riot_api_connection import riot_api

api = riot_api()

# TR PLAT LEAGUE DATA COLLECTION

api.get_all_league_entries_by_queue_tier_division()

tr_plat_i = api.get_all_league_entries_by_queue_tier_division(division='I')
tr_plat_i = pd.DataFrame.from_dict(tr_plat_i[0], )

tr_plat_ii = api.get_all_league_entries_by_queue_tier_division(division='II').json()

tr_plat_iii = api.get_all_league_entries_by_queue_tier_division(division='III').json()

tr_plat_iv = api.get_all_league_entries_by_queue_tier_division(division='IV').json()








