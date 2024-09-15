import pandas as pd
from matplotlib import pyplot as plt
# import os

odi_rankings = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\ICC_ODI_Rankings.csv')
t20i_rankings = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\ICC_WT20I_Rankings.csv')
test_rankings = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\ICC_Test_Rankings.csv')
wodi_rankings = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\ICC_WODI_Rankings.csv')
t20_rankings=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\ICC_T20I_Rankings.csv')

odi_all_round = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\odi_all-rounder.csv')
odi_bat = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\odi_batting.csv')
odi_bowl = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\odi_bowling.csv')
t20_all_round = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\t20_all-rounder.csv')
t20_bat = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\t20_batting.csv')
t20_bowl = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\t20_bowling.csv')
test_all_round=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\test_all-rounder.csv')
test_bat=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\test_batting.csv')
test_bowl=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\test_bowling.csv')
Wodi_all_round=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\womenodi_all-rounder.csv')
Wodi_bat=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\womenodi_batting.csv')
Wodi_bowl=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\womenodi_bowling.csv')
Wt20_all_rounnd=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\woment20_all-rounder.csv')
Wt20_bat=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\woment20_batting.csv')
Wt20_bowl=pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\Players Ranking\woment20_bowling.csv')

def plot_seaoson_rankings(data, title):
    teams = data['Team'][:10]  
    ratings = data['Rating'][:10]
    
    plt.figure(figsize=(10, 6))
    plt.barh(teams, ratings, color='lightgreen')
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Teams', fontsize=12)
    plt.title(title, fontsize=16)
    plt.gca().invert_yaxis()  # Highest rating at the top
    plt.show()

def plot_player_ranking(data, title):
    Name = data['Name'][:5]  # Select the top 5 players by name
    ratings = data['Rating'][:5]  # Select the top 5 ratings
    
    plt.figure(figsize=(10, 6))
    plt.barh(Name, ratings, color='lightgreen')  # Horizontal bar chart
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Name', fontsize=12)
    plt.title(title, fontsize=16)
    plt.gca().invert_yaxis()  # Highest rating at the top
    
    # Add text annotations for each bar
    for i, (rating, name) in enumerate(zip(ratings, Name)):
        plt.text(rating + 5, i, f'{rating}', va='center', fontsize=10)
    
    plt.show()


def display_players():
    # Load the CSV file
    data = pd.read_csv(r'C:\Users\Faisal\Desktop\Project 1\extracted_names.csv')
    
    # Ensure the first column contains player names
    if data.empty:
        print("The CSV file is empty or could not be loaded.")
        return
    
    # List all players
    players = data.iloc[:, 0].unique()
    print("Available players:")
    for idx, player in enumerate(players):
        print(f"{idx + 1}. {player}")
    
    # Get user input for player selection
    try:
        choice = int(input("Enter the number of the player you want to view: ")) - 1
        if choice < 0 or choice >= len(players):
            print("Invalid choice. Please select a valid number.")
            return
        
        selected_player = players[choice]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Display the overview for the selected player
    if selected_player not in data.iloc[:, 0].values:
        print(f"Player '{selected_player}' not found in the CSV file.")
        return
    
    return selected_player


def display_overview_row(row_name='overview'):
    
    player_name=display_players()
    # Load the CSV file
    name = player_name
    folder_path = r"C:\Users\Faisal\Desktop\Project 1\Individual Players"

    # Using os.path.join() for proper path concatenation
    csv_file = os.path.join(folder_path, f"{name} stats.csv")
    data = pd.read_csv(csv_file)
    
    # Check if the row exists
    if row_name not in data.iloc[:, 0].values:
        print(f"Row '{row_name}' not found in the CSV file.")
        return
    
    # Extract the row by its name
    row_data = data[data.iloc[:, 0] == row_name]
    
    # Display the row
    print(f"Displaying  {row_name}")
    print(row_data)


import pandas as pd
import matplotlib.pyplot as plt

def player_bio():
    # List of file paths
    file_paths = [
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Afghanistan_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Australia_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Bangladesh_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\England_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\India_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Ireland_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\New_Zealand_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Pakistan_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\South_Africa_Cricketers.csv',
        r'C:\Users\Faisal\Desktop\Project 1\10 Players Bio\Sri_Lanka_Cricketers.csv'
    ]

    # List of team names
    teams = ['Afghanistan', 'Australia', 'Bangladesh', 'England', 'India', 'Ireland', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka']
    
    # Loop over each file and corresponding team
    for file_path, team in zip(file_paths, teams):
        # Read the CSV file
        cricketers_df = pd.read_csv(file_path)

        # Plot a bar chart of 'Player Name' vs 'Age'
        plt.figure(figsize=(10, 6))
        plt.bar(cricketers_df['Player Name'], cricketers_df['Age'], color='skyblue')

        # Adding labels and title
        plt.xlabel('Player Name')
        plt.ylabel('Age')
        plt.title(f'Age of {team} Cricketers')
        plt.xticks(rotation=45, ha='right')

        # Show the plot
        plt.tight_layout()
        plt.show()





def main():
    while(True):
        print("1. Display Overview of individual Players")
        print("2. Display graphical representation of team rankings")
        print("3. Display 10 player bio")
        print("4. Display graphical representation of player ranking")
        print("5. Exit")
        choice=int(input("Choose the correct option: "))
        if choice == 1:
            display_overview_row()
        #plots for season rankings 
        elif choice ==2:
            plot_seaoson_rankings(odi_rankings, 'Top 10 ODI Team Rankings')
            plot_seaoson_rankings(t20i_rankings, 'Top 10 T20I Team Rankings')
            plot_seaoson_rankings(test_rankings, 'Top 10 Test Team Rankings')
            plot_seaoson_rankings(wodi_rankings, 'Top 10 WODI Team Rankings')
            plot_seaoson_rankings(t20_rankings, 'Top 10 T20 Team Rankings' )
        elif choice==3:
                player_bio()


        elif choice==4:
            plot_player_ranking(odi_all_round, 'Top 5 ODI All Rounder')
            plot_player_ranking(odi_bat, 'Top 5 ODI Batting')
            plot_player_ranking(odi_bowl, 'Top 5 ODI Bowling')
            plot_player_ranking(t20_all_round, 'Top 5 T20 All Rounder')
            plot_player_ranking(t20_bat, 'Top 5 T20 Batting' )
            plot_player_ranking(t20_bowl, 'Top 5 T20 Bowling' )
            plot_player_ranking(test_all_round, 'Top 5 Test All Rounder' )
            plot_player_ranking(test_bat, 'Top 5 Test Batting' )
            plot_player_ranking(test_bowl, 'Top 5 Test Bowling' )
            plot_player_ranking(Wodi_all_round, 'Top 5 WODI All Rounder' )
            plot_player_ranking(Wodi_bat, 'Top 5 WODI Batting')
            plot_player_ranking(Wodi_bowl, 'Top 5 WODI Bowling')
            plot_player_ranking(Wt20_all_rounnd, 'Top 5 Wt20 All Rounder')
            plot_player_ranking(Wt20_bat, 'Top 5 Wt20 Batting' )
            plot_player_ranking(Wt20_bowl, 'Top 5 Wt20 Bowling')
        elif choice==5:
            return False
            
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()