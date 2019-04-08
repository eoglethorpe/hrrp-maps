"""sample exec call"""

import os
from atlas_auto import at

test_list = ([24001, 24002])

# inside palika docker /code/core/resources/mapfiles
mapfiles_path = os.environ.get('MAPFILES_PATH', '.')

x = at(
    data_uri='./data/profile_data_structure_template.xlsx',

    wards_uri=mapfiles_path + '/hrrp_shapes/jsons/merge.json',
    palika_uri=mapfiles_path + '/hrrp_shapes/jsons/GaPaNaPa_hrrp.json',
    dists_uri=mapfiles_path + '/hrrp_shapes/jsons/Districts_hrrp.json',

    dists_syle=mapfiles_path + '/styles/dist_style.qml',
    pka_style=mapfiles_path + '/styles/palika_style.qml',
    atlas_style=mapfiles_path + '/styles/atlas_layout.qpt',
    pka_hide_style=mapfiles_path + '/styles/palika_hide_style.qml',
    ward_style=mapfiles_path + '/styles/ward_style.qml',

    parent_join_cd='N_WCode',
    to_join_code='ward',
    pka_list=test_list,
    img_type='svg',
    out_path='./maps/m/',
)

x.setup()
x.make_maps()
x.exit()
del(x)
