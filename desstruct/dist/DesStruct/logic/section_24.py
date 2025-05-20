def generate_section_24(excel_dict, defaults):
    """
    Generate Section 24 of the DesStruct IN file.
    This section contains rigid frame interior columns specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 24 text with rigid frame interior columns parameters
    """
    return """*(24)RIGID FRAME INTERIOR COLUMNS:
* Frame  Column  Column  Column   No.       Column
*  Id    Typ/Con Rot/Shp  Elev   Columns   Location
    1     'WPP'    'YC'         0   3          7470
                                             14940
                                             22410
    2     '-P-'    'N-'         0   0 """ 