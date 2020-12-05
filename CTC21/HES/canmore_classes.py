class Shipwreck:
    def __init__(self, name, ship_type, council_name, loc, can_id):
        if name.lower() != "unknown":
            self.name = name
        else:
            self.name = "Unnamed shipwreck - Canmore " + can_id
        self.ship_type = ship_type
        if council_name != "Q00000":
            self.council = council_name
        self.location = loc
        self.can_id = can_id

    def __str__(self):
        return f"Name: {self.name}, Type: {self.ship_type}, Council: {self.council}, Loc: {self.location}, Canmore ID: {self.can_id}"

    def create_string(self):
        return(
            "CREATE\n"
            f'LAST\tLen\t"{self.name}"\n'
            f'LAST\tDen\t"Shipwreck added as part of CTC21"\n'
            f"LAST\tP31\t{self.ship_type}\n"
            f"LAST\tP31\tQ852190\n"
            f"LAST\tP17\tQ145\n"
            f"LAST\tP131\t{self.council}\n"
            f"LAST\tP625\t{self.location}\n"
            f"LAST\tP793\tQ906512\n"
            f"LAST\tP1343\tQ5032525\n"
            f'LAST\tP718\t"{self.can_id}"'
        )
