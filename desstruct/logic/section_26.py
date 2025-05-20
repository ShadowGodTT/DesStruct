def generate_section_26(excel_dict, defaults):
    """
    Generate Section 26 of the DesStruct IN file.
    This section contains wind bracing location specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 26 text with wind bracing location parameters
    """
    return """*(26)WIND BRACING LOCATION:
* Wall  No.    Bay
*  Id   Bays   Id
    1     0   
    2     2    1  6 
    3     0   
    4     2    1  6 
    5     2    1  6 """ 