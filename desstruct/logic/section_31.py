def generate_section_31(excel_dict, defaults):
    """
    Generate Section 31 of the DesStruct IN file.
    This section contains wall light panels specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 31 text with wall light panels parameters
    """
    return """*(31)WALL LIGHT PANELS (NO LONGER USED):
* Data     Wall   Panel   Panel   Panel    Panel    Panel  Remove
* Lines     Id    Quan    Type    Color   Length   Offset  Panel
     0""" 