def generate_section_33(excel_dict, defaults):
    """
    Generate Section 33 of the DesStruct IN file.
    This section contains walkdoors and accessories specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 33 text with walkdoors and accessories parameters
    """
    return """*(33)WALKDOORS & ACCESSORIES:
* Data   Door    Door  Door   Weather  --Hardware---  Door  Lock Acc  Close
* Lines  Size    Quan  Color  Stripp.  Panic Mullion  Type  Type Type  Type
     0""" 