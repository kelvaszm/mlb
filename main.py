#main.py
from fangraph_scrape import Fangraph_scrape
from sql_connect import Sql_connect
from config import Config
import pandas
import numpy

def main():
    
    #yaml config
    config = Config()

    #fangraphs urls
    teams_url = config['team_path']
    roster_url = config['roster_path']
    
    #fangraph object will handle beautiful soup and selenium for web scrapping.
    fangraph = Fangraph_scrape()

    #sql connect object will handle mysql connection
    sql = Sql_connect(config['database'])
    
    #scrape the teams page and load into dataframe
    team_soup = fangraph.get_soup_page(teams_url)
    team_df = fangraph.team(team_soup)
    
    #insert teams into database
    row_count = process_df(team_df, sql, 'TEAMS')
    print(str(row_count) + ' rows inserted into TEAMS')

    #scrape the player rosters from each team and load into dataframe
    for team in team_df.itertuples(index=False):
        
        roster_soup = fangraph.get_soup_page(roster_url + team[1].replace(' ', '-'))
        roster_list = fangraph.roster(roster_soup, team[0])
        
        #load each team roster into database
        row_count = process_df(roster_list[0], sql, 'PLAYERS_HITTING')
        print(str(row_count) + ' rows inserted for ' + team[1] + ' into PLAYERS_HITTING')

        row_count = process_df(roster_list[1], sql, 'PLAYERS_PITCHING')
        print(str(row_count) + ' rows inserted for ' + team[1] + ' into PLAYERS_PITCHING')


def process_df(df, sql, table_name):
    #df cols need to match the sql table
    cols = sql.get_column_datatypes(table_name)
    df.columns = [col[0] for col in cols]
    
    #replace None with Nans
    df = df.fillna(value=numpy.nan)
    
    #remove any percent signs
    for col in df.items():
        if(col[1].dtype == 'object'):
            df[col[0]] = df[col[0]].astype(str).str.replace('%', '')

    #insert df into database
    return sql.load(df, table_name)


if __name__ == '__main__':
    main()
