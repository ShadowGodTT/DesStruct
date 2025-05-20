def safe_float(val, default=0.0):
    try:
        return float(val)
    except (ValueError, TypeError):
        return default

def generate_section_67(excel_dict, defaults):
    span = int(safe_float(excel_dict.get("Crane span in m", 27.48), 27.48) * 1000)
    elev = int(safe_float(excel_dict.get("Crane beam top height in m", 6), 6) * 1000)
    offset = 1100
    start = 0
    end = int(safe_float(excel_dict.get("Length in m (o/o of steel)", 48.174), 48.174) * 1000)

    return f"""*(67)CRANE RUNWAY LAYOUT:
*No. Sys Crane Runway -----------------Runway Location----------------
*Sys Id  Type  Orn    Elev     Offset     Span       Start      End       
  1  1   'TG'  'L'     {elev}      {offset}     {span}          {start}     {end}""" 