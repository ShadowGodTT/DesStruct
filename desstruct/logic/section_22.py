def generate_section_22(excel_dict, defaults):
    """
    Generate Section 22 of the DesStruct IN file.
    This section contains roof panel data specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 22 text with roof panel data parameters
    """
    part = "'45250 .5'"
    thickness = "0.50"
    color = "'A3--'"
    gable_color = "'HA--'"
    screw_type = "'M--'"
    ins_use = "'N'"
    ins_type = "'--'"
    ins_thick = "0.00"
    wire = "'N'"
    standing_seam_use = "'N'"
    seam_type = "'--'"
    clip = "0.00"
    seam = "'---------------'"
    clamp = "'N'"
    thermal = "0.0000"

    return f"""*(22)ROOF PANEL DATA:
*                   Roof     Gable  Screw  -----Insulation-----  -------------Standing_Seam-------------
* Part        Thk   Color    Color  Type   Use Type  Thick Wire  Use  Type  Clip   Seam Type       Clamp  Thermal_Block
  {part}  {thickness}  {color}   {gable_color} {screw_type}  {ins_use} {ins_type}   {ins_thick}  {wire}  {standing_seam_use}  {seam_type}  {clip}  {seam} {clamp}    {thermal}""" 