bathroom = {
    "name": "",
    "floor":"",
    "traps": "",
    "trap_cost":"",
    "lavatories":"",
    "pedestal":"",
    "clean": {
        "tubshower":"",
        "type":"",
        "brand":"",
        "walls":"",
        "size":"",
        },
    }

labor={
    'tub':{
        # no walls
        'slide-in':15,
        'garden':30,
        'drop-in': 100,
        'freestanding':700,
        # walls
        'ts':{
            'separate walls':30,
            'one-piece':50
        }
    },
    'shower':{
        # no walls no base
        'full tile':100,
        # base only
        'base only':{
            'sterling':15,
            'florestone':20,
            'mustee':20
        },
        # shower unit
        'built in seated':30,
        'shower unit':{
            'separate walls':30,
            'one-piece':50
        }
    }
}

clean = int(input("For tub enter 1\nFor shower enter 2\n"))
walls = input("Will walls be included? Y/N\n").upper()

if clean == 1:
    bathroom["clean"]["tubshower"] = "Tub"
    clean = int(input('What type of of tub will this bathroom get?\n1 - Slide-In\n2 - Garden\n3 - Drop-In\n4 - Freestanding\n'))
    if walls == 'N' and clean == 1:
        bathroom["clean"]["type"] = 'slide-in'
        bathroom['clean']['walls'] = 'tile walls'
    elif walls == 'N' and clean == 2:
        bathroom["clean"]["type"] = 'garden'
        bathroom['clean']['walls'] = 'tile walls'
    elif walls == 'N' and clean == 3:
        bathroom["clean"]["type"] = 'drop-in'
    elif walls == 'N' and clean == 4:
        bathroom["clean"]["type"] = 'freestanding'
    
    if walls == "Y":
        clean = int(input("What type of walled tub unit will this bathroom get"))
        if clean == 1:
            bathroom["clean"]["walls"] = 'separate walls'

        elif clean == 2:
            bathroom["clean"]["walls"] = 'one-piece unit'

elif clean == 2:
    bathroom["clean"]["tubshower"] = "Shower"
    if walls == 'N':
        walls = int(input('1 - Full Tile Shower\n2 - Base w/ Tile Walls\n'))
        if walls == 1:
            bathroom["clean"]["type"] = 'full tile shower'
        elif walls == 2:
            walls = int(input('What brand will the shower base be?\n1 - Sterling\n2 - Florestone or Mustee\n'))
            bathroom['clean']['type'] = 'base w/ tile walls'
            bathroom["clean"]["walls"] = 'tile walls'
            if walls == 1:
                bathroom['clean']['brand'] = 'Sterling'
            elif walls == 2:
                bathroom['clean']['brand'] = 'Florestone or Mustee'


    elif walls == 'Y':
        walls = int(input(f'What type of walls will this {bathroom['clean']['tubshower']} have?\n1 - Separate Walls\n2 - Attached (One Piece)\n'))
        if walls == 1:
            bathroom["clean"]["walls"] = "w/ separate walls"
            
        elif walls == 2:
            bathroom["clean"]["type"] = "one-piece unit"

print(f"Tub/Shower : {bathroom['clean']['tubshower']}")
print(f"Type : {bathroom['clean']['type']}")
print(f"Walls : {bathroom['clean']['walls']}")             
print(f"Brand : {bathroom['clean']['brand']}")        