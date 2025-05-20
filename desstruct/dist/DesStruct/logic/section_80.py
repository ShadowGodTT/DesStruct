def generate_section_80(excel_dict, defaults):
    part = "'--------'"
    color = "'----'"
    opt = "'-N'"
    base = "'----'"
    trim = "'------------'"
    top = "'----'"
    screw = "'---'"
    ins_use = "'-'"
    ins_type = "'--'"
    thickness = "0"
    wire = "'-'"
    rot = "'-'"

    output = [
        "*(80)PARTIAL WALL PANEL & TRIM:",
        "*    --------Panel-----------   -----------Trim----------   Screw  ----Insulation-----  Panel",
        "*Id  Part        Color    Opt   Base   LeftRghtJamb   Top   Type   Use Type Thick Wire   Rot"
    ]
    for i in range(1, 5):
        output.append(
            f"  {i} {part}  {color}   {opt}  {base} {trim} {top} {screw}  {ins_use} {ins_type}     {thickness}  {wire}   {rot}"
        )
    return "\n".join(output) 