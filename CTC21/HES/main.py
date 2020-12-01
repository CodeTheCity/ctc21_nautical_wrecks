import shapefile as shp
import OSGridConverter as OSGC
import csv
from canmore_classes import Shipwreck


complete_list = []
valid_grid_ref = ['HO','HP','HT','HU','HW','HX','HY','HZ','NA','NB','NC','ND','NE','NF','NG','NH','NJ','NK','NL','NM',
                  'NN','NO','NP','NR','NS','NT','NU','NW','NX','NY','NZ','OV','SC','SD','SE','SH','SJ','SK','SM','SN',
                  'SO','SP','SR','SS','ST','SU','SV','SW','SX','SY','SZ','TA','TF','TG','TL','TM','TQ','TR','TV']


def main():
    with open('councils.csv', mode='r') as raw_input:
        reader = csv.reader(raw_input)
        council_dict = {rows[1]: rows[0] for rows in reader}
        del council_dict["item"]

    with open('short_types.csv', mode='r') as raw_input:
        reader = csv.reader(raw_input)
        type_dict = {rows[1]: rows[0] for rows in reader}
        del type_dict["item"]

    with shp.Reader("Canmore_Points/Canmore_Maritime") as sf:
        records = sf.shapeRecords()

    for rec in records:
        if rec.record[12][:2] in valid_grid_ref:
            rec_class = generate_class(rec, council_dict, type_dict)
            complete_list.append(rec_class)

    with open('output.txt', mode="w") as output_text:
        for rec_class in complete_list:
            output_text.write(rec_class.create_string()+"\n")

    """for rec in records:
        can_id = rec.record[14].split('/')[-2]
        if can_id == "292341":
            print_record(rec, council_dict, type_dict)"""


def generate_class(rec, council_dict, type_dict):
    name = tidy_string(rec.record[2].split(":")[0])
    ship_type = get_type_Q(rec.record[5], type_dict)
    council = council_dict[tidy_string(rec.record[7])]
    gr = rec.record[12]
    latlong = convert_coords(gr)
    loc = f"@{latlong.latitude}/{latlong.longitude}"
    can_id = rec.record[14].split('/')[-2]
    my_class = Shipwreck(name, ship_type, council, loc, can_id)
    return my_class


def convert_coords(gr):
    latlong = OSGC.grid2latlong(gr)
    return latlong


def tidy_string(str_val):
    str_val = str_val.lower()
    str_val = str_val.capitalize()
    return str_val


def get_type_Q(raw_type, type_dict):
    ship_type = tidy_string(raw_type.split(",")[0].split("[")[0].split("(")[0].strip())
    if ship_type in type_dict:
        return type_dict[ship_type]
    else:
        return "Q11446"


def print_record(rec, council_dict, type_dict):
    name = tidy_string(rec.record[2].split(":")[0])
    ship_type = get_type_Q(rec.record[5], type_dict)
    council = council_dict[tidy_string(rec.record[7])]
    gr = rec.record[12]
    latlong = convert_coords(gr)
    loc = f"@{latlong.latitude}/{latlong.longitude}"
    can_id = rec.record[14].split('/')[-2]
    my_class = Shipwreck(name, ship_type, council, loc, can_id)
    print(my_class.create_string())


if __name__ == '__main__':
    main()


""" Temporary script to find missing ship types
type_set = set()

    for rec in records:
        ship_type = tidy_string(rec.record[5].split(",")[0].split("[")[0].split("(")[0].strip())
        type_set.add(ship_type)

    with open('ship_types.csv', mode='r', encoding="utf-8") as raw_input:
        reader = csv.reader(raw_input)
        types_dict = {rows[1].lower(): rows[0] for rows in reader}
        del types_dict["itemlabel"]

    temp_set = set()
    temp_type_dict = {}

    for s_type in type_set:
        if s_type.lower() not in types_dict:
            temp_set.add(s_type)
        else:
            temp_type_dict[s_type] = types_dict[s_type.lower()]

    with open('types.txt', 'w') as opened_file:
        for s_type in temp_set:
            opened_file.write(str(s_type)+"\n")

    with open('types2.txt', 'w') as opened_file:
        for s_type in temp_type_dict:
            opened_file.write(str(s_type)+"\n")
"""