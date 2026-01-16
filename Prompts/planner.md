Read the file .agents/PLANNER_PROMPT.md for your instructions.

You are the PLANNER agent.

Project goal: Build a Python CLI weather tool that:
- Takes a city name as a command line argument (sys.argv)
- Uses Open-Meteo's FREE API (no API key needed):
  - Geocoding: https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1
  - Weather: https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true
- Displays: city name, temperature in Celsius and Fahrenheit), weather description, wind speed in m/s and mph
- Handles errors gracefully (city not found, network errors)

Create the task breakdown in .agents/tasks.json

Remember: Create small, independent tasks. One task = one Python file.