bathroom = {
    "name": "",
    "floor":"",
    "traps": "",
    "trap_cost":"",
    "lavatories":"",
    "pedestal":"",
    "clean": {
        "tubshower":"",
        "unit":"",
        "size":""
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
    if walls == 'N':
        clean = int(input('What type of of tub will this bathroom get?\n1 - Slide-In\n2 - Garden\n3 - Drop-In\n4 - Freestanding\n'))

        if clean == 1:
            bathroom["clean"]["type"] = 'slide-in'
        elif clean == 2:
            bathroom["clean"]["type"] = 'garden'
        elif clean == 3:
            bathroom["clean"]["type"] = 'drop-in'
        elif clean == 4:
            bathroom["clean"]["type"] = 'freestanding'

    elif walls == "Y":
        clean = int(input("What type of walled tub unit will this bathroom get"))
        if clean == 1:
            bathroom["clean"]["walls"] = 'separate walls'
        elif clean == 2:
            bathroom["clean"]["walls"] = 'one-piece unit'

elif clean == 2:
    bathroom["clean"]["tubshower"] = "Shower"
    clean = int(input())
    if walls == 'N':
        walls = int(input('1 - Full Tile Shower\n2 - Base w/ Tile Walls\n'))
        if walls == 1:
            bathroom["clean"]["type"] =
        elif walls == 2:
            if walls = int(input('1 - Sterling\n2 - Florestone or Mustee\n'))
            bathroom["clean"]["type"] =

    elif walls == 'Y':

        

    elif walls == 'Y':

elif bathroom['clean']['tubshower'] == "Shower":
    # no walls no base

    # base only
        # sterling
        # florestone / mustee
    # shower unit
        # separate walls
        # one-piece unit
        # built in seat

# if bathroom['clean']['tubshower'] == "Tub":
#     if walls == "Y":
#         if wall_type == 1:
#             bathroom["clean"]["walls"] = "w/ separate walls"
#         elif wall_type == 2:
#             bathroom["clean"]["walls"] = "one-piece unit"
#         elif wall_type == 3:
#             bathroom["clean"]["walls"] = "w/ seat and separate walls"
#     elif walls == "N":
#         if wall_type == 1:
#             bathroom["clean"]["walls"] = "shower base w/ tile walls"
#         elif wall_type == 2:
#             bathroom["clean"]["walls"] = "tile walls"
# elif bathroom['clean']['tubshower'] == "Shower":
#     if walls == "Y":
#         if wall_type == 1:
#             bathroom["clean"]["walls"] = "w/ separate walls"
#         elif wall_type == 2:
#             bathroom["clean"]["walls"] = "one-piece unit"
#     elif walls == "N":