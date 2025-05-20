def generate_section_79(excel_dict, defaults):
    height_top = 3050
    walls = [1, 2, 3, 4]
    output = [
        "*(79)PARTIAL WALL LAYOUT:",
        "*        Wall      --Bay_Id--  ----Offset----  -----Height-----   --Attach_Type--  ---Jamb--    Full  Deflect_Limit",
        "* No. Id  Id  Use  Start  End   Start     End   Bottom      Top   Bottom      Top  Type  Opt    Load   Girt   Panel"
    ]
    for i, wall_id in enumerate(walls, start=1):
        output.append(
            f"  {i}   {wall_id}   {wall_id}  'PO'   1     4        0       0        0     {height_top}   '-:---' '-:1--'  '-'   '-'    'NY'     90      0"
        )
    return "\n".join(output) 