aliens = [
    {
        'color':'green',
        'speed':'fast'
    }, 
]

print(aliens[0]['color'])

aliens[0]['points'] = 25
print(aliens[0])

for k, v in aliens[0].items():
    print("\nKey: " + str(k))
    print("Value: " + str(v))

for k in aliens[0]:
    print("\nKey: " + str(k))