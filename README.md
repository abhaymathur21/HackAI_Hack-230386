<h1>Temperature Alert Agent</h1>

<h3>Description:</h3>

In this project we have made an application that:
- Lets users set their preferred temperature range (e.g. a minimum and maximum temperature) and location
- Sends an alert notification to the user when the temperature in their chosen location goes below the minimum or above the maximum threshold they've set

We used fetch.ai's uAgents library to create two agents:
-  alert_agent: This is an agent created by the custom Agent class 'Temperature_Alert_Agent' that we have defined. It fetches the temperature of the user-specified location from https://openweathermap.org/ and checks if it is within the user-specified temperature range or not and sends an alert message along with the current temperature if it is outside the range to the the message_printer agent
- message_printer: This agent receives the alert message sent by the alert_agent and prints it in the terminal in a colour we have specified

<h3>HOW TO GET THE TEMPERATURE API:</h3>
- To create an API key, go to https://openweathermap.org/ and make an account
- Once you are logged in, go to the 'My API keys' section of your profile and generate a new API key with the name uAgents
- Make sure its status says 'Active'
- Copy paste that API into the quotes above.

<h3>INSTRUCTIONS TO RUN THIS PROJECT:</h3>
- Clone this repository into a folder:
git clone https://github.com/abhaymathur21/Temperature_Alert_Agent.git

- Open a Terminal in the folder

- Install poetry (we installed it in WSL): https://python-poetry.org/docs/#installing-with-the-official-installer

- Then type the following commands in the terminal opened in Temperature_Alert_Agent:
poetry shell
poetry install 
cd src
poetry run python3 main.py

- Then,
Enter a location
Enter the minimum temperature of your range
Enter the maximum temperature of your range

*The program will now send you an alert in the terminal itself if the current temperature of the location you mentioned is above or below your specified temperature range.*

