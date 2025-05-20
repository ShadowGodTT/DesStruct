def generate_section_25(excel_dict, defaults):
    """
    Generate Section 25 of the DesStruct IN file.
    This section contains wind framing specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 25 text with wind framing parameters
    """
    return """*(25)WIND FRAMING:
* Wall  Panel  Diagonal  Wind   Wind   Weak_Axis  Brace
*  Id   Shear  Bracing   Bent  Column   Bending   Option    Height
    1    'N'     'N'     'N'     'N'     'N'      '--'         0
    2    'N'     'R'     'N'     'N'     'N'      '--'         0
    3    'N'     'N'     'N'     'N'     'N'      '--'         0
    4    'N'     'R'     'N'     'N'     'N'      '--'         0
    5    'N'     'R:N'   'N'     'N'     'N'      '--'         0""" 