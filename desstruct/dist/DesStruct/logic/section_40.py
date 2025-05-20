def generate_section_40(excel_dict, defaults):
    """
    Generate Section 40 of the DesStruct IN file.
    This section contains longitudinal partition wall location specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 40 text with longitudinal partition wall location parameters
    """
    return """*(40)LONGITUDINAL PARTITION WALL LOCATION (NO LONGER USED):
* No.  Wall  -B_SW-  -L_EW Offset--  -Top_Of_Wall-
*Walls No.   Offset   Start     End  Height  Panel
    0""" 