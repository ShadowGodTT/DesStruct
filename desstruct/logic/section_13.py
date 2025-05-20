def generate_section_13(excel_dict, defaults):
    """
    Generate Section 13 of the DesStruct IN file.
    This section contains wall openings specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 13 text with wall openings parameters
    """
    # Hardcoded based on the Desctrl3.In sample, as Excel doesn't provide door/window layout
    return """*(13)WALL OPENINGS:
* Wall   No.   Bay                                       Sill      Base  Panel
*  Id   Open   Id     Width   Height   Offset   Type   Height      Elev   Opt
    1     0 
    2     2     2      6100     6100      965     51        0         0   'Y'
                5      6100     6100      965     51        0         0   'Y'
    3     1     2      6100     6100      685     51        0         0   'Y'
    4     0 """ 