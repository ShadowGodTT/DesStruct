def generate_section_47(excel_dict, defaults):
    """
    Generate Section 47 of the DesStruct IN file.
    This section contains extension layout specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 47 text with extension layout parameters
    """
    return """*(47)EXTENSION LAYOUT:
*             Wall              ---Bay_Id--    --Edge_Extend-  -End_Option-
* No.    Id    Id  Type  Style  Start   End    Left     Right  Left   Right
   3      1     2  'EC'    0      2      2         0        0  '--'    '--'
          2     2  'EC'    0      5      5         0        0  '--'    '--'
          3     3  'EC'    0      2      2         0        0  '--'    '--'""" 