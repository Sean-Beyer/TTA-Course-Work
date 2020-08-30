

mySentance = 'loves the color'

color_list = ['red','blue','cyan','limegreen','black','white']

def color_function(name):
    lst = []
    for i in color_list:
        msg = '{0} {1} {2}'.format(name,mySentance,i)
        lst.append(msg)
        return lst


lst = (color_function('SEAN'))
for i in lst:
    print(i)
