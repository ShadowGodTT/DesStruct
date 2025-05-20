def generate_section_12(excel_dict, defaults):
    """
    Generate Section 12 of the DesStruct IN file.
    This section contains wall bay spacing specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 12 text with wall bay spacing parameters
    """
    # Assuming wall bay spacing format is like "6@7.5" meaning 6 bays of 7.5m each
    def parse_bay_spacing(value):
        try:
            count, size = value.split("@")
            return int(count), float(size) * 1000  # convert m to mm
        except:
            return 0, 0.0

    left_bays, left_width = parse_bay_spacing(excel_dict.get("Left end wall bay spacing in m", ""))
    right_bays, right_width = parse_bay_spacing(excel_dict.get("Right end wall bay spacing in m", ""))
    side_bays, side_width = parse_bay_spacing(excel_dict.get("Side wall bay spacing", ""))

    return f"""*(12)WALL BAY SPACING:
*  Wall   Sets     Bay     No.
*   Id    Bays    Width    Bays
     1      1       {int(left_width)}     {left_bays}
     2      1       {int(side_width)}     {side_bays}
     3      1       {int(right_width)}     {right_bays}
     4      1       {int(side_width)}     {side_bays}
     5      1       {int(side_width)}     {side_bays}""" 