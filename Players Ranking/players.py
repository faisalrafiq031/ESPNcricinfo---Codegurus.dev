# Players Ranking File - ODI , TEST, T20, WT20 more

import requests
import pandas as pd
from bs4 import BeautifulSoup

# List of URLs for different ranking tables
urls = [
    "http://www.relianceiccrankings.com/ranking/test/batting/",  # Test Batting rankings
    "http://www.relianceiccrankings.com/ranking/test/bowling/",   # Test Bowling rankings
    "http://www.relianceiccrankings.com/ranking/test/all-rounder/", # Test All Rounder

    # ODI ranking
    "http://www.relianceiccrankings.com/ranking/odi/all-rounder/",
    "http://www.relianceiccrankings.com/ranking/odi/batting/",
    "http://www.relianceiccrankings.com/ranking/odi/bowling/",
    
    # T20 Ranking
    "http://www.relianceiccrankings.com/ranking/t20/batting/",
    "http://www.relianceiccrankings.com/ranking/t20/bowling/",
    "http://www.relianceiccrankings.com/ranking/t20/all-rounder/",

    # WODI ranking
    "http://www.relianceiccrankings.com/ranking/womenodi/batting/",
    "http://www.relianceiccrankings.com/ranking/womenodi/bowling/",
    "http://www.relianceiccrankings.com/ranking/womenodi/all-rounder/",
    
    # WT20 ranking
    "http://www.relianceiccrankings.com/ranking/woment20/batting/",
    "http://www.relianceiccrankings.com/ranking/woment20/bowling/",
    "http://www.relianceiccrankings.com/ranking/woment20/all-rounder/"
]

# Dictionary to store data for each ranking type and role
data_dict = {}

for url in urls:
    # Get the page content
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    # Identify the type of ranking (test, odi, t20, womenodi, woment20) and role (batting, bowling, all-rounder) from the URL
    ranking_type = url.split('/')[-3]  # test, odi, t20, womenodi, woment20
    role = url.split('/')[-2]  # batting, bowling, all-rounder
    
    # Create a unique key for each ranking type and role
    key = f"{ranking_type}_{role}"
    
    # Initialize a list to accumulate data for each key if it doesn't exist
    if key not in data_dict:
        data_dict[key] = []
    
    for i, table in enumerate(tables):
        rows = table.find_all('tr')
        
        # Extract headers
        headers = [th.text.strip() for th in rows[0].find_all('th')]
        
        # Extract table data
        for row in rows[1:]:
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            
            # Ensure row_data matches headers count
            if len(row_data) < len(headers):
                row_data += [''] * (len(headers) - len(row_data))  # Pad with empty strings
            elif len(row_data) > len(headers):
                row_data = row_data[:len(headers)]  # Truncate the row
            
            data_dict[key].append(row_data)  # Append data to the correct ranking type and role

# Save each ranking type and role to a separate CSV file
for key, data in data_dict.items():
    # Convert accumulated data to DataFrame
    df = pd.DataFrame(data, columns=headers)
    
    # Clean heading for filename (replace special characters)
    clean_key = key.replace(' ', '_').replace('/', '_').replace('\\', '_')
    
    # Save to CSV
    filename = f"{clean_key}.csv"
    df.to_csv(filename, index=False)
    
    print(f"Saved: {filename}")
