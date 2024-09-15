import requests
from bs4 import BeautifulSoup
import pandas as pd

# URLs for different cricket teams
urls = [
    # 'https://www.espncricinfo.com/cricketers/team/bangladesh-25',
    # 'https://www.espncricinfo.com/cricketers/team/england-1',
    # 'https://www.espncricinfo.com/cricketers/team/india-6',
    # 'https://www.espncricinfo.com/cricketers/team/ireland-29',
    # 'https://www.espncricinfo.com/cricketers/team/new-zealand-5',
    # 'https://www.espncricinfo.com/cricketers/team/pakistan-7',
    # 'https://www.espncricinfo.com/cricketers/team/south-africa-3',
    # 'https://www.espncricinfo.com/cricketers/team/sri-lanka-8',
    # 'https://www.espncricinfo.com/cricketers/team/west-indies-4',
    # 'https://www.espncricinfo.com/cricketers/team/zimbabwe-9',
    # 'https://www.espncricinfo.com/cricketers/team/afghanistan-40',
    # 'https://www.espncricinfo.com/cricketers/team/australia-2'
]

# Loop through each URL
for url in urls:
    # Send a GET request to the URL
    r = requests.get(url)
    
    # Parse the content of the page with BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Find the section containing the player information
    player_section = soup.find('div', {'class': 'ds-grid'})
    
    # Find the heading for the team
    heading = soup.find('h1', {'class' : 'ds-text-title-l'}).text.strip()
    
    # Initialize a list to hold player names
    players = []
    
    # Extract player names
    for player in player_section.find_all('div', {'class': 'ds-p-4'}, limit=10):
        player_name = player.text
        players.append(player_name)
    
    # Create a DataFrame with player names
    df = pd.DataFrame(players, columns=["Player Names"])
    
    # Clean the heading for use in file name
    clean_heading = heading.replace(' ', '_').replace('/', '_').replace('\\', '_')
    
    # Define the CSV file name
    csv_file = f"{clean_heading}.csv"
    
    # Write DataFrame to the CSV file
    df.to_csv(csv_file, index=False)
    
    print(f'Player names have been saved to {csv_file}')

