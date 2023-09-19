# Given a dictionary of:
provinsi = {'Nanggroe Aceh Darussalam': 'Aceh',
            'Sumatera Selatan': 'Palembang',
            'Kalimantan Barat': 'Pontianak',
            'Jawa Timur': 'Madiun',
            'Sulawesi Selatan': 'Makassar',
            'Maluku': 'Ambon'}

#  What python command can be use to:
#  a.Get list of keys available in dictionary
# b.Change 'Jawa Timur' value from 'Madiun'  to 'Surabaya'

#a
print(provinsi.keys())

#b
provinsi["Jawa Timur"]="Surabaya"
print(provinsi)