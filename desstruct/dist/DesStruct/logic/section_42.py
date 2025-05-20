def generate_section_42(excel_dict, defaults):
    """
    Generate Section 42 of the DesStruct IN file.
    This section contains crane specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 42 text with crane parameters
    """
    return """*(42)CRANES:
*No.  Frame  Crane Col ------Loads------  --Beam %_Force--  Wheel --------Location---------
*Cran Id Bay Type  Sup  Cap  Brg    Ht    DL    Long  Lat   Base  Elev   XL     Span   XR
    0""" 