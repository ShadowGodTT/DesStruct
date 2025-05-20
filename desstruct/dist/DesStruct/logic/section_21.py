def generate_section_21(excel_dict, defaults):
    """
    Generate Section 21 of the DesStruct IN file.
    This section contains wall panel data specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 21 text with wall panel data parameters
    """
    part = "'45250 .5'"
    thickness = "0.50"
    color = "'A2--'"
    trim = "'HA--'"
    screw_type = "'M--'"
    ins_use = "'N'"
    ins_type = "'--'"
    ins_thick = "0.00"
    wire = "'N'"
    thermal = "0.0000"
    panel_rot = "'-'"

    output = [
        "*(21)WALL PANEL DATA:",
        "*                   Wall       ---Trim_Color---    Screw   -------Insulation-----  Thermal  Panel",
        "* Part        Thk   Color    Eave  Corner   Jamb    Type   Use Type   Thick  Wire   Block    Rot"
    ]
    for _ in range(4):
        output.append(
            f"  {part}   {thickness}  {color}  {trim} {trim}  {trim}  {screw_type}  {ins_use} {ins_type}    {ins_thick}   {wire}    {thermal}   {panel_rot}"
        )
    return "\n".join(output) 