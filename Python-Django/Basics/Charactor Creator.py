def start():
    print('Starfinder Simple Character Builder')
    race_list_full = {'android' : ['4' , 'Construct' , '+2 Dex, +2 Int, -2 Cha'] , 'human' : ['4' , 'Skilled' , '+2 to any'] , 'kasatha' : ['4' , 'Four-Armed' , '+2 Str, +2 Wis, -2 Int'] , 'lashunta' : ['4' , 'Limited Telepathy' , 'Dimorphic'] , 'shirren' : ['6' , 'Communalism' , '+2 Con, +2 Wis, -2 Cha'] , 'vesk' : ['6' , 'Natural Weapons' , '+2 Str, +2 Con, -2 Int'] , 'ysoki' : ['2' , 'Cheek Pouches' , '+2 Dex, +2 Int, -2 Str']}
    race_list_short = ["Android", "Human", "Kasatha", "Lashunta", "Shirren", "Vesk", "Ysoki"]
    print('To create your character, start by selecting your race:')
    print(race_list_short)
    Race = input('Enter a race: ').lower()
    print('You typed in the race ' + Race.capitalize())
    try:
        Race_Data = race_list_full[Race]
        print('Name: ' + Race.capitalize())
        print('Base Hit Points: ' + Race_Data[0])
        print('Trait: ' + Race_Data[1])
        print('Ablility Modifier: ' + Race_Data[2])
        srace()
    except:
        print('The race (as written) was not found.')
        start()
def srace():
    Selection = input('Is this your race?')
    if Selection == 'No':
        start()
    if Selection == 'Yes':
        theme()
    else:
        print('Please enter Yes or No.')
        srace()
def theme():
    theme_list_full = {'ace pilot' : ['Dexterity' , 'Pilot'] , 'bounty hunter' : ['Intelligence' , 'Survival'] , 'icon' : ['Charisma' , 'Culture'] , 'mercenary' : ['Strength' , 'Athletics'] , 'outlaw' : ['Dexterity' , 'Slight of Hand'] , 'priest' : ['Wisdome' , 'Mysticism'] , 'scholar' : ['Intelligence' , 'Life or Physical Scineces'] , 'spacefarer' : ['Constitution' , 'Physical Science'] , 'xenoseeker' : ['Charisma' , 'Life Science']}
    theme_list_short = ["Ace Pilot", "Bounty Hunter", "Icon", "Mercenary", "Outlaw", "Priest", "Scholar", "Spacefarer", "Xenoseeker"]
    print(theme_list_short)
    print('Next, what is your theme?')
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
    Selection = input('Is this your theme?')
    if Selection == 'No':
        theme()
    if Selection == 'Yes':
        class_sel()
    else:
        print("Please enter Yes or No.")
        stheme()
def class_sel():
    class_list_full = {'envoy' : ['6' , 'Improvisation' , 'Charisma'] , 'mechanic' : ['6' , 'Custom Rig & A.I.' , 'Intelligence'] , 'mystic' : ['6' , 'Connection' , 'Wisdom'] , 'operative' : ['6' , 'Specialization' , 'Dexterity'] , 'solarian' : ['7' , 'Solar Manifestation' , 'Charisma'] , 'soldier' : ['7' , 'Fighting Style' , 'Str or Dex'] , 'technomancer' : ['5' , 'Spell Cache' , 'Intelligence']}
    class_list_short = ["Envoy", "Mechanic", "Mystic" , "Operative" , "Solarian", "Soldier", "Technomancer"]
    print(class_list_short)
    print('Finally, what is your class?')
    Class = input('Enter your class: ').lower()
    print('You typed in the class ' + Class.capitalize())
    try:
        Class_Data = class_list_full[Class]
        print('Name: ' + Class.capitalize())
        print('Hit Points: ' + Class_Data[0])
        print('Feature: ' + Class_Data[1])
        print('Key Ability: ' + Class_Data[2])
        sclass()
    except:
        print('The class (as written) was not found.')
def sclass():
    Selection = input('Is this your class?')
    if Selection == 'No':
        class_sel()
    if Selection == 'Yes':
        you_are()
    else:
        print('Please enter Yes or No.')
        sclass()
def input():
    class_list_full = {'envoy' : ['6' , 'Improvisation' , 'Charisma'] , 'mechanic' : ['6' , 'Custom Rig & A.I.' , 'Intelligence'] , 'mystic' : ['6' , 'Connection' , 'Wisdom'] , 'operative' : ['6' , 'Specialization' , 'Dexterity'] , 'solarian' : ['7' , 'Solar Manifestation' , 'Charisma'] , 'soldier' : ['7' , 'Fighting Style' , 'Str or Dex'] , 'technomancer' : ['5' , 'Spell Cache' , 'Intelligence']}
    class_list_short = ["Envoy", "Mechanic", "Mystic" , "Operative" , "Solarian", "Soldier", "Technomancer"]
    race_list_full = {'android' : ['4' , 'Construct' , '+2 Dex, +2 Int, -2 Cha'] , 'human' : ['4' , 'Skilled' , '+2 to any'] , 'kasatha' : ['4' , 'Four-Armed' , '+2 Str, +2 Wis, -2 Int'] , 'lashunta' : ['4' , 'Limited Telepathy' , 'Dimorphic'] , 'shirren' : ['6' , 'Communalism' , '+2 Con, +2 Wis, -2 Cha'] , 'vesk' : ['6' , 'Natural Weapons' , '+2 Str, +2 Con, -2 Int'] , 'ysoki' : ['2' , 'Cheek Pouches' , '+2 Dex, +2 Int, -2 Str']}
    race_list_short = ["Android", "Human", "Kasatha", "Lashunta", "Shirren", "Vesk", "Ysoki"]
    theme_list_full = {'ace pilot' : ['Dexterity' , 'Pilot'] , 'bounty hunter' : ['Intelligence' , 'Survival'] , 'icon' : ['Charisma' , 'Culture'] , 'mercenary' : ['Strength' , 'Athletics'] , 'outlaw' : ['Dexterity' , 'Slight of Hand'] , 'priest' : ['Wisdome' , 'Mysticism'] , 'scholar' : ['Intelligence' , 'Life or Physical Scineces'] , 'spacefarer' : ['Constitution' , 'Physical Science'] , 'xenoseeker' : ['Charisma' , 'Life Science']}
    theme_list_short = ["Ace Pilot", "Bounty Hunter", "Icon", "Mercenary", "Outlaw", "Priest", "Scholar", "Spacefarer", "Xenoseeker"]
    print('You are a ')
    print([Race]).join
    print([Theme]).join
    print([Class]).join
start()
