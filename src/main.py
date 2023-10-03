import requests
from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low

from agents.temperature.TemperatureAlertAgent import alert_agent

from agents.temperature.message_printer import message_printer

bureau = Bureau()
bureau.add(alert_agent)
bureau.add(message_printer)

if __name__ == "__main__":
    bureau.run()