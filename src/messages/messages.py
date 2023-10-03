from uagents import Model

class Temperature(Model):
    value: float


class Alert(Model):
    message: str
