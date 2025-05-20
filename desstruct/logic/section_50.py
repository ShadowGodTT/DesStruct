def generate_section_50(excel_dict, defaults):
    roof_part = "'45250 .5'"
    color = "'A3--'"
    screw = "'M--'"
    soffit_part = "'--------'"
    soffit_color = "'----'"
    rotate = "'N'"
    spacing = 0
    clip = 0

    return f"""*(50)EXTENSION PANELS, HORIZONTAL:
* ------------------Roof---Standing_Seam--  --------------Soffit--------------  Screw
* Id   Part       Color   Use  Type   Clip  Part       Color   Rotate  Spacing   Type
   1  {roof_part} {color}   'N'  '--'  {clip} {soffit_part} {soffit_color}   {rotate}        {spacing}  {screw}
   2  {roof_part} {color}   'N'  '--'  {clip} {soffit_part} {soffit_color}   {rotate}        {spacing}  {screw}
   3  {roof_part} {color}   'N'  '--'  {clip} {soffit_part} {soffit_color}   {rotate}        {spacing}  {screw}""" 