def generate_section_8(excel_dict, defaults):
    """
    Generate Section 8 of the DesStruct IN file.
    This section contains building load specifications.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 8 text with building loads
    """
    # Extract and convert load values
    dead = float(excel_dict.get("Dead Load in kN/m2", 0.1))
    live = float(excel_dict.get("Live Load in kN/m2", 0.575))
    snow = 0.000
    collat = float(excel_dict.get("Collateral load kN/m2", 0.05))
    wind_speed = float(excel_dict.get("Max wind speed in m/s", 39)) * 3.6  # convert m/s to km/h
    load_reduce = "'N'"
    wind10 = 0.000
    wind30 = 0.000
    sa02 = 0.0000
    sa05 = 0.1000
    sa10 = 0.0000
    sa20 = 1.0000
    
    # Extract temperature value, handling the "degrees" suffix
    temp_str = excel_dict.get("Maximum temperate variation", "20 degrees")
    temp = int(temp_str.split()[0])  # Get just the number part

    return f"""*( 8)BUILDING LOADS:
*  Dead    Live    Snow   Colat.  Wind     Load
*  Load    Load    Load    Load   Speed    Reduce Wind10  Wind30   Sa02   Sa05   Sa10   Sa20  Temp
   {dead:.3f}   {live:.3f}   {snow:.3f}   {collat:.3f}  {wind_speed:.3f}    {load_reduce}   {wind10:.3f}   {wind30:.3f}  {sa02:.4f} {sa05:.4f} {sa10:.4f} {sa20:.4f}   {temp}""" 