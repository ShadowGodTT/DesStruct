def generate_section_20(excel_dict, defaults):
    """
    Generate Section 20 of the DesStruct IN file.
    This section contains roof purlin spacing specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 20 text with roof purlin spacing parameters
    """
    peak_space = 300
    max_space = 1650
    set_space = 0
    left = 0
    right = 0
    soffit = "'------------'"

    output = [
        "*(20)ROOF PURLIN SPACING:",
        "* Surf   Peak     Max      Set     ------Surface_Ext------",
        "*  Id    Space   Space    Space    Left     Right   Soffit"
    ]
    for surf_id in [2, 3]:
        output.append(
            f"    {surf_id}      {peak_space}     {max_space}        {set_space}        {left}        {right}  {soffit}"
        )
    return "\n".join(output) 