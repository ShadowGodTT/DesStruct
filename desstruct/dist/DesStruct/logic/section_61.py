def generate_section_61(excel_dict, defaults):
    height = 3050
    part_name = "'45250 .5'"
    color = "'A2--'"
    screw = "'M--'"
    corner = "'HA--'"
    jamb = "'HA--'"
    top = "'HA--'"
    base = "'HA--'"

    return f"""*(61)PARTITION WALL LEFT SIDE OF WALL DATA:
*Partn --Top_Wall---  --------Panel-------- Screw  -----------Trim_Color---------
* Id   Height  Panel  Part_Name      Color  Type   Corner   Jamb    Top     Base 
    1   {height}  {part_name}  {color}  {screw}   {corner}   {jamb}   {top}   {base}""" 