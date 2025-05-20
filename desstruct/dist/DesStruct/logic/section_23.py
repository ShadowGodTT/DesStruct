def generate_section_23(excel_dict, defaults):
    """
    Generate Section 23 of the DesStruct IN file.
    This section contains rigid frames specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 23 text with rigid frames parameters
    """
    return """*(23)RIGID FRAMES:
* No_Diff  Frame  Frame  Load     --Frame_Shape--  Frame  Frame  Frame_Line
* Frames    Id    Type   Width    Col/ConL:R  Raf   Symm    Quan     Id_No.
     2       1    'HP-'     4197  'T:FI:FI'   'T '   'S'      2      1   7 
             2    'RF-'     8029  'T:FI:FI'   'T '   'S'      5      2   3   4   5   6 """ 