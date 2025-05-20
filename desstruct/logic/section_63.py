def generate_section_63(excel_dict, defaults):
    use = "'N'"
    ins_type = "'--'"
    thick = "0.00"
    wire = "'N'"
    angle = "'Y'"
    channel = "'N'"
    seal = "'NHA--'"
    angle_seal = "'N'"

    return f"""*(63)PARTITION WALL ACCESSORIES:
* --------Insulation--------    -----------Base_Options------------
*Partn                          Base     Base     Base     Base    
* Id    Use Type  Thick Wire    Angle   Channel   Seal   Angle/Seal
    1    {use} {ins_type}  {thick} {wire}    {angle}   {channel}   {seal}   {angle_seal}""" 