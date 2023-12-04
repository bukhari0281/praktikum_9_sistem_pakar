fakta = {
    'A': True,
    'B': True,
    'C': True,
    'D': True,
    'E': True,
    'X': False,
    'L': False,
    'Y': False,
    'Z': False,
    'M': False,
    'N': False,
}

rule = {
    'R1': False,
    'R2': False,
    'R3': False,
    'R4': False,
    'R5': False,
}

rules_fired = []
i = 0
perubahan = True

while perubahan == True :
    perubahan = False
    i+= i
    print('iterasi ke', i)
    
#rule 1
if rule ['R1'] is False :
    if fakta ['Y'] is True and fakta ['D'] is True :
        fakta ['Z'] = True
        perubahan = True
        rules_fired.append('R1')
        rule ['R1'] = True
print ('Rule ke-1 :', rule ['R1'])
    print(rules_fired)

print ("Kesimpulan Z :", fakta ['Z'])
