def generate_section_15(excel_dict, defaults):
    """
    Generate Section 15 of the DesStruct IN file.
    This section contains partial walls specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 15 text with partial walls parameters
    """
    return """*(15)PARTIAL WALLS (NO LONGER USED):
* Wall               Sets    --Bay_Id--   Wall    Base  Full
*  Id   Opt1  Opt2   Bays    Start  End  Height   Type  Load  Opt3
    1   '-'   '-'      0 
    2   '-'   '-'      0 
    3   '-'   '-'      0 
    4   '-'   '-'      0 """ 