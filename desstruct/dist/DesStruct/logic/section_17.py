def generate_section_17(excel_dict, defaults):
    """
    Generate Section 17 of the DesStruct IN file.
    This section contains wall girts specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 17 text with wall girts parameters
    """
    # Defaults for all walls (assumed same unless specified)
    girt_type = "'ZB'"
    flange_brace = "'Y'"
    supply = "'Y'"
    offset = 0
    project = 230
    set_depth = [200, 0, 0, 0]  # Example: first wall has 200, rest 0 — adjust if needed
    lap = 0

    output = [
        "*(17)WALL GIRTS:",
        "* Wall  Girt  Flange_Brace                      Set      Set",
        "*  Id   Type   Use  Supply   Offset   Project   Depth    Lap"
    ]
    for wall_id in range(1, 5):
        depth = set_depth[wall_id - 1] if wall_id - 1 < len(set_depth) else 0
        output.append(
            f"    {wall_id}   {girt_type}   {flange_brace}    {supply}         {offset}      {project}      {depth}        {lap}"
        )
    
    return "\n".join(output) 