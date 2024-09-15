import requests
import pandas as pd
from bs4 import BeautifulSoup

# List of URLs for different player profiles
urls = [
    
    # TEAM PLAYERS
    
    'https://www.espncricinfo.com/cricketers/craig-ervine-55412/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/chiedza-dhururu-1094714/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/tanaka-chivanga-1059122/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/francisca-chipare-1119417/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/kudzai-chigora-1302575/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/tendai-chatara-425639/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/johnathan-campbell-1120613/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/ryan-burl-495964/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/beloved-biza-1302686/bowling-batting-stats',
    'https://www.espncricinfo.com/cricketers/brian-bennett-1071484/bowling-batting-stats'
    
    
    # ALL PLAYERS URLS Below - I just replaced with other team 
    
]


for url in urls:
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    tables = soup.find_all('table')
    
    all_dataframes = []
    
    for table in tables:
        rows = table.find_all('tr')
        data = []
        
        headers = [th.text.strip() for th in rows[0].find_all('th')]
        
        for row in rows[1:]:
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
        
        df = pd.DataFrame(data, columns=headers)
        
        all_dataframes.append(df)
    
    # Concatenate all tables for this player into one DataFrame
    player_df = pd.concat(all_dataframes, ignore_index=True)
    
    player_name = url.split('/')[-2]  # Gets the player name part from the URL
    
    # Save the DataFrame to a CSV file with the player's name
    player_df.to_csv(f'{player_name}_stats.csv', index=False)

    print(f"Stats saved to '{player_name}_stats.csv'")
