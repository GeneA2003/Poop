import pandas as pd

bus_stops_table = pd.read_csv("Bus_Stops_of_NJ_Transit_by_Line.csv", na_values=["NA"])
land_use_table = pd.read_csv("Land_Use_Land_Cover_of_New_Jersey_2020.csv", na_values=["NA"])
income_table = pd.read_csv("LOW_MOD_INCOME_BY_BG_-8762454996677272279.csv", na_values=["NA"])
group_table = pd.read_csv("BlkGroup_Data_.csv", na_values=["NA"])
bus_stops_table.info()
land_use_table.info()
income_table.info()
group_table.info()
#print(bus_stops_table)
