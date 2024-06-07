import xlsxwriter
import datetime
import math

# todays date
today = datetime.datetime.now().strftime("%B %d, %Y").upper()

def generate_quote(job_info,fixture_info,floors,bath_count,bathrooms):
    # traps
    first_floor_trap = fixture_info['base_trap_price']
    second_floor_trap = first_floor_trap+15
    third_floor_trap = second_floor_trap+5

    # Create workbook and sheet
    # workbook = xlsxwriter.Workbook(fr'/Users/paulwilliams/Work/test_folder/{job_info['builder'].upper()}/QUOTES/{job_info['plan'].upper()}.xlsx')
    workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\Stancil Services\Quan Estimating - Documents\General\{fixture_info['name'].upper()}\QUOTES\{job_info['plan'].upper()}.xlsx')
    # workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\OneDrive - Stancil Services\Documents\Projects\TEST\ESTIMATING\{fixture_info['name'].upper()}\QUOTES\{job_info['plan'].upper()}.xlsx')
    worksheet = workbook.add_worksheet()

    # format worksheet
    worksheet.set_column('A:A',3)
    worksheet.set_column('B:B',5.56)
    worksheet.set_column('C:C',51.36)
    worksheet.set_column('D:D',10)
    worksheet.set_column('E:E',10)

    # cell formats
    bold = workbook.add_format({'bold':True})

    builder_title = workbook.add_format({'bold':True})
    builder_title.set_font_size(20)
    builder_title.set_align('center')

    community_title = workbook.add_format({'bold':True})
    community_title.set_font_size(16)
    community_title.set_align('center')

    project_title = workbook.add_format({'bold':True})
    project_title.set_font_size(14)
    project_title.set_align('center')

    room_title = workbook.add_format({'bold':True})

    color_title = workbook.add_format({'bold':True})
    color_title.set_align('center')

    quantity = workbook.add_format()
    quantity.set_align('center')

    num_format = workbook.add_format()
    num_format.set_num_format('#,##0.00')

    sub_item = workbook.add_format()
    sub_item.set_indent(3)

    tap_depth = workbook.add_format({'bold':True})
    tap_depth.set_indent(6)

    total_price_format = workbook.add_format({'bold':True})
    total_price_format.set_font_size(16)
    total_price_format.set_align('center')

    # builder
    worksheet.write('C1',fixture_info['name'].upper(),builder_title)
    # community
    worksheet.write('C2',job_info['community'].upper(),community_title)
    # project
    worksheet.write('C3',job_info['plan'].upper(),project_title)
    # date
    worksheet.write('B5',today)

    worksheet.write('D5','PRICE')
    worksheet.write('E5','EXTENDED')

    # kitchen
    worksheet.write('B8',f'KITCHEN - {floors[0]['kitchen'].upper()} FLOOR',room_title)
    worksheet.write('C9',f'{fixture_info['fixt_brand'].upper()} {fixture_info['kitchen']['kitchen_coll'].upper()} {fixture_info['kitchen']['kitchen_color'].upper()}',color_title)

    worksheet.write('C10','SINK - BY OTHERS')

    worksheet.write('B11',1,quantity)
    worksheet.write('C11',f'{fixture_info['fixt_brand'].upper()} {fixture_info['kitchen']['kitchen_faucet_mod_num']} 1-HOLE FAUCET')
    worksheet.write('D11',f'=(({fixture_info['kitchen']['kitchen_faucet_price']}*.55)*1.07)/{fixture_info['markup']}',num_format)
    worksheet.write('E11','=B11*D11',num_format)

    worksheet.write('B12',1,quantity)
    worksheet.write('C12',fixture_info['kitchen']['garbage_disposal'])
    worksheet.write('D12',f'=(({fixture_info['kitchen']['garbage_disposal_price']}*1.07)/.65)+25',num_format)
    worksheet.write('E12','=B12*D12',num_format)

    worksheet.write('B13',1,quantity)
    worksheet.write('C13','DISHWASHER INSTALLATION')
    worksheet.write('D13',150,num_format)
    worksheet.write('E13','=B13*D13',num_format)

    worksheet.write('B14',1,quantity)
    worksheet.write('C14','ICE MAKER BOX FOR REFRIGERATOR')
    worksheet.write('D14',100,num_format)
    worksheet.write('E14','=B14*D14',num_format)

    worksheet.write('B15',1,quantity)
    worksheet.write('C15','TRAP')

    if floors[0]['kitchen'] == 'FIRST':
        worksheet.write('D15',first_floor_trap,num_format)
    elif floors[0]['kitchen'] == 'SECOND':
        worksheet.write('D15',second_floor_trap,num_format)
    else:
        worksheet.write('D15',third_floor_trap,num_format)
    worksheet.write('E15','=B15*D15',num_format)

    # bathrooms
    line = 18
    for i in range(bath_count):
        # bathroom naming convention
        worksheet.write(f'B{line}',f'{bathrooms[i]['name'].upper()} - {bathrooms[i]['floor'].upper()} FLOOR',room_title)
        line +=1
        worksheet.write(f'C{line}',f'{fixture_info['fixt_brand'].upper()} {fixture_info['bath']['bath_coll'].upper()} {fixture_info['house_color'].upper()}',color_title)
        line +=1

        # toilet
        worksheet.write(f'B{line}',1,quantity)
        worksheet.write(f'C{line}',f'{fixture_info['bath']['closet']['closet'].upper()} WHITE CLOSET')
        worksheet.write(f'D{line}',f'=((({fixture_info['bath']['closet']['closet_bowl_cost']}+{fixture_info['bath']['closet']['closet_tank_cost']})*1.04)*1.07)/{fixture_info['markup']}',num_format)
        worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
        line +=1

        # bowl
        worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['closet']['closet_bowl']}',sub_item)
        line +=1

        # tank
        worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['closet']['closet_tank']}',sub_item)
        line +=1

        # toilet seat
        worksheet.write(f'B{line}',1,quantity)
        worksheet.write(f'C{line}',f'{fixture_info['bath']['closet']['closet_seat']}')
        worksheet.write(f'D{line}',f'=(({fixture_info['bath']['closet']['closet_seat_cost']}*1.04)*1.07)/{fixture_info['markup']}',num_format)
        worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
        line +=1

        if bathrooms[i]["traps"] >= 3:
            # lavatory(ies)
            # if two lavatories
            if bathrooms[i]['lavatories'] == 2:
                worksheet.write(f'C{line}',f'TWO LAVATORIES - BY OTHERS')
                line +=1
                # double lavatory faucets
                worksheet.write(f'B{line}',bathrooms[i]['lavatories'],quantity)
                worksheet.write(f'C{line}',f'TWO {fixture_info['fixt_brand'].upper()} {fixture_info['bath']['lavatory']['lav_faucet_mod_num']} FAUCETS')
                worksheet.write(f'D{line}',f'=(({fixture_info['bath']['lavatory']['lav_faucet_price']}*.55)*1.07)/{fixture_info['markup']}',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
            else:
                worksheet.write(f'C{line}',f'LAVATORY - BY OTHERS')
                line +=1
                # single lavatory faucet
                worksheet.write(f'B{line}',bathrooms[i]['lavatories'],quantity)
                worksheet.write(f'C{line}',f'{fixture_info['fixt_brand'].upper()} {fixture_info['bath']['lavatory']['lav_faucet_mod_num']} FAUCET')
                worksheet.write(f'D{line}',f'=(({fixture_info['bath']['lavatory']['lav_faucet_price']}*.55)*1.07)/{fixture_info['markup']}',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1

            

        # shower
        if bathrooms[i]['clean']['tubshower'] == 'Shower':
            # shower units
            if bathrooms[i]['clean']['walls'] == 'w/ separate walls':
                # separate walls
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {fixture_info['bath']['shower']['shower_coll'].upper()} {fixture_info['bath']['shower']['shower_base']}/{fixture_info['bath']['shower']['shower_back_wall']}/{fixture_info['bath']['shower']['shower_end_wall']}')
                worksheet.write(f'D{line}',f'=(((({fixture_info['bath']['shower']['shower_base_cost']}+{fixture_info['bath']['shower']['shower_back_wall_cost']}+{fixture_info['bath']['shower']['shower_end_wall_cost']})*1.04)*1.07)/{fixture_info['markup']})+30',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
                worksheet.write(f'C{line}',f'{bathrooms[i]['clean']['size']} WHITE SHOWER UNIT',sub_item)
                line +=1

            elif bathrooms[i]['clean']['walls'] == 'one-piece unit':
                # one piece
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {fixture_info['bath']['shower']['shower_base']} {bathrooms[i]['clean']['size']} WHITE SHOWER UNIT')
                worksheet.write(f'D{line}',f'=((({fixture_info['bath']['shower']['shower_base_cost']}*1.04)*1.07)/{fixture_info['markup']})+50',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1

            elif bathrooms[i]['clean']['walls'] == 'w/ seat and separate walls':
                # separate walls w/ seat
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {fixture_info['bath']['shower']['shower_coll'].upper()} {fixture_info['bath']['shower']['shower_base']}/{fixture_info['bath']['shower']['shower_wall_set']}')
                worksheet.write(f'D{line}',f'=(((({fixture_info['bath']['shower']['shower_base_cost']}+{fixture_info['bath']['shower']['shower_wall_set_cost']})*1.04)*1.07)/{fixture_info['markup']})+30',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
                worksheet.write(f'C{line}',f'{bathrooms[i]['clean']['size']} WHITE SHOWER UNIT W/ SEAT',sub_item)
                line +=1

            elif bathrooms[i]['clean']['walls'] == 'shower base w/ tile walls':
                # shower base only
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {fixture_info['bath']['shower']['shower_coll'].upper()} {fixture_info['bath']['shower']['shower_base']} {bathrooms[i]['clean']['size']} WHITE SHOWER BASE ONLY')
                worksheet.write(f'D{line}',f'=((({fixture_info['bath']['shower']['shower_base_cost']}*1.04)*1.07)/{fixture_info['markup']})+15',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1

            elif bathrooms[i]['clean']['walls'] == 'tile walls':
                # tile shower
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'TILE SHOWER - BY OTHERS')
                worksheet.write(f'D{line}',100,num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1

            # shower valve and trim
            worksheet.write(f'B{line}',1,quantity)
            worksheet.write(f'C{line}',f'{fixture_info['fixt_brand'].upper()} SHOWER VALVE AND TRIM')
            worksheet.write(f'D{line}',f'=((({fixture_info['bath']['shower']['shower_valve_price']}+{fixture_info['bath']['shower']['shower_trim_cost']})*.55)*1.07)/{fixture_info['markup']}',num_format)
            worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
            line +=1

            # valve
            worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['shower']['shower_valve']} ROUGH SHOWER VALVE',sub_item)
            line +=1

            # trim
            worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['shower']['shower_trim_mod_num']} SHOWER TRIM',sub_item)
            line +=1
            
        # tub and shower
        elif bathrooms[i]['clean']['tubshower'] == 'Tub':
            if bathrooms[i]['clean']['walls'] == 'tub only':
                # tub only
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {bathrooms[i]['clean']['size']} WHITE SLIDE-IN TUB ONLY')
                worksheet.write(f'D{line}',1,num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
                

            elif bathrooms[i]['clean']['walls'] == 'w/ separate walls':
                # tub and shower w/ walls
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {fixture_info['bath']['ts']['ts_coll'].upper()} {fixture_info['bath']['ts']['tub']}-0/{fixture_info['bath']['ts']['tub_walls']}')
                worksheet.write(f'D{line}',f'=(((({fixture_info['bath']['ts']['tub_cost']}+{fixture_info['bath']['ts']['tub_walls_cost']})*1.04)*1.07)/{fixture_info['markup']})+30',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
                worksheet.write(f'C{line}',f'WHITE T&S UNIT',sub_item)
                line +=1

            elif bathrooms[i]['clean']['walls'] == 'one-piece unit':
                # one piece
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['brand'].upper()} {fixture_info['bath']['ts']['tub']} WHITE ONE PIECE T/S UNIT')
                worksheet.write(f'D{line}',f'=((({fixture_info['bath']['ts']['tub_cost']}*1.04)*1.07)/{fixture_info['markup']})+50',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1

            # tub and shower valve and trim
            worksheet.write(f'B{line}',1,quantity)
            worksheet.write(f'C{line}',f'{fixture_info['fixt_brand'].upper()} T&S VALVE AND TRIM')
            worksheet.write(f'D{line}',f'=((({fixture_info['bath']['ts']['ts_valve_price']}+{fixture_info['bath']['ts']['ts_trim_cost']})*.55)*1.07)/{fixture_info['markup']}',num_format)
            worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
            line +=1

            # valve
            worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['ts']['ts_valve']} ROUGH TUB AND SHOWER VALVE',sub_item)
            line+=1

            # trim
            worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['ts']['ts_trim_mod_num']} T&S TRIM',sub_item)
            line +=1   

        # colored shower strainer / waste and overflow
        if fixture_info['house_color'] != 'Chrome' :
            if bathrooms[i]['clean']['tubshower'] == 'Shower':
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['strainer_overflow_color'].upper()} SHOWER STRAINER')
                worksheet.write(f'D{line}',f'=({fixture_info['bath']['strainer_overflow_price']}*1.07)/.6',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
            else:
                worksheet.write(f'B{line}',1,quantity)
                worksheet.write(f'C{line}',f'{fixture_info['bath']['strainer_overflow_color'].upper()} WASTE AND OVERFLOW')
                worksheet.write(f'D{line}',f'=({fixture_info['bath']['strainer_overflow_price']}*1.07)/.6',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1

        if bathrooms[i]['name'].upper() == 'POWDER ROOM':
            # lavatory
            # if pedestal
            if bathrooms[i]['pedestal'] == "Y":
                worksheet.write(f'B{line}',bathrooms[i]['lavatories'],quantity)
                worksheet.write(f'C{line}',f'LAVATORY - {fixture_info['bath']['lavatory']['pedestal_lav'].upper()} PEDESTAL')
                worksheet.write(f'D{line}',f'=(((({fixture_info['bath']['lavatory']['ped_lav_bowl_cost']}+{fixture_info['bath']['lavatory']['ped_lav_leg_cost']})*1.04)*1.07)/{fixture_info['markup']})+25',num_format)
                worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
                line +=1
                # bowl
                worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['lavatory']['ped_lav_bowl'].upper()}',sub_item)
                line+=1
                # leg
                worksheet.write(f'C{line}',f'(1) {fixture_info['bath']['lavatory']['ped_lav_leg'].upper()}',sub_item)
                line+=1
            else:
                worksheet.write(f'C{line}',f'LAVATORY - BY OTHERS (PLAN SHOWS CABINET)')
                line +=1

            # faucet
            worksheet.write(f'B{line}',bathrooms[i]['lavatories'],quantity)
            worksheet.write(f'C{line}',f'{fixture_info['fixt_brand'].upper()} {fixture_info['bath']['lavatory']['lav_faucet_mod_num']} FAUCET')
            worksheet.write(f'D{line}',f'=(({fixture_info['bath']['lavatory']['lav_faucet_price']}*.55)*1.07)/{fixture_info['markup']}',num_format)
            worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
            line +=1

        # traps
        worksheet.write(f'B{line}',bathrooms[i]['traps'],quantity)
        worksheet.write(f'C{line}','TRAPS')
        worksheet.write(f'D{line}',bathrooms[i]['trap_cost'],num_format)
        worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
        line+=3

    # laundry room
    worksheet.write(f'B{line}',f'LAUNDRY ROOM - {floors[1]['laundry']} FLOOR',room_title)
    line +=1
    worksheet.write(f'B{line}',1,quantity)
    worksheet.write(f'C{line}','WASHER BOX')
    worksheet.write(f'D{line}',75,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line +=1
    worksheet.write(f'B{line}',1,quantity)
    worksheet.write(f'C{line}','TRAP')
    if floors[1]['laundry'] == 'FIRST':
        worksheet.write(f'D{line}',first_floor_trap,num_format)
    elif floors[1]['laundry'] == 'SECOND':
        worksheet.write(f'D{line}',second_floor_trap,num_format)
    else:
        worksheet.write(f'D{line}',third_floor_trap,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=3

    # behind the walls
    worksheet.write(f'C{line}','REHAU PEX WATER SYSTEM WITH PEX STUB OUTS')
    line+=3
    worksheet.write(f'C{line}','PVC DRAIN AND VENT SYSTEM')
    line+=3

    # water heater
    worksheet.write(f'B{line}',1,quantity)
    # if
    worksheet.write(f'C{line}',fixture_info['other']['water_heater'])
    worksheet.write(f'D{line}',f'=(({fixture_info['other']['water_heater_cost']}*1.07)/.6)+{fixture_info['other']['water_heater_labor']}',num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=1
    worksheet.write(f'C{line}',f'LOCATED IN {fixture_info['other']['water_heater_location'].upper()}',sub_item)
    line+=3

    # water heater stand/pan
    # if located in the garage
    if floors[2]['water_heater'] == "Y":
        worksheet.write(f'B{line}',1,quantity)
        worksheet.write(f'C{line}','WATER HEATER STAND')
        worksheet.write(f'D{line}',100,num_format)
        worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
        line+=3
    else:
        worksheet.write(f'B{line}',1,quantity)
        worksheet.write(f'C{line}','WATER HEATER PAN WITH DRAIN')
        worksheet.write(f'D{line}',185,num_format)
        worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
        line+=3

    # water heater stand
    worksheet.write(f'B{line}',1,quantity)
    worksheet.write(f'C{line}','EXPANSION TANK')
    worksheet.write(f'D{line}',85,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=3

    # expansion tank
    worksheet.write(f'B{line}',1,quantity)
    worksheet.write(f'C{line}','3/4" PRESSURE REGULATOR VALVE')
    worksheet.write(f'D{line}',85,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=3

    # hose bibbs
    worksheet.write(f'B{line}',2,quantity)
    worksheet.write(f'C{line}','TWO HOSE BIBBS WITH QUICK FLASHING')
    worksheet.write(f'D{line}',95,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=3

    # sewer line
    worksheet.write(f'B{line}',fixture_info['other']['sewer_line'],quantity)
    worksheet.write(f'C{line}',f'SEWER LINE INSTALLATION - {fixture_info['other']['sewer_line']} FT')
    worksheet.write(f'D{line}',12,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=1
    worksheet.write(f'C{line}',f'EXCESS TO BE BILLED AT $15.00 PER FT',sub_item)
    line+=1
    worksheet.write(f'C{line}','TAP DEPTH NOT TO EXCEED 5 FT',tap_depth)
    line+=3

    # water line
    worksheet.write(f'B{line}',fixture_info['other']['water_line'],quantity)
    worksheet.write(f'C{line}',f'WATER LINE INSTALLATION - {fixture_info['other']['water_line']} FT')
    worksheet.write(f'D{line}',8,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=1
    worksheet.write(f'C{line}','EXCESS TO BE BILLED AT $10.00 PER FT',sub_item)
    line+=3

    # toilet camera lines
    worksheet.write(f'B{line}',bath_count,quantity)
    worksheet.write(f'C{line}','CAMERA TOILET LINES AT TRIM')
    worksheet.write(f'D{line}',50,num_format)
    worksheet.write(f'E{line}',f'=B{line}*D{line}',num_format)
    line+=4

    # total price
    worksheet.write(f'C{line}',f'QUAN TOTAL PRICE : $10,000.00',total_price_format)
    worksheet.write(f'E{line}',f'=SUM(E10:E{line-1})',num_format)
    line+=3

    # extras
    worksheet.write(f'C{line}','EXTRAS',color_title)
    line+=1
    # water
    worksheet.write(f'C{line}','IF WATER IS NOT AVAILABLE FOR SLAB OR ROUGH TESTING:')
    line+=1
    worksheet.write(f'C{line}','ADD $250.00 EACH',sub_item)
    line+=2

    # backwater valve
    worksheet.write(f'C{line}','BACKWATER VALVE IF REQUIRED:')
    line+=1
    worksheet.write(f'C{line}','ADD $675.00',sub_item)

    workbook.close()


 