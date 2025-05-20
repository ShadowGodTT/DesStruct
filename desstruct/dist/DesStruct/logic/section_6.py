def generate_section_6(excel_dict, defaults):
    """
    Generate Section 6 of the DesStruct IN file.
    This section contains deflection limits for various structural elements.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 6 text with deflection limits
    """
    # Default deflection limits in mm
    ew_col = 120
    ew_raf_live = 180
    ew_raf_wind = 150
    wall_girt_live = 180
    wall_girt_wind = 120
    wall_panel_live = 180
    wall_panel_wind = 120
    roof_panel_live = 180
    roof_panel_wind = 120
    rigid_frame_horz = 100
    rigid_frame_live = 180
    rigid_frame_bent = 60
    crane = 100
    seismic = 50
    wind_frame = 50
    total_vert_purlin = 0
    total_vert_ew = 0
    total_vert_rf = 0

    return f"""*( 6)DEFLECTION LIMITS:
*  EW   --EW_RAF--  Wall  --Purlin--  Wall  Roof_Panel  Rigid_Frame Wind Rigid_Frame Wind_Frame -Total_Vertical-
*  Col  Live  Wind  Girt  Live  Wind Panel  Live  Wind  Horz  Live  Bent Crane Seism   Seismic  Purlin   EW   RF
   {ew_col}   {ew_raf_live}   {ew_raf_wind}    90   {wall_girt_live}   {wall_girt_wind}    90   {roof_panel_live}   {roof_panel_wind}   {rigid_frame_horz}   {rigid_frame_live}    {rigid_frame_bent}   {crane}    {seismic}    {wind_frame}           {total_vert_purlin}    {total_vert_ew}    {total_vert_rf}""" 