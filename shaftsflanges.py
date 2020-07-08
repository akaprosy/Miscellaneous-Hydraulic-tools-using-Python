sae_keyed_shaft = {'AA': {
    'shaft_diam': 0.500,
    'short_shaft_length':0.750,
    'long_shaft_length': 'none',
    'key_width': 0.125,
    },
    'A': {
    'shaft_diam': 0.625,
    'short_shaft_length': .938,
    'long_shaft_length': 2.000,
    'key_width': 0.125,

    },
    'B': {
    'shaft_diam': 0.875,
    'short_shaft_length': 1.312,
    'long_shaft_length': 2.500,
    'key_width': 0.250,
    },
    'BB': {
    'shaft_diam': 1.000,
    'short_shaft_length': 1.500,
    'long_shaft_length': 2.750,
    'key_width': 0.250,
    },
    'C': {
    'shaft_diam': 1.250,
    'short_shaft_length': 1.875,
    'long_shaft_length': 3.000,
    'key_width': 0.312,   
    },
    'CC': {
    'shaft_diam': 1.500,
    'short_shaft_length': 2.125,
    'long_shaft_length': 3.250,
    'key_width': 0.753,
    },
    'D': {
    'shaft_diam': 1.750,
    'short_shaft_length': 2.625,
    'long_shaft_length': 3.625,
    'key_width': 0.437,
    },
    'E': {
    'shaft_diam': 1.750,
    'short_shaft_length': 2.625,
    'long_shaft_length': 3.625,
    'key_width': 0.437,
    },
    

}

for sae_code, specs in sae_keyed_shaft.items():
    print(f'\nSAE Shaft Code: {sae_code}')
    shaft_diam = specs['shaft_diam']
    print(f'\tShaft Diameter: {shaft_diam}')
    short_length = specs['short_shaft_length']
    print(f'\tShort Shaft Length: {short_length}')
    long_length = specs['long_shaft_length']
    print(f'\tLong Shaft Length: {long_length}')
    keyed_width = specs['key_width']
    print(f'\tKeyed Width: {keyed_width}')
