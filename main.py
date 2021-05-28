from utils.sql_connect import Sql_Connect
from utils.api import Api
import requests
import pandas as pd


def main():

    mlb = Sql_Connect("192.168.1.207","freenas", "mlbapp")
    
    url = "https://mlb-data.p.rapidapi.com/json/"

    query = {"name_part":"'%'",
             "sport_code":"'mlb'",
             "active_sw":"'Y'"}


    api = Api(url, query, "x-rapidapi-key", "mlb_rapid" )
    
    response = api.get_response("named.search_player_all.bam")

    data = response["search_player_all"]["queryResults"]["row"]
    
    cols = mlb.get_columns("PLAYER_INFO")
    cols = [col[0].lower() for col in cols]

    df = pd.DataFrame.from_dict(data)
    df =df[cols]

    mlb.insert(df, 'PLAYER_INFO' )

main()
