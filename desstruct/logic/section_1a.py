def generate_section_1a(excel_dict, defaults):
    """Process Section 1a: WALL LAYOUT."""
    width = float(excel_dict.get("Width in m (o/o of steel)", 0)) * 1000
    length = float(excel_dict.get("Length in m (o/o of steel)", 0)) * 1000
    fallback_elev = float(excel_dict.get("Eave height in m", 0))  # meters

    def get_base_elev(field):
        value = excel_dict.get(field, None)
        return int(float(value) * 1000) if value else int(fallback_elev * 1000)

    elevs = {
        "LEFT":  get_base_elev("Left endwall base elev"),
        "FRONT": get_base_elev("Front sidewall base elev"),
        "RIGHT": get_base_elev("Right endwall base elev"),
        "BACK":  get_base_elev("Back sidewall base elev"),
        "ROOF":  0  # always 0 for roof
    }

    walls = [
        (1, "'LEFT '",  width, 0.0, width, 0.0, 0.0, elevs["LEFT"]),
        (2, "'FRONT'", length, 0.0, 0.0, length, 0.0, elevs["FRONT"]),
        (3, "'RIGHT'", width, length, 0.0, length, width, elevs["RIGHT"]),
        (4, "'BACK '", length, length, width, 0.0, width, elevs["BACK"]),
        (5, "'ROOF '", length, 0.0, 0.0, length, width, elevs["ROOF"]),
    ]

    output = [
        "*(1a)WALL LAYOUT:",
        "*                                    ---Start_Coord--  ----End_Coord---   Base",
        "*No. Id  Use     Type Opt    Length       X1       Y1       X2       Y2   Elev"
    ]
    for no, use, length, x1, y1, x2, y2, elev in walls:
        output.append(
            f"  {no:<2}  {use:>7}  '-'  '-'  {length:10.4f}  {x1:8.4f} {y1:8.4f}  {x2:8.4f} {y2:8.4f} {elev:8.4f}"
        )
    return "\n".join(output) 