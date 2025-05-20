def generate_section_49(excel_dict, defaults):
    purlin_type = "'ZB'"
    ev_st = "'ZB--'"
    depth = 0
    soffit = "'--'"
    gutter = "'--'"

    return f"""*(49)EXTENSION PURLINS:
*      -------------Purlins-------------  ----------------Girts----------------  --Horizontal--  ---Set_Space---
* Id   Type Ev St   Depth  Soffit  Depth  Top   Inter Bot  Depth   Gutr   Depth  Peak       Set  Top       Inter
   1   {purlin_type} {ev_st}       {depth} {soffit}      {depth}  '--'  '--' '--'      {depth} {gutter}     {depth}       0       0       0        0
   2   {purlin_type} {ev_st}       {depth} {soffit}      {depth}  '--'  '--' '--'      {depth} {gutter}     {depth}       0       0       0        0
   3   {purlin_type} {ev_st}       {depth} {soffit}      {depth}  '--'  '--' '--'      {depth} {gutter}     {depth}       0       0       0        0""" 