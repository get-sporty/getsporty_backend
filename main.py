import requests, flask

#get GeoJSON data from brimbank
DATASETS = [('Brimbank Parks','http://data.gov.au/geoserver/playground/wfs?request=GetFeature&typeName=ckan_e8d3580c_3981_47ab_a675_573805c3fa86&outputFormat=json'),
            ('Ballarat Indoor','http://data.gov.au/geoserver/ballarat-indoor-recreation-facilities/wfs?request=GetFeature&typeName=9006b1fc_9a36_425d_ae2a_6307c37c99c9&outputFormat=json'),
            ]

if __name__ == '__main__':
    print get_datasets()