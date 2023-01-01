#extract details from <dl class="dl-horizontal other-ads">
from asyncio.windows_events import NULL


def extract_details(info_container):
    """extract details from listing detail view (milage,transmission, fuel_type, body_style, engine_size, doors, location, warraty"""
    key = []
    value = []
    for i in info_container.find_all('dt'):
        i = i.text.strip('\n')
        key.append(i)
#print(atributes, len(atributes))
    for i in info_container.find_all('dd'):
        i = i.text.strip()
        value.append(i)
#print(atributes_values, len(atributes_values))

    attribute_dict = dict(zip(key,value))

    try:
        milage = int(attribute_dict['Mileage'].split(' ')[0])
    except:
        milage = NULL

    try:
        transmission = attribute_dict['Transmission']
    except:
        transmission = ''
    
    try:
        fuel_type = attribute_dict['Fuel Type']
    except:
        fuel_type = ''

    try:
        body_style = attribute_dict['Body Style']
    except:
        body_style = ''

    try:
        engine_size = float(attribute_dict['Engine Size'].split(' ')[0])
    except:
        engine_size = NULL

    try:
        doors = float(attribute_dict['Doors'].split(' ')[0])
    except:
        doors = NULL
    
    try:
        location = attribute_dict['Location']
    except:
        location =''

    try:
        warranty = attribute_dict['Warranty']
    except:
        warranty = ''

    clean_info = {
        'milage': milage,
        'transmission' : transmission,
        'fuel_type' : fuel_type,
        'body_style': body_style,
        'engine_size' : engine_size,
        'doors' : doors,
        'location': location.capitalize(),
        'warranty' : warranty
    }


    return clean_info


#clean title 

def clean_title(title):
    t = title.text
    t = t.strip()
    te = t.split(' ')
    title = te[2:]
    clean_title = " ".join(title)
    return clean_title

def get_year(title):
    t = title.text
    t = t. strip().split(' ')
    year = t[1]
    try:
        year = int(year)
    except:
        try:
            year = int(t[0])
        except:
            year = ''
    
    return year