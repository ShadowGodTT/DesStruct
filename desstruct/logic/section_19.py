def generate_section_19(excel_dict, defaults):
    """
    Generate Section 19 of the DesStruct IN file.
    This section contains roof purlins specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 19 text with roof purlins parameters
    """
    purlin_type = "'ZBZBZB'"
    flange_brace = "'Y'"
    supply = "'Y'"
    offset = 0
    project = 0
    depth = 0
    lap = 0

    output = [
        "*(19)ROOF PURLINS:",
        "* Surf  Purlin      Flange_Brace                     Set     Set",
        "*  Id Type/EaveF/B   Use  Supply  Offset  Project   Depth    Lap"
    ]
    for surf_id in [2, 3]:
        output.append(
            f"     {surf_id}  {purlin_type}     {flange_brace}    {supply}        {offset}        {project}        {depth}        {lap}"
        )
    return "\n".join(output) 