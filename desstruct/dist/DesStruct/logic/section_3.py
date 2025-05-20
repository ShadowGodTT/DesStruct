def generate_section_3(excel_dict, defaults):
    """
    Generate Section 3 of the DesStruct IN file.
    This section contains roof options and configurations.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 3 text with roof options
    """
    # Get roof sheeting, bracing, and purlins information
    roof_sheeting = excel_dict.get("Roof sheeting", "").strip().lower()
    bracing = excel_dict.get("Roof bracing type", "").strip().lower()
    purlins = excel_dict.get("Purlins", "").strip().lower()

    # Determine panel, brace, and purlin options
    panel = "'YY'" if roof_sheeting else "'N'"
    brace = "'YY'" if "rod" in bracing else "'N'"
    purl = "'YY'" if purlins else "'N'"

    # Default values
    detail = "'YY'"
    angle = "'YY'"

    # Format roof options section
    output = [
        "*( 3)ROOF OPTIONS:",
        "* Detail   Use     Use     Use     Use",
        "*  Roof    Purl   Panel   Brace   Angle",
        f"   {detail}     {purl}   {panel}    {brace}    {angle}"
    ]
    
    return "\n".join(output) 