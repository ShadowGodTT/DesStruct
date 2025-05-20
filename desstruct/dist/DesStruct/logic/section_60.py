def generate_section_60(excel_dict, defaults):
    girt_locations = [3130, 1500]
    loc = "'I'"
    num_girts = len(girt_locations)
    location_str = " ".join(str(g) for g in girt_locations)

    return f"""*(60)PARTITION WALL GIRT LOCATION:
*Partn  Set   No.    Girt    
*  Id   Loc  Girts   Location
    1   {loc}    {num_girts}       {location_str}""" 