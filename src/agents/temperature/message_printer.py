from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low
from messages.messages import Alert
from colored import Fore, Back, Style

color: str = f'{Style.underline}{Fore.cyan}{Back.black}'

message_printer = Agent(name="message_printer", endpoint =["http://localhost:8001"], port=8001)

fund_agent_if_low(message_printer.wallet.address())

@message_printer.on_message(model = Alert)
async def message_handler(ctx: Context,sender:str,message: Alert):
    ctx.logger.info(f"{color}Received msg from {ctx.name}: {message.message}{Style.reset}")
