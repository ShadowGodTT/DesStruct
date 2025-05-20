def generate_section_38(excel_dict, defaults):
    """
    Generate Section 38 of the DesStruct IN file.
    This section contains liner panels specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 38 text with liner panels parameters
    """
    return """*(38)LINER PANELS:
*     Loc          -----Location-----  ---------------Panel----------------  Liner_Trim
* No.  Id   Use      Start        End   Part         Thick    Yield   Color  Use  Color   Opt    Height
    0""" 