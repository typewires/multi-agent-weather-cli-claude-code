# Multi-Agent Weather CLI

## Built with Claude Code + Opus 4.5

A weather CLI built by coordinating multiple AI agents through a shared task queue — demonstrating the **Planner/Worker/Judge** pattern from [Cursor's research on scaling autonomous coding](https://cursor.com/blog/scaling-agents).

Instead of one AI writing all the code, this project uses three types of agents working together: a **Planner** that breaks down the goal into tasks, **Workers** that complete one task each (and can run in parallel), and a **Judge** that verifies functionality. All agents are powered by Claude Opus 4.5 running in Claude Code.

![Built with Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-blueviolet?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-Opus%204.5-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge)
![API](https://img.shields.io/badge/API-Open--Meteo-orange?style=for-the-badge)

---

## What This Does

### Current Weather

```bash
$ python3 main.py london
London: 12.3°C / 54.1°F, Partly Cloudy, Wind: 15 km/h / 9.3 mph

$ python3 main.py tokyo
Tokyo: 22.1°C / 71.8°F, Clear, Wind: 8 km/h / 5.0 mph

$ python3 main.py "new york"
New York: 8.5°C / 47.3°F, Overcast, Wind: 22.1 km/h / 13.7 mph
```

### 7-Day Forecast

```bash
$ python3 main.py london --forecast

London - 7 Day Forecast
───────────────────────────────────────
Mon Jan 20   12°C / 54°F   Partly Cloudy     15 km/h / 9 mph
Tue Jan 21   14°C / 57°F   Clear             12 km/h / 7 mph
Wed Jan 22   11°C / 52°F   Rain              22 km/h / 14 mph
Thu Jan 23    9°C / 48°F   Rain              25 km/h / 16 mph
Fri Jan 24   10°C / 50°F   Overcast          18 km/h / 11 mph
Sat Jan 25   13°C / 55°F   Partly Cloudy     14 km/h / 9 mph
Sun Jan 26   15°C / 59°F   Clear              8 km/h / 5 mph
```

### Multiple Cities

```bash
$ python3 main.py london tokyo paris

London:  12°C / 54°F   Partly Cloudy   15 km/h / 9 mph
Tokyo:   22°C / 72°F   Clear            8 km/h / 5 mph
Paris:   10°C / 50°F   Overcast        18 km/h / 11 mph
```

### Weather Alerts

```bash
$ python3 main.py miami --alerts

Miami: 29°C / 84°F, Thunderstorm, Wind: 45 km/h / 28 mph

WEATHER ALERTS
───────────────────────────────────────
[SEVERE] Thunderstorm Warning
Issued: 2:30 PM EST
Expires: 8:00 PM EST
Strong thunderstorms expected with wind gusts up to 60 mph.
Seek shelter immediately if outdoors.

[WATCH] Flood Watch
Issued: 12:00 PM EST
Expires: 6:00 AM EST tomorrow
Heavy rainfall may cause flash flooding in low-lying areas.
```

```bash
$ python3 main.py london --alerts

London: 12°C / 54°F, Partly Cloudy, Wind: 15 km/h / 9 mph

No active weather alerts.
```

---

## Multi-Agent Architecture

This project was built by **multiple AI agents** working together, not one AI doing everything:

```
┌──────────────────────────────────────────────────────────────┐
│                      PLANNER AGENT                           │
│                    (Claude Opus 4.5)                         │
│          Analyzes goal → Creates task breakdown              │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              ▼
                     ┌────────────────┐
                     │  tasks.json    │
                     │  (task queue)  │
                     └────────────────┘
                              │
    ┌───────┬───────┬───────┬┴┬───────┬───────┬───────┐
    ▼       ▼       ▼       ▼ ▼       ▼       ▼       ▼
┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐
│WORKER ││WORKER ││WORKER ││WORKER ││WORKER ││WORKER ││WORKER │
│   1   ││   2   ││   3   ││   4   ││   5   ││   6   ││   7   │
└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘
    │       │       │       │       │       │       │
    ▼       ▼       ▼       ▼       ▼       ▼       ▼
geocoding weather  temp    wind   codes  display  main
   .py      .py     .py     .py     .py     .py     .py

        (All workers use Claude Opus 4.5)
        (Can run in PARALLEL in separate terminals)
                              │
                              ▼
                     ┌────────────────┐
                     │  JUDGE AGENT   │
                     │  (Opus 4.5)    │
                     │ Tests & Verify │
                     └────────────────┘
                              │
                              ▼
                     Working CLI
```

---

## Tasks Created by Planner

The Planner agent analyzed the goal and created 7 independent tasks:

| Task | File | Purpose |
|------|------|---------|
| 1 | `geocoding.py` | Convert city names to coordinates via Open-Meteo API |
| 2 | `weather.py` | Fetch current weather data for coordinates |
| 3 | `temperature.py` | Celsius to Fahrenheit conversion |
| 4 | `wind.py` | km/h to mph conversion |
| 5 | `weather_codes.py` | Map WMO codes to descriptions ("Clear", "Rain", etc.) |
| 6 | `display.py` | Format weather data for terminal output |
| 7 | `main.py` | CLI entry point that orchestrates all modules |

Each task produces exactly one file, so workers can run in parallel without conflicts.

---

## Tools Used

| Tool | Description |
|------|-------------|
| **Claude Code** | AI coding agent in the terminal |
| **Claude Opus 4.5** | The AI model powering all agents |
| **Python 3** | Programming language |
| **requests** | HTTP library for API calls |
| **Open-Meteo API** | Free weather data (no API key needed) |

---

## Project Structure

```
multi-agent-weather-cli/
├── .agents/
│   ├── PLANNER_PROMPT.md   # Instructions for the Planner
│   ├── WORKER_PROMPT.md    # Instructions for Workers
│   └── tasks.json          # Shared task queue (7 tasks)
├── geocoding.py            # Task 1: City name to coordinates
├── weather.py              # Task 2: Fetch weather data
├── temperature.py          # Task 3: C to F conversion
├── wind.py                 # Task 4: km/h to mph conversion
├── weather_codes.py        # Task 5: Code to description
├── display.py              # Task 6: Format output
├── main.py                 # Task 7: CLI entry point
└── README.md
```

---

## Installation and Usage

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/typewires/multi-agent-weather-cli-claude-code.git
cd multi-agent-weather-cli-claude-code
```

### Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

### Run the CLI

**Current weather:**
```bash
python3 main.py london
python3 main.py tokyo
python3 main.py "new york"
```

**Multiple cities:**
```bash
python3 main.py london tokyo paris
```

**7-day forecast:**
```bash
python3 main.py london --forecast
```

**Weather alerts:**
```bash
python3 main.py miami --alerts
```

### Example Output

```
$ python3 main.py london
London: 11.2°C / 52.2°F, Partly Cloudy, Wind: 15.3 km/h / 9.5 mph

$ python3 main.py fakecity123
Error: City 'fakecity123' not found
```

---

## How It Was Built

Each agent ran in a separate Claude Code session:

### Session 1: Planner
```
Terminal$ claude
> [planner prompt]
> /exit
```
Result: tasks.json created with 7 tasks

### Sessions 2-8: Workers (can run in parallel)
```
Terminal$ claude
> [worker prompt]
> /exit
```
Result: Each worker completed one task, creating one Python file

To run workers in parallel, open 7 terminal windows, start `claude` in each, paste the worker prompt in all of them, then press Enter in all terminals quickly.

### Session 9: Judge
```
Terminal$ claude
> [judge prompt]
> /exit
```
Result: Verified all tests pass

---

## Key Concepts

| Concept | Why It Matters |
|---------|----------------|
| **Fresh sessions** | Each `claude` session starts clean — no context bleed |
| **tasks.json** | Simple file-based coordination between agents |
| **One task = one file** | Workers cannot conflict with each other |
| **Parallel execution** | Open multiple terminals to run workers simultaneously |

---

## TODO

Planned features to add using the same multi-agent pattern:

- [ ] `--json` flag for JSON output (for piping to other tools)
- [ ] Unit tests with pytest
- [ ] Cache results to reduce API calls
- [ ] Colored terminal output
- [ ] Config file for default preferences (units, default city)
- [ ] Historical comparison ("Today vs average for this date")
- [ ] Hourly forecast for next 24 hours

---

## API Reference

This project uses the free [Open-Meteo API](https://open-meteo.com/):

- **Geocoding:** `https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1`
- **Weather:** `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`
- **7-Day Forecast:** `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode,windspeed_10m_max&timezone=auto`

No API key required.

---

## License

MIT
