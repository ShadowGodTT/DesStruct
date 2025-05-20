def generate_section_10(excel_dict, defaults):
    """
    Generate Section 10 of the DesStruct IN file.
    This section contains expandable endwall and flush wall specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 10 text with expandable endwall and flush wall parameters
    """
    l_expand_use = "'YY:E'"
    l_expand_offset = "365"
    r_expand_use = "'YY:E'"
    r_expand_offset = "365"
    flush_wall = "'N'"
    flush_depth = "0"
    wall_same = "'Y'"

    return f"""*(10)EXPANDABLE ENDWALL/FLUSH WALL:
* -L_Expand_EW-  -R_Expand_EW-  Flush_Wall  Wall
* Use    Offset  Use    Offset  Use  Depth  Same
 {l_expand_use}     {l_expand_offset} {r_expand_use}     {r_expand_offset}  {flush_wall}      {flush_depth}  {wall_same}""" 