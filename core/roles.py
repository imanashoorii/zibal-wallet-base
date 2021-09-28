from rolepermissions.roles import AbstractUserRole

class admin(AbstractUserRole):
    available_permissions = {
        'create_merchant': True,
    }

class operator(AbstractUserRole):
    available_permissions = {
        'edit_merchant': True,
    }

class gateway(AbstractUserRole):
    available_permissions = {}

class gateway_sandbox(AbstractUserRole):
    available_permissions = {}


class pos(AbstractUserRole):
    available_permissions = {}

class pos_sandbox(AbstractUserRole):
    available_permissions = {}

class club(AbstractUserRole):
    available_permissions = {}

class publisher(AbstractUserRole):
    available_permissions = {}

class dist(AbstractUserRole):
    available_permissions = {}

class regulator(AbstractUserRole):
    available_permissions = {}

class customer_support(AbstractUserRole):
    available_permissions = {}

class ipg_transactions(AbstractUserRole):
    available_permissions = {}