import xlsxwriter

from base_options import builders
from excel_quote_generator import generate_quote
from materials_list_generator import generate_materials_list

# roundup in python
# need to calculate the cost of the home outside of excel so I can input the value on the quote
# math.ceil()

# project info
floors=[
    {'kitchen':''},
    {'laundry':''},
    {'water_heater':''}
]
bathrooms = []
strainer_overflow = [
    {'Brushed Gold':25},
    {'Matte Black':24},
    {'Brushed Nickel':21.5},
]
fixture_info = {
    'name':'',
    'fixt_brand':'',
    'markup':.7,
    'base_trap_price':480,
    'house_color':'',
    'kitchen':{
        'kitchen_coll':'',
        'kitchen_color':'',
        'kitchen_faucet_mod_num':'67315SRS',
        'kitchen_faucet_price':399.05,
        'garbage_disposal':'GX PRO 1/3 DISPOSAL WITH CORD - GXP33C',
        'garbage_disposal_price':126.4,

    },
    'bath':{
        'bath_coll':'',
        'brand':'',
        'closet':{
            'closet':'KHOLER HIGHLINE WHITE CLOSET',
            'closet_bowl':'K-5297-0 WHITE ELONGATED COMFORT HEIGHT BOWL',
            'closet_bowl_cost':132.5,
            'closet_tank':'K-5308-0 WHITE TANK',
            'closet_tank_cost':78.75,
            'closet_seat':'MAINLINE ML170000 WHITE ELONGATED CLOSET SEAT',
            'closet_seat_cost':15.23,
        },
        'lavatory':{
            'pedestal_lav':'Gerber Maxwell G002514',
            'ped_lav_bowl':'12-514 4" CC Bowl',
            'ped_lav_bowl_cost':75.39,
            'ped_lav_leg':'29-842 Pedestal Leg',
            'ped_lav_leg_cost':28.63,
            'lav_faucet_mod_num':'L64601 4" CC',
            'lav_faucet_price':217.05,
        },
        'shower':{
            'shower_coll':'',
            'shower_base':'72331100-0',
            'shower_base_cost':244.51,
            'shower_back_wall':'72432100-0',
            'shower_back_wall_cost':238.72,
            'shower_end_wall':'72405100-0',
            'shower_end_wall_cost':141.77,

            'shower_valve':'FP62325PF',
            'shower_valve_price':161.3,
            'shower_trim_mod_num':'TL182',
            'shower_trim_cost':50.05,
        },
        'ts':{
            'ts_coll':'',
            'tub':'71171112 OR 22',
            'tub_cost':226.52,
            'tub_walls':'71374100',
            'tub_walls_cost':243.29,

            'ts_valve':'FP62380PF',
            'ts_valve_price':168.65,
            'ts_trim_mod_num':'TL183',
            'ts_trim_cost':81.25
        },
        'strainer_overflow_color':'',
        'strainer_overflow_price':'',
    },
    'other':{
        'water_heater':'STATE EN650DORT 50-GALLON ELECTRIC WATER HEATER',
        'water_heater_cost':425,
        'water_heater_labor':100,
        'water_heater_location':'',
        'sewer_line':30,
        'water_line':30
    },
}


def general_info():
    global fixture_info
    print('Which builder is this estimate for?')
    for i, sublist in enumerate(builders):
        print(f'{i} - {builders[i]['name']}')
    print(f'{len(builders)} - Other Builder')
    builder_choice = int(input())
    global community
    community = input("What is the name of this community?\n").upper()
    global project_name
    project_name = input("What is the name of the project?\n").upper()
    global bath_count
    bath_count = int(input("How many bathrooms are in this home?\n"))
    # if Other Builder
    if builder_choice == len(builders):
        brands = ['Moen','Delta']
        j=1
        print('What brand will the fixtures in this house be?')
        for i in brands:
            print(f'{j} - {i}')
            j+=1
        brand = int(input())
        fixture_info['fixt_brand'] = brands[brand-1]
        colors=["Chrome","Brushed Nickel / Stainless","Matte Black","Brushed Gold"]
        j=1
        print('What color are the fixtures in this home?')
        for i in colors:
            print(f'{j} - {i}')
            j+=1
        color = int(input())
        fixture_info['house_color'] = colors[color-1]
        if fixture_info['house_color'] == 'Brushed Nickel / Stainless': 
            if fixture_info['fixt_brand'] == 'Delta':  
                fixture_info['kitchen']['kitchen_color'] = "Artic Stainless"
                fixture_info['house_color'] = 'Stainless'
            elif fixture_info['fixt_brand'] == 'Moen':
                fixture_info['kitchen']['kitchen_color'] = "Spot Resist Stainless"
                fixture_info['house_color'] = 'Brushed Nickel'
        else:
            fixture_info['kitchen']['ktichen_color'] = fixture_info['house_color']
        
        if fixture_info['house_color'].upper() == "BRUSHED NICKEL / STAINLESS":
            fixture_info['bath']['strainer_overflow_color'] = 'Brushed Nickel'
            fixture_info['bath']['strainer_overflow_price'] = strainer_overflow[2]['Brushed Nickel']
        elif fixture_info['house_color'].upper() == "MATTE BLACK":
            fixture_info['bath']['strainer_overflow'] = strainer_overflow[1]['Matte Black']
        elif fixture_info['house_color'].upper() == "BRUSHED GOLD":
            fixture_info['bath']['strainer_overflow'] = strainer_overflow[0]['Brushed Gold']

    # known builder
    else:
        fixture_info = builders[builder_choice]
        standard_opt = input('Will this builder be using their base package? Y/N\n')
        # if builder that we already know their standard package
        if standard_opt.upper() == "Y":
            fixture_info=builders[builder_choice]
        # need to build logic for options
        else:
            fixture_info['kitchen']['kitchen_coll']= input('What collection will be in the kitchen?\n')
            # bathroom fixture collection
            fixture_info['bath']['bath_coll']=input('What collection will be in the bathrooms?\n')

    floors[0]['kitchen'] = input('What floor is the kitchen on?\n').upper()
    floors[1]['laundry'] = input('What floor is the laundry room on?\n').upper()
    floors[2]['water_heater'] = input('Will the water heater be in the garage? Y/N\n').upper()
    if floors[2]['water_heater'] == 'Y':
        fixture_info['other']['water_heater_location'] = 'GARAGE'
    else:
        fixture_info['other']['water_heater_location'] = input('Where is the water heater located?\n')

