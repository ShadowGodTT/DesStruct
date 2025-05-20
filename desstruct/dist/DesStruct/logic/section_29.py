def generate_section_29(excel_dict, defaults):
    """
    Generate Section 29 of the DesStruct IN file.
    This section contains eave extension specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 29 text with eave extension parameters
    """
    return """*(29)EAVE EXTENSION (NO LONGER USED):
*Wall No. Bay_Id                        Purl_Extend      Purl   -Member--  ------Soffit------   -End_Option-  -----Space-----
* Id  Ext St End      Width     Slope  Start     End     Type   Typ Shape  Part         Color   Left   Right  Peak        Set
   2   0 
   4   0 """ 