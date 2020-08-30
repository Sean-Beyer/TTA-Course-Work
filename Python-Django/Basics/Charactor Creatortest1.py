def start():
    theme_list_full = {'ace pilot' : ['Dexterity' , 'Pilot'] , 'bounty hunter' : ['Intelligence' , 'Survival'] , 'icon' : ['Charisma' , 'Culture'] , 'mercenary' : ['Strength' , 'Athletics'] , 'outlaw' : ['Dexterity' , 'Slight of Hand'] , 'priest' : ['Wisdome' , 'Mysticism'] , 'scholar' : ['Intelligence' , 'Life or Physical Scineces'] , 'spacefarer' : ['Constitution' , 'Physical Science'] , 'xenoseeker' : ['Charisma' , 'Life Science']}
    theme_list_short = ["Ace Pilot", "Bounty Hunter", "Icon", "Mercenary", "Outlaw", "Priest", "Scholar", "Spacefarer", "Xenoseeker"]
    print('Next, what is your theme?')
    print(theme_list_short)
    Theme = input('Enter a theme: ').lower()
    print('You typed in the theme ' + Theme.capitalize())
    try:
        Theme_Data = theme_list_full[Theme]
        print('Name: ' + Theme.capitalize())
        print('Ability Bonus: ' + Theme_Data[0])
        print('Class Skill: ' + Theme_Data[1])
        stheme()
    except:
        print('The theme (as written) was not found.')
        theme()
def stheme():
    Selection = input('Is this your them?')
    if Selection == 'No':
        start()
    if Selection == 'Yes':
        class_sel()
    else:
        print("Please enter Yes or No.")
        stheme()

start()
