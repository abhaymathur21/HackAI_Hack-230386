from uagents import Model

# Here we have defined the models for the messages


class Temperature(Model):
    value: float


class Alert(Model):
    message: str
