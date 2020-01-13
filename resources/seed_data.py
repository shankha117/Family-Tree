
# Initial family mappings based on the problem pdf

alpha_data = [
            # Alpha Gen
                # new child
            {"name": "King Shan", "sex": "M", "mother": None, "partner":None},
                # new marriage
            {"name": "Queen Anga", "sex": "F", "mother": None, "partner": "King Shan"},
]


family_data = [
            # 1st Gen
                # new childs
            {"name": "Chit", "sex": "M", "mother": "Queen Anga", "partner":None},
            {"name": "Ish", "sex": "M", "mother": "Queen Anga", "partner":None},
            {"name": "Aras", "sex": "M", "mother": "Queen Anga", "partner":None},
            {"name": "Vich", "sex": "M", "mother": "Queen Anga", "partner":None},
            {"name": "Satya", "sex": "F", "mother": "Queen Anga", "partner":None},
                # new marriage
            {"name": "Amba", "sex": "F", "mother": None, "partner": "Chit"},
            {"name": "Lika", "sex": "F", "mother": None, "partner": "Vich"},
            {"name": "Vyan", "sex": "M", "mother": None, "partner": "Satya"},
            {"name": "Chitra", "sex": "F", "mother": None, "partner": "Aras"},

            # 2nd Gen
                # new child
            {"name": "Dritha", "sex": "F", "mother": "Amba", "partner": None},
            {"name": "Tritha", "sex": "F", "mother": "Amba", "partner": None},
            {"name": "Vrita", "sex": "M", "mother": "Amba", "partner": None},
            {"name": "Vila", "sex": "F", "mother": "Lika", "partner": None},
            {"name": "Chika", "sex": "F", "mother": "Lika", "partner": None},
            {"name": "Jnki", "sex": "F", "mother": "Chitra", "partner": None},
            {"name": "Ahit", "sex": "M", "mother": "Chitra", "partner": None},
            {"name": "Asva", "sex": "M", "mother": "Satya", "partner": None},
            {"name": "Vyas", "sex": "M", "mother": "Satya", "partner": None},
            {"name": "Atya", "sex": "F", "mother": "Satya", "partner": None},

                # new marriage
            { "name": "Jaya", "sex": "M","mother": None, "partner": "Dritha"},
            { "name": "Arit", "sex": "M","mother": None, "partner": "Jnki"},
            { "name": "Satvy", "sex": "F","mother": None, "partner": "Asva"},
            { "name": "Krpi", "sex": "F","mother": None, "partner": "Vyas"},


            # 3rd Gen

            {"name": "Yodhan", "sex": "M", "mother": "Dritha", "partner": None},
            {"name": "Laki", "sex": "M", "mother": "Jnki", "partner": None},
            {"name": "Lavnya", "sex": "F", "mother": "Jnki", "partner": None},
            {"name": "Vasa", "sex": "M", "mother": "Satvy", "partner": None},
            {"name": "Kriya", "sex": "M", "mother": "Krpi", "partner": None},
            {"name": "Krithi", "sex": "F", "mother": "Krpi", "partner": None}

    ]