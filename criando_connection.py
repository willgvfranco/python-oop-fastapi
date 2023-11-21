class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def connect(self):
        pass

    @classmethod
    def create_with_auth(cls, user, password):
        c = cls()
        c.set_user(user)
        c.set_password(password)
        return c


c1 = Connection()
c1.set_user("luiz")
c1.set_password("<PASSWORD>")
