def generate_section_37(excel_dict, defaults):
    """
    Generate Section 37 of the DesStruct IN file.
    This section contains fascia specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 37 text with fascia parameters
    """
    return """*(37)FACIA (NO LONGER USED):
* Wall   Use   ----Location---  Bottom                         --Cover---
*  Id   Facia    Start     End   Elev   Height  Offset  Slope  Panel Trim
    1    'N'
    2    'N'
    3    'N'
    4    'N'""" 