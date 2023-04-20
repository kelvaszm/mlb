#main.py
from fangraph_scrape import Fangraph_scrape

def main():
    try:
        
        #fangraphs urls
        TEAMS_URL = 'https://www.fangraphs.com/depthcharts.aspx?position=Standings'
        ROSTER_URL = 'https://www.fangraphs.com/teams/mets'
        
        #fangraph object will handle beautiful soup and selenium for web scrapping.
        fangraph = Fangraph_scrape()

        #scrape the teams page and load into dataframe
        team_soup = fangraph.get_soup_page(TEAMS_URL)
        team_df = fangraph.team(team_soup)

        #scrape the player rosters from each team and load into dataframe
        roster_soup = fangraph.get_soup_page(ROSTER_URL)
        roster_list = fangraph.roster(roster_soup)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
