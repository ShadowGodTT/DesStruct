def generate_section_2(excel_dict, defaults):
    """
    Generate Section 2 of the DesStruct IN file.
    This section contains wall options and configurations.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 2 text with wall options
    """
    # Get wall sheeting and bracing information
    wall_sheeting = excel_dict.get("Wall sheeting", "").strip().lower()
    bracing = excel_dict.get("Wall bracing type", "").strip().lower()

    # Determine panel and brace options
    panel = "'YY'" if wall_sheeting else "'N'"
    brace = "'YY'" if "rod" in bracing else "'N'"

    # Default values
    detail = "'YY'"
    girt = "'YY'"
    trim = "'Y'"

    # Format wall options section
    output = [
        "*( 2)WALL OPTIONS:",
        "* Wall   Detail   Use     Use     Use    Use",
        "*  Id     Wall    Girt   Panel   Brace   Trim"
    ]
    
    # Add options for each wall
    for wall_id in [1, 2, 3, 4]:
        output.append(f"    {wall_id}     {detail}    {girt}   {panel}    {brace}    {trim}")
    
    return "\n".join(output) 