def generate_section_41(excel_dict, defaults):
    """
    Generate Section 41 of the DesStruct IN file.
    This section contains longitudinal partition wall data specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 41 text with longitudinal partition wall data parameters
    """
    return """*(41)LONGITUDINAL PARTITION WALL DATA (NO LONGER USED):
*No.   Wall -----------Panel-----------  -----Insulation-----  Screw  --Trim--
*Walls No.  Side Type  Thk  Yield Color  Use Type  Thick Wire  Type   Top  End
    0""" 