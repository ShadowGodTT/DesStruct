def generate_section_9(excel_dict, defaults):
    """
    Generate Section 9 of the DesStruct IN file.
    This section contains building shape specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 9 text with building shape parameters
    """
    build_type = "'FF-S'"
    width = float(excel_dict.get("Width in m (o/o of steel)", 0)) * 1000
    length = float(excel_dict.get("Length in m (o/o of steel)", 0)) * 1000
    eave_height = float(excel_dict.get("Eave height in m", 0)) * 1000
    peak_offset = length / 2  # assuming symmetrical gable roof
    
    # Parse roof slope from format "X:100"
    slope_str = excel_dict.get("Roof slope (?:100)", "10:100").split(":")
    slope = round(float(slope_str[0]) / float(slope_str[1]), 4) if len(slope_str) == 2 else 1.2

    return f"""*( 9)BUILDING SHAPE:
* Build   Build     Build    L_Eave   R_Eave   Peak     L_Roof
* Type    Width    Length    Height   Height   Offset   Slope
 {build_type}      {int(width)}    {int(length)}      {int(eave_height)}     {int(eave_height)}    {int(peak_offset)}  {slope:.4f}""" 