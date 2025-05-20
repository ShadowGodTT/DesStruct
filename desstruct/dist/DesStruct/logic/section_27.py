def generate_section_27(excel_dict, defaults):
    """
    Generate Section 27 of the DesStruct IN file.
    This section contains wind bent location specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 27 text with wind bent location parameters
    """
    return """*(27)WIND BENT LOCATION:
* Wall  No.
*  Id   Bays   BayId
    1     0   
    2     0   
    3     0   
    4     0 """ 