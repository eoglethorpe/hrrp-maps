"""sample exec call"""

from hrrpmaps.atlas_auto import at

test_list = ([24001,
                24002])

x = at(
    data_uri='./data/profile_data_structure_template.xlsx',
    wards_uri='./hrrp_shapes/jsons/merge.json',
    palika_uri='./hrrp_shapes/jsons/GaPaNaPa_hrrp.json',
    dists_uri='./hrrp_shapes/jsons/Districts_hrrp.json',
    dists_syle='./styles/dist_style.qml',
    pka_style='./styles/palika_style.qml',
    atlas_style='./styles/atlas_layout.qpt',
    pka_hide_style='./styles/palika_hide_style.qml',
    ward_style='./styles/ward_style.qml',
    parent_join_cd='N_WCode',
    to_join_code='ward',
    pka_list=test_list,
    img_type = 'svg',
    out_path = './maps/m/')

x.setup()
x.make_maps()
x.exit()
del(x)