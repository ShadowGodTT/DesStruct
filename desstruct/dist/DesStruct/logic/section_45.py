def generate_section_45(excel_dict, defaults):
    """
    Generate Section 45 of the DesStruct IN file.
    This section contains additional loads specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 45 text with additional loads parameters
    """
    return """*(45)ADDITIONAL LOADS:
*No.   Frame  Surf/  Basic    Load       Fx        Fy       Mom        DX        DY          ----Surface----
*Load  Load   Col    Load     Type       W1        W2        Co        D1        D2  Orn     Start       End
   0""" 