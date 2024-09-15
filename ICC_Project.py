import requests  
from bs4 import BeautifulSoup 
import pandas as pd  

# Step 1: Webpage request
url = 'https://www.espncricinfo.com/rankings/icc-team-ranking'  # Icc - Team Ranking Link

r = requests.get(url)  

# Step 2: html content ko parse usin beautifulsoup
soup = BeautifulSoup(r.content, 'html.parser') 

# Step 3: Table heading and tables
headings = soup.find_all(['h2', 'h3', 'h4'])  

tables = soup.find_all('table')  

# Step 4: Loop through each table and extract the data

for i, table in enumerate(tables): # this is for getting index (i) as well

    # Get the heading for the table

    heading = headings[i].text.strip() if i < len(headings) else f"Table {i+1}"
    
    # Extract table headers rows data 
    
    rows = table.find_all('tr')  
    headers = [th.text.strip() for th in rows[0].find_all('th')]  

    # Extract the rows of data from the table
    table_data = []
    for row in rows[1:]:  
        cells = row.find_all('td')  
        row_data = [cell.text.strip() for cell in cells]  
        table_data.append(row_data)  

    # Step 5: Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(table_data, columns=headers)  

    # Step 6: Clean up the heading to use as a filename
    clean_heading = heading.replace(' ', '_').replace('/', '_').replace('\\', '_')
    
    CricInfo = f"{clean_heading}.csv"  # clean heading se csv filename construct and saved as .csv

    # Step 7: save in csv file
    
    df.to_csv(CricInfo, index=False)   # .to_csv means file ko csv me save krna [ .to_json, txt, more ]
    print(f"Saved: {CricInfo}") 
    
