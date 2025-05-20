def generate_section_11(excel_dict, defaults):
    """
    Generate Section 11 of the DesStruct IN file.
    This section contains surface shape specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 11 text with surface shape parameters
    """
    return """*(11)SURFACE SHAPE:
*   No.
*   Surf   X_Coord   Y_Coord
    0""" 