def generate_section_87(excel_dict, defaults):
    dead = 0.10
    collat = 0.00
    live = 0.57
    snow = 0.00
    coeff = 0.00
    roof = "'Y'"

    output = [
        "*(87)EXTENSION LOADS:",
        "*     Ext                                Thermal Slippery",
        "* No.  Id   Dead  Collat   Live   Snow    Coeff    Roof"
    ]
    for i in range(1, 4):
        output.append(f"   3    {i}   {dead:.2f}    {collat:.2f}   {live:.2f}   {snow:.2f}     {coeff:.2f}    {roof}")
    return "\n".join(output) 