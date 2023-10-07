from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from messages.messages import Alert
from colored import Fore, Back, Style

color: str = f"{Style.underline}{Fore.cyan}{Back.black}"  # This is used to color the output

# Here we have defined an agent to receive the messages from the Temperature_Alert_Agent and print it
message_printer = Agent(name="message_printer", endpoint=["http://localhost:8001"], port=8001)

fund_agent_if_low(message_printer.wallet.address())


# Here we are using the on_message decorator to receive the messages from the Temperature_Alert_Agent and thenprint it
@message_printer.on_message(model=Alert)
async def message_handler(ctx: Context, sender: str, message: Alert):
    ctx.logger.info(f"{color}Received msg from {ctx.name}: {message.message}{Style.reset}")
