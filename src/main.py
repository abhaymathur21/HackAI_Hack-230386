import requests
from uagents import Agent, Context, Bureau, Model
from uagents.setup import fund_agent_if_low


class Temperature(Model):
    value: float


class Alert(Model):
    message: str


class TemperatureAlertAgent(Agent):
    def __init__(self, name: str, seed: str, endpoint: str, location: str, min_temp: float, max_temp: float, api_key: str, port: int):
        super().__init__(name=name, seed=seed, endpoint=endpoint, port=port)
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.api_key = api_key
        self.endpoint = endpoint

    async def get_temperature(self) -> float:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            return temp
        else:
            raise Exception(f"Failed to fetch temperature data: {response.text}")

    async def check_temperature(self,ctx: Context):
        temp = await self.get_temperature()
        if temp < self.min_temp:
            msg = f"Temperature is below minimum threshold ({self.min_temp}): {temp}"
            alert = Alert(message=msg)
            # print(msg)
            await ctx.send(destination=self.endpoint,message=alert)
        elif temp > self.max_temp:
            msg = f"Temperature is above maximum threshold ({self.max_temp}): {temp}"
            alert = Alert(message=msg)
            # print(msg)
            await ctx.send(destination=self.endpoint,message=alert)
        else :
            msg = f"Temperature is within the range: {temp}"
            alert = Alert(message=msg)
            # print(msg)
            await ctx.send(destination=self.endpoint,message=alert)
            
    async def run(self):
        while True:
            await self.check_temperature()
            await self.sleep(60)

# Usage
alert_agent = TemperatureAlertAgent(
    name="alert_agent",
    seed="alert_agent_seed",
    endpoint="http://localhost:8000",
    location=input("Enter Location "),
    port=8000,
    min_temp=float(input("Enter Minimum Temperature ")),
    max_temp=float(input("Enter Maximum Temperature ")),
    api_key="a74eebe6704ebe9ae5aed50998769d85",
)

fund_agent_if_low(alert_agent.wallet.address())

@alert_agent.on_interval(period=10.0)
async def temperature_handler(ctx: Context):
    await alert_agent.check_temperature(ctx)

bureau = Bureau()
bureau.add(alert_agent)

if __name__ == "__main__":
    bureau.run()