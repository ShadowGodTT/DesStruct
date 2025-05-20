def generate_section_5(excel_dict, defaults):
    """
    Generate Section 5 of the DesStruct IN file.
    This section contains steel yield specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 5 text with steel yield values
    """
    # Extract yield values from Excel input
    hot_yield = float(excel_dict.get("Hot rolled sections grade (Mpa)", 235))
    cold_yield = float(excel_dict.get("Cold form sections  grade (Mpa)", 345))
    panel_yield = 250.0  # assumed standard
    flange_plate = float(excel_dict.get("Primary sections grade (Mpa)", 345))
    web_plate = flange_plate
    max_stress_ratio = 1.00

    return f"""*( 5)STEEL YIELD:
*  -------------Steel_Yield--------------    Max
*                Wall  Roof  Flange   Web    Stress
*  Hot   Cold   Panel  Panel  Plate  Plate   Ratio
   {hot_yield:.1f} {cold_yield:.1f}  {panel_yield:.1f}  {panel_yield:.1f}  {flange_plate:.1f}  {web_plate:.1f}   {max_stress_ratio:.2f}""" 