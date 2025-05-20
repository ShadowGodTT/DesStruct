def generate_section_46(excel_dict, defaults):
    """
    Generate Section 46 of the DesStruct IN file.
    This section contains extension loads and deflection limits specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 46 text with extension loads and deflection limits parameters
    """
    return """*(46)EXTENSION LOADS & DEFLECTION LIMITS:
*                      -----------------------Deflection Limits-----------------------
*       ---Snow--      --Horizontal_Beam--  Horizontal-Beam-Purlin  --Vertical_Facia--
*Dead   SW     EW      Live   Wind   Total   Live   Wind   Total    Beam   Panel  Girt
  0.10   0.00   0.00     180    180    120     150    150    120      120    120    120""" 