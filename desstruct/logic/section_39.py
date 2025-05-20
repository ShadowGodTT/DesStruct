def generate_section_39(excel_dict, defaults):
    """
    Generate Section 39 of the DesStruct IN file.
    This section contains wall properties data specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 39 text with wall properties parameters
    """
    output = [
        "*(39)WALL PROPERTIES DATA:",
        "* Walls       -----Base-----  -----Seismic------",
        "*No. Id  Opt  Notch    Grout  Dead   Force  Girt"
    ]
    wall_opts = ["'0'", "'0'", "'0'", "'4'"]  # example: 4th wall has different Opt
    for i, opt in enumerate(wall_opts):
        output.append(
            f"  4   {i+1}  {opt}  0.000    0.000   0.000  'Y'   'N'"
        )
    return "\n".join(output) 