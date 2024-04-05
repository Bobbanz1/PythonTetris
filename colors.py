class Colors:
    # Grid color
    dark_grey = (26, 31, 40)

    # L Block
    #   0
    # 000
    purple = (138, 43, 226)

    # J Block
    # 0
    # 000
    sonic_silver = (117, 117, 117)

    # I Block
    # 0000
    pink = (255, 192, 203)

    # O Block
    # 00
    # 00
    light_green = (144, 238, 144)

    # S Block
    #  00
    # 00
    red = (60, 0, 0)

    # T Block
    #  0
    # 000
    metallic_gold = (219, 172, 52)

    # Z Block
    # 00
    #  00
    flame_orange = (251, 139, 35)

    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (137, 207, 240)

    @classmethod
    def get_cell_colors(cls):
        return [
            cls.dark_grey,
            cls.purple,
            cls.sonic_silver,
            cls.pink,
            cls.light_green,
            cls.red,
            cls.metallic_gold,
            cls.flame_orange,
        ]
