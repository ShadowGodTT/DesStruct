def generate_section_32(excel_dict, defaults):
    """
    Generate Section 32 of the DesStruct IN file.
    This section contains roof light panels specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 32 text with roof light panels parameters
    """
    return """*(32)ROOF LIGHT PANELS (NO LONGER USED):
* No.      Surf   Panel   Panel   Panel    Panel    Panel  Remove
* Panels    Id    Quan    Type    Color   Length   Offset  Panel
     0""" 