def generate_section_4(excel_dict, defaults):
    """
    Generate Section 4 of the DesStruct IN file.
    This section contains base options and configurations.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 4 text with base options
    """
    # Extract values from Excel input, normalize
    base_detail = excel_dict.get("Base Detail", "").strip().lower()
    
    # Derive flags
    angle = "'Y'" if "angle" in base_detail or base_detail == "" else "'N'"
    channel = "'Y'" if "channel" in base_detail else "'N'"
    seal = "'NHA--'" if "seal" in base_detail or base_detail == "" else "'N'"
    angle_seal = "'N'"  # usually default, override if Excel defines it separately

    # Assume 4 walls — apply same values (unless future version adds per-wall logic)
    output = [
        "*( 4)BASE OPTIONS:",
        "*  Angle   Channel   Seal   Angle/Seal"
    ]
    for _ in range(4):
        output.append(f"   {angle}      {channel}      {seal}      {angle_seal}")
    
    return "\n".join(output) 