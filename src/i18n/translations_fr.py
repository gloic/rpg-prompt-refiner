def trad_gender(input):
    table = {
        'Male': 'masculin',
        'Female': 'féminin',
        'Either': 'masculin et féminin',
        'Neither': 'aucun genre',
    }
    return table.get(input, input)


def trad_species(input):
    table = {
        'Elf': 'Elf',
        'Human': 'Humain',
        'Beast': 'Bête',
        'Khajiit': 'Khajiit',
        'Ayleid': 'Ayleid',
        'Argonian': 'Argonien',
        'Daedric': 'Daedra',
        'Dragon': 'Dragon',
        'Radiant': 'Radiant'
    }
    return table.get(input, input)


def trad_race(input):
    table = {
        'Dunmer': 'Dunmer',
        'Nord': 'Nordique',
        'Beast': 'Bête',
        'Breton': 'Bréton',
        'Khajiit': 'Khajiit',
        'Altmer': 'Altmer',
        'Redguard': 'Rougegarde',
        'Bosmer': 'Bosmer',
        'Ayleid': 'Ayleid',
        'Imperial': 'Impérial',
        'Spriggan': 'Spriggan',
        'Argonian': 'Argonien',
        'Elder': 'Elder',
        'Orsimer': 'Orc',
        'Radiant': 'Radiant',
        'Dremora': 'Drémora',
        'Skeleton': 'Squelette',
        'Snow Elf': 'Falmer',
        'Daedric': 'Daedra',
        'Khajiit-Orc': 'Orc Khajiit',
        'Demon': 'Démon',
        'Reachman': 'Crevassais',
        'Dragon': 'Dragon',
        'Canine': 'Chien',
        'Daedra': 'Daedra',
        'Hagraven': 'Harfreuse',
        'Akaviri': 'Akaviri',
        'Ningheim': 'Ningheim'
    }
    return table.get(input, input)
