def generate_section_53(excel_dict, defaults):
    pressure = "0.00"
    col = 90
    girt = 90
    panel = 90

    return f"""*(53)PARTITION WALL LOADS & DEFLECTION LIMITS:
*  Wind      ---Deflection--- 
* Pressure   Col   Girt  Panel
    {pressure}      {col}    {girt}     {panel}""" 