first_floor_trap = fixture_info['base_trap_price']
second_floor_trap = first_floor_trap+15
third_floor_trap = second_floor_trap+5

def bath_info(baths,fixture_info):
    for i in range(bath_count):
        bathroom = {
        "name": "",
        "floor":"",
        "traps": "",
        "trap_cost":"",
        "lavatories":"",
        "pedestal":"",
        "clean": {
            "tubshower":"",
            "size":"",
            "walls":""
            },
        }

        bathroom["name"] = input("What is the name of this bathroom?\n")
        bathroom["floor"] = input('What floor is this bathroom on?\n')
        if bathroom['name'].upper() == 'POWDER ROOM':
            bathroom['pedestal'] = input("Will the lavatory be a pedestal sink? Y/N\n").upper()
            bathroom["traps"]=2
            bathroom["lavatories"]=1

        else:
            bathroom["traps"]=int(input("How many traps are in this bathroom?\n"))
            bathroom["lavatories"]=int(input("How many lavatories are in this bathroom?\n"))
            clean = int(input("For tub enter 1\nFor shower enter 2\n"))
            if clean == 1:
                bathroom["clean"]["tubshower"] = "Tub"
            elif clean == 2:
                bathroom["clean"]["tubshower"] = "Shower"
            bathroom["clean"]['size'] = input(f'What size is the {bathroom["clean"]["tubshower"].lower()}?\n')
            walls = input("Will walls be included? Y/N\n").upper()
            if walls == "Y":
                wall_type = int(input(f'What type of walls will this {bathroom['clean']['tubshower']} have?\n1 - Separate Walls\n2 - Attached (One Piece)\n3 - Separate Walls w/ Seat\n'))
            elif walls == "N":
                wall_type = int(input(f'What type of walls will this {bathroom['clean']['tubshower']} have?\n1 - Shower Base w/ Tile Walls\n2 - Full Tile Shower\n'))

            if bathroom['clean']['tubshower'] == "Shower":
                if walls == "Y":
                    if wall_type == 1:
                        bathroom["clean"]["walls"] = "w/ separate walls"
                    elif wall_type == 2:
                        bathroom["clean"]["walls"] = "one-piece unit"
                    elif wall_type == 3:
                        bathroom["clean"]["walls"] = "w/ seat and separate walls"
                elif walls == "N":
                    if wall_type == 1:
                        bathroom["clean"]["walls"] = "shower base w/ tile walls"
                    elif wall_type == 2:
                        bathroom["clean"]["walls"] = "tile walls"
            elif bathroom['clean']['tubshower'] == "Tub":
                if walls == "Y":
                    if wall_type == 1:
                        bathroom["clean"]["walls"] = "w/ separate walls"
                    elif wall_type == 2:
                        bathroom["clean"]["walls"] = "one-piece unit"
                elif walls == 'N':
                    bathroom['clean']['walls'] = 'tile walls'

        if bathroom['floor'].upper() == "FIRST":
            bathroom['trap_cost'] = fixture_info['base_trap_price']
        elif bathroom['floor'].upper() == "SECOND":
            bathroom['trap_cost'] = fixture_info['base_trap_price']+15
        else:
            bathroom['trap_cost'] = fixture_info['base_trap_price']+20

        bathrooms.append(bathroom)




# builder = input('What is the name of this builder?')
# community = input('What is the name of this community?')
# plan = input('What is the name of this plan?')



general_info()
bath_info(bath_count,fixture_info)
job_info = {
    'community':community,
    'plan':project_name,
}

generate_quote(job_info,fixture_info,floors,bath_count,bathrooms)
# generate_materials_list(job_info)
