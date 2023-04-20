#main.py
from fangraph_scrape import Fangraph_scrape

def main():
    try:
        
        #fangraphs urls
        TEAMS_URL = 'https://www.fangraphs.com/depthcharts.aspx?position=Standings'
        
        #fangraph object will handle beautiful soup and selenium for web scrapping.
        fangraph = Fangraph_scrape()

        #scrape the teams page and load into dataframe
        team_soup = fangraph.get_soup_page(TEAMS_URL)
        team_df = fangraph.team(team_soup)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
