def section_16(excel_dict, defaults):
    """Process Section 16: BASE ELEVATION."""
    # Get fallback from "Eave height in m" if base elevation fields are missing
    fallback_elev = float(excel_dict.get("Eave height in m", 0))  # in meters

    def get_base_elev(field):
        value = excel_dict.get(field, None)
        return int(float(value) * 1000) if value else int(fallback_elev * 1000)

    left = get_base_elev("Left endwall base elev")
    right = get_base_elev("Right endwall base elev")
    front = get_base_elev("Front sidewall base elev")
    back = get_base_elev("Back sidewall base elev")

    return f"""*(16)BASE ELEVATION:
*  -----Base_Elevation-------
*    Endwalls       Sidewalls
*  Left   Right   Front   Back
  {left:5d}  {right:5d}  {front:6d}  {back:5d}""" 