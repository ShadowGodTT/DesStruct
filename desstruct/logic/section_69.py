def safe_float(val, default=0.0):
    try:
        return float(val)
    except (ValueError, TypeError):
        return default

def generate_section_69(excel_dict, defaults):
    cap = safe_float(excel_dict.get("Crane Capacity in MT", 100.0), 100.0)
    brg = 122.4
    ht = 8.4
    load = 82
    long = 10.0
    lat = 20.0
    vert = 10.0
    wheel_base = int(safe_float(excel_dict.get("Wheel Base in mm", 4600), 4600))
    crane_class = "'C'"
    cond = "500000"

    return f"""*(69)RUNWAY CRANES:
*    Sys                         -------Loads-------  Max.Whl  --------Power / %_Force--------  --Wheel_Base-- Service Load
*No.  Id  Id  Start     End      Cap     Brg    H/T    Load    --Long---  ---Lat---  --Vert---   Out     In     Class  Cond
  1    1  1         0     27480 {cap:6.2f}  {brg:5.1f}    {ht:.1f}       {load}  'E'  {long:.1f}  'E'  {lat:.1f}  'E'  {vert:.1f}    {wheel_base}       0   {crane_class}    {cond}""" 