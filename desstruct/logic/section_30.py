def generate_section_30(excel_dict, defaults):
    """
    Generate Section 30 of the DesStruct IN file.
    This section contains gutters and downspouts specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 30 text with gutters and downspouts parameters
    """
    length = int(float(excel_dict.get("Length in m (o/o of steel)", 0)) * 1000)
    downspouts = 8
    gutter_color = "'----E'"
    downspout_color = "'----'"

    return f"""*(30)GUTTERS & DOWNSPOUTS:
*    Gutter_Length      No. Downspouts    ------Color-----
*  Front_SW  Back_SW   Front_SW  Back_SW  Gutter Downspout
     {length}     {length}     {downspouts}         {downspouts}      {gutter_color}   {downspout_color}""" 