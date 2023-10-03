from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low
from messages.messages import Alert

message_printer = Agent(name="message_printer", endpoint =["http://localhost:8001"], port=8001)

fund_agent_if_low(message_printer.wallet.address())

@message_printer.on_message(model = Alert)
async def message_handler(ctx: Context,sender:str,message: Alert):
    ctx.logger.info(f"Received msg from {ctx.name}: {message.message}")
