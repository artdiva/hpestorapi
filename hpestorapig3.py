import xml.etree.ElementTree
import hpestorapi

with hpestorapi.StoreOnceG3('10.0.0.1', 'Admin', 'password') as so:
    try:
        so.open()
    except Exception as error:
        print('Something went wrong:')
        print(error)
    else:
        status, data = so.get('/cluster')
        if status == 200:
            tree = xml.etree.ElementTree.fromstring(data)
            name = tree.find('./cluster/properties/applianceName').text
            model = tree.find('./cluster/properties/productClass').text
            print(f'SO Name = "{name}"')
            print(f'SO Model = "{model}"')