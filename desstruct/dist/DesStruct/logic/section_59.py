def generate_section_59(excel_dict, defaults):
    girt_type = excel_dict.get("Partition Wall Girt Type", "'ZB'")
    use = "'Y'"
    supply = "'Y'"
    depth = 200
    top_type = girt_type

    return f"""*(59)PARTITION WALL GIRTS:
*Partn  Girt  Flange_Brace   Set    Top_Girt
*  Id   Type   Use  Supply   Depth    Type  
    1   {girt_type}   {use}  {supply}   {depth}    {top_type}""" 