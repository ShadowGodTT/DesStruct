def generate_section_48(excel_dict, defaults):
    """
    Generate Section 48 of the DesStruct IN file.
    This section contains extension size specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 48 text with extension size parameters
    """
    return """*(48)EXTENSION SIZE:
*      ----Horizontal_Size----     ------Vertical_Size-------    -Orientation-  ---Beam---
* Id   Elev     Width    Slope     Elev     Height      Slope    Beam    Panel  Type Shape
   1      7300     4500 10.0000          0        0    0.0000    '-'     '-'    'S'  'H'
   2      7300     4500 10.0000          0        0    0.0000    '-'     '-'    'S'  'H'
   3      7300     4500 10.0000          0        0    0.0000    '-'     '-'    'S'  'H'""" 