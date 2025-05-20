def generate_section_14(excel_dict, defaults):
    """
    Generate Section 14 of the DesStruct IN file.
    This section contains endwall framing specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 14 text with endwall framing parameters
    """
    return """*(14)ENDWALL FRAMING:
* Wall     Corner_Column     Interior_Column   ----Rafter---     Splice
*  Id   Type  Rot    Depth    Type    Depth    Type    Depth      Type
    1   'W   :-:-'        0   'W   '        0  'W   '          0   'M :M '
    3   'W   :-:-'        0   'W   '        0  'W   '          0   'M :M '""" 