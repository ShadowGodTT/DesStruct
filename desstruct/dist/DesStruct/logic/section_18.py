def generate_section_18(excel_dict, defaults):
    """
    Generate Section 18 of the DesStruct IN file.
    This section contains wall girt location specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 18 text with wall girt location parameters
    """
    # Girt locations assumed constant for now, can be parameterized per wall
    low_girt = 0
    loc = "'I'"
    num_girts = 2
    girt_locations = [3130, 1500]  # mm, example values

    output = [
        "*(18)WALL GIRT LOCATION:",
        "* Wall    Low    Set   No.    Girt",
        "*  Id     Girt   Loc  Girts   Location"
    ]
    for wall_id in range(1, 5):
        girt_str = "  ".join([f"{loc_val}" for loc_val in girt_locations])
        output.append(
            f"    {wall_id}         {low_girt}  {loc}    {num_girts}       {girt_str} "
        )
    
    return "\n".join(output) 