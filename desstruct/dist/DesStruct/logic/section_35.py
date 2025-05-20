def generate_section_35(excel_dict, defaults):
    """
    Generate Section 35 of the DesStruct IN file.
    This section contains accessory items specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 35 text with accessory items parameters
    """
    return """*(35)ACCESSORY ITEMS:
*  No.          Access    Accessory
*  Acc   Quan     Id      Description
     0""" 