from uagents import Bureau

from agents.temperature.message_printer import message_printer
from agents.temperature.TemperatureAlertAgent import alert_agent

# Here we have created a bureau and added the agents to it
bureau = Bureau()
bureau.add(alert_agent)
bureau.add(message_printer)

if __name__ == "__main__":
    bureau.run()
