#main.py
from fangraph_scrape import Fangraph_scrape
from sql_connect import Sql_connect
from config import Config
import pandas
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
    
    #df cols need to match the sql table
    cols = sql.get_column_datatypes('TEAMS')
    team_df.columns = [col[0] for col in cols]
    
    #insert teams into database
    row_count = sql.load(team_df, 'TEAMS')
    
    print(str(row_count) + ' rows interted into TEAMS')
    
    #scrape the player rosters from each team and load into dataframe
    roster_soup = fangraph.get_soup_page(roster_url)
    roster_list = fangraph.roster(roster_soup)


if __name__ == '__main__':
    main()
