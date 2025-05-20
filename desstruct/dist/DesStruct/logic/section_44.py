def generate_section_44(excel_dict, defaults):
    """
    Generate Section 44 of the DesStruct IN file.
    This section contains canopy specifications (no longer used).
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 44 text with canopy parameters
    """
    return """*(44)CANOPY (NO LONGER USED):
*Wall No. Bay_Id                             Purl_Extend       Purl  -Member--   ------Soffit------  --------Roof-------  -End_Option-  Screw   -Standing_Seam-  -----Space-----
* Id  Ext St End  Width    Height   Slope    Start    End      Type  Typ Shape   Part         Color  Part          Color  Left   Right  Type    Use  Type  Clip  Peak        Set
   1   0 
   2   0 
   3   0 
   4   0 """ 