def generate_section_36(excel_dict, defaults):
    """
    Generate Section 36 of the DesStruct IN file.
    This section contains wall liner panels specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 36 text with wall liner panels parameters
    """
    return """*(36)WALL LINER PANELS (NO LONGER USED):
* Wall   Use   ----Location----            --------------Panel--------------  Liner_Trim
*  Id   Liner    Start      End   Height   Part        Thick   Yield   Color  Use  Color
    1    'N'
    2    'N'
    3    'N'
    4    'N'""" 