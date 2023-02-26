class User:
    def __init__(self, item) -> None:
        self.user_id = item.get('UserId').get('S')
        self.display_name = item.get('DisplayName').get('S')
        self.email = item.get('Email').get('S')
        self.password_hash = item.get('PasswordHash').get('S')

    def __repr__(self) -> str:
        return "User<{} -- {}>".format(self.user_id, self.display_name)


class Tenant:
    def __init__(self, item):
        self.tenant_id = item.get('TenantId').get('S')
        self.display_name = item.get('DisplayName').get('S')
        self.name = item.get('Name').get('S')

    def __repr__(self) -> str:
        return "Tenant<{} -- {}>".format(self.tenant_id, self.display_name)


class Member:
    def __init__(self, item):
        self.tenant_id = item.get('TenantId').get('S')
        self.user_id = item.get('UserId').get('S')

    def __repr__(self) -> str:
        return "Member<{} -- {}>".format(self.tenant_id, self.user_id)