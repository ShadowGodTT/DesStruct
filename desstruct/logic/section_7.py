def generate_section_7(excel_dict, defaults):
    """
    Generate Section 7 of the DesStruct IN file.
    This section contains building code specifications and parameters.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values (not used in this section)
        
    Returns:
        str: Formatted section 7 text with building code parameters
    """
    code = "'MBMA:WS'"
    year = "'10:AISC05:NAUS07  '"  # standardized
    exposure = excel_dict.get("Exposure category", "B").strip().upper()
    closure = "'C '"  # default unless Excel says Open
    seismic_zone = excel_dict.get("Seismic zone", "II").strip().upper()
    importance_seis = "1.00"
    importance_wind = "1.00"
    column_wind_ew = "'YY'"
    column_wind_sw = "'YY'"

    return f"""*( 7)BUILDING CODE:
* Wind Des Code  Hot   Cold      Exposure/Code                   Closure  Seismic   Importance  Column_Wind
* Code Typ Year  Ver    Ver     (B/C:CCode:Code Lbl:Code File)    (O/C)    Zone     Seis  Wind  EW     SW 
 {code} {year}  '{exposure}  :    :MBMA 10 :MBMA.10     '  {closure}    '{seismic_zone} '      {importance_seis}  {importance_wind}  {column_wind_ew}   {column_wind_sw}""" 