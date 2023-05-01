from constants import PLAYERS as players, TEAMS as teams
from statistics import mean

# Below are two links which I used for help to convert a list of values to a dictionary, and how to organize dictionaries by value for the two exceeds expectations criteria, the organization of the players by height and the saving to data structures respectively, which I found to be the most challenging tasks:

# This is the link that I used for help with organizing the players by height: https://careerkarma.com/blog/python-sort-a-dictionary-by-value/.

# I learned how to convert a list of values to a dictionary to incorporate teams stats into dictionaries for each of the three respective teams here: https://careerkarma.com/blog/python-convert-list-to-dictionary/.

if __name__ == "__main__":
    def clean_data(players):
        cleaned = []
        for player in players:
            fixed = {}
            fixed['name'] = player['name']
            fixed['height'] = player['height'].split(" inches")[0]
            fixed['experience'] = player['experience']
            fixed['guardian'] = ", ".join(player['guardians'].split(" and "))

            if player['experience'] == 'YES':
                fixed['experience'] = True
            else: 
                fixed['experience'] = False
                
            cleaned.append(fixed)
        
        return cleaned
    
    players_cleaned_data = clean_data(players)
    
    def height(player):
        return player['height']
    
    def menu():
        print("BASKETBALL TEAM STATS TOOL")
        print('\n---- MENU ---- ')
        print('\nHere are your choices:')
        print('\nA: Display Team Stats')
        print('B: Quit')
        
        option_input = input('\nEnter an option: ')
        
        while option_input.lower() != 'a' and option_input.lower() != 'b':
            option_input = input("Sorry, I don't understand. Please type 'a' or 'b'. ")
            
        if option_input.lower() == 'a':
            print(f'\nA) {teams[0]}')
            print(f'B) {teams[1]}')
            print(f'C) {teams[2]}')
            
            option_input_2 = input('\nEnter an option: ')
            
            while option_input_2.lower() != 'a' and option_input_2.lower() != 'b' and option_input_2.lower() != 'c':
                option_input_2 = input("Sorry, I don't understand. Please type 'a', 'b' or 'c'. ")
            
            def return_menu():
                enter_input = input("\nPlease type 'e' to continue. ")
                
                while enter_input.lower() != 'e':
                    enter_input = input("Sorry, I don't understand. Please type 'e' to continue. ")
                
                if enter_input.lower() == 'e':
                    menu()
    
            def balance_teams():
                if option_input_2.lower() == 'a':
                    print(f'\n{teams[0]} Stats')
                    print('-------------------')
                    
                    p_names = []
                    p_experienced = []
                    p_inexperienced = []
                    p_heights = []
                    p_guardians = []
                    
                    for p in range(0, 3):
                        players_cleaned_data[p]['team'] = teams[0]
                                            
                        if players_cleaned_data[p]['experience'] == True:
                            p_experienced.append(players_cleaned_data[p]['experience'])
                        elif players_cleaned_data[p]['experience'] == False:
                            p_inexperienced.append(players_cleaned_data[p]['experience'])
                        
                        p_height = int(players_cleaned_data[p]['height'])
                        p_heights.append(p_height)
                        
                        p_name = str(players_cleaned_data[p]['name'])
                        p_names.append(p_name)
                                      
                        p_guardian = str(players_cleaned_data[p]['guardian'])
                        p_guardians.append(p_guardian)
                        
                    for p in range(9, 12):
                        players_cleaned_data[p]['team'] = teams[0]
                                            
                        if players_cleaned_data[p]['experience'] == True:
                            p_experienced.append(players_cleaned_data[p]['experience'])
                        elif players_cleaned_data[p]['experience'] == False:
                            p_inexperienced.append(players_cleaned_data[p]['experience'])
                        
                        p_height = int(players_cleaned_data[p]['height'])
                        p_heights.append(p_height)
                        
                        p_name = str(players_cleaned_data[p]['name'])
                        p_names.append(p_name)
                                      
                        p_guardian = str(players_cleaned_data[p]['guardian'])
                        p_guardians.append(p_guardian)
                    
                    p_name_keys = p_names
                    p_name_values = p_heights
                    p_name_team = dict(zip(p_name_keys, p_name_values))
                    
                    p_names_team = sorted(p_name_team.items(), key=lambda x:x[1])
                    p_new_names = []
                    
                    for name in p_names_team:
                        p_new_names.append(str(name[0]))
                    
                    print(f'Total players: {(len(players_cleaned_data[0:3]) + len(players_cleaned_data[9:12]))}')
                    print(f'Total experienced: {len(p_experienced)}')
                    print(f'Total inexperienced: {len(p_inexperienced)}')
                    print(f'Average height: {mean(p_heights)}')
                    
                    print('\nPlayers on Team (from shortest to tallest):')
                    print(", ".join(p_new_names))
                    
                    print('\nGuardians:')
                    print(", ".join(p_guardians))
                    
                    p_keys = ['name', 'players', 'experienced', 'inexperienced', 'average_height']
                    p_values = [teams[0], p_names, len(p_experienced), len(p_inexperienced), mean(p_heights)]
                    p_team = dict(zip(p_keys, p_values))
                    
                    return_menu()                
    
                elif option_input_2.lower() == 'b':
                    print(f'\n{teams[1]} Stats')
                    print('-------------------')
                    
                    b_names = []
                    b_experienced = []
                    b_inexperienced = []
                    b_heights = []
                    b_guardians = []
                    
                    for b in range(3, 9):
                        players_cleaned_data[b]['team'] = teams[1]
                        
                        if players_cleaned_data[b]['experience'] == True:
                            b_experienced.append(players_cleaned_data[b]['experience'])
                        else:
                            b_inexperienced.append(players_cleaned_data[b]['experience'])
                        
                        b_height = int(players_cleaned_data[b]['height'])
                        b_heights.append(b_height)
                               
                        b_name = str(players_cleaned_data[b]['name'])
                        b_names.append(b_name)
                        
                        b_guardian = str(players_cleaned_data[b]['guardian'])
                        b_guardians.append(b_guardian)
                    
                    b_name_keys = b_names
                    b_name_values = b_heights
                    b_name_team = dict(zip(b_name_keys, b_name_values))
                    
                    b_names_team = sorted(b_name_team.items(), key=lambda x:x[1])
                    b_new_names = []
                    for name in b_names_team:
                        b_new_names.append(str(name[0]))
                        
                    print(f'Total players: {len(players_cleaned_data[3:9])}')
                    print(f'Total experienced: {len(b_experienced)}')
                    print(f'Total inexperienced: {len(b_inexperienced)}')
                    print(f'Average height: {mean(b_heights)}')
                    
                    print('\nPlayers on Team (from shortest to tallest):')
                    print(", ".join(b_new_names))
                    
                    print('\nGuardians:')
                    print(", ".join(b_guardians))
                    
                    b_keys = ['name', 'players', 'experienced', 'inexperienced', 'average_height']
                    b_values = [teams[1], b_names, len(b_experienced), len(b_inexperienced), mean(b_heights)]
                    b_team = dict(zip(b_keys, b_values))
                    
                    return_menu()
            
                elif option_input_2.lower() == 'c':
                    print(f'\n{teams[2]} Stats')
                    print('-------------------')
                    
                    w_names = []
                    w_experienced = []
                    w_inexperienced = []
                    w_heights = []
                    w_guardians = []
                    
                    for w in range(12, len(players_cleaned_data)):
                        players_cleaned_data[w]['team'] = teams[2]
                        
                        if players_cleaned_data[w]['experience'] == True:
                            w_experienced.append(players_cleaned_data[w]['experience'])
                        else:
                            w_inexperienced.append(players_cleaned_data[w]['experience'])
                        
                        w_height = int(players_cleaned_data[w]['height'])
                        w_heights.append(w_height)
                        
                        w_name = str(players_cleaned_data[w]['name'])
                        w_names.append(w_name)
                        
                        w_guardian = str(players_cleaned_data[w]['guardian'])
                        w_guardians.append(w_guardian)
                    
                    w_name_keys = w_names
                    w_name_values = w_heights
                    w_name_team = dict(zip(w_name_keys, w_name_values))
                    
                    w_names_team = sorted(w_name_team.items(), key=lambda x:x[1])
                    w_new_names = []
                    for name in w_names_team:
                        w_new_names.append(str(name[0]))
    
                    print(f'Total players: {len(players_cleaned_data[12:len(players_cleaned_data)])}')
                    print(f'Total experienced: {len(w_experienced)}')
                    print(f'Total inexperienced: {len(w_inexperienced)}')
                    print(f'Average height: {mean(w_heights)}')
                    
                    print('\nPlayers on Team (from shortest to tallest):')
                    print(", ".join(w_new_names))
                    
                    print('\nGuardians:')
                    print(", ".join(w_guardians))
                    
                    w_keys = ['name', 'players', 'experienced', 'inexperienced', 'average_height']
                    w_values = [teams[2], w_names, len(w_experienced), len(w_inexperienced), mean(w_heights)]
                    w_team = dict(zip(w_keys, w_values))
                    
                    return_menu()
            
            balance_teams()
        
        elif option_input.lower() == 'b':
            print('Thanks for stopping by. See you soon!')
            
    menu()    
#    print(teams)