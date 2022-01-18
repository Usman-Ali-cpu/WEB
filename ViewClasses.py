class User:
    def __init__(self) -> None:
        self.user_id = 0
        self.email = ""
        self.password = "Not set"
        self.name = None

    def __init__(self, name, a_password) -> None:
        self.user_id = id
        self.email = "none"
        self.password = a_password
        self.name = name

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password


class Reviews:
    def __init__(self, profession, desc, rev_id) -> None:
        self.review_id = rev_id
        self.profession = profession
        self.description = desc
