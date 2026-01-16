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

```bash
$ python3 weather.py london
London: 12.3°C / 54.1°F, Partly Cloudy, Wind: 15 km/h / 9.3 mph

$ python3 weather.py tokyo
Tokyo: 22.1°C / 71.8°F, Clear, Wind: 8 km/h / 5.0 mph

$ python3 weather.py "new york"
New York: 8.5°C / 47.3°F, Overcast, Wind: 22.1 km/h / 13.7 mph
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
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
       ┌─────────┐       ┌─────────┐       ┌─────────┐
       │ WORKER  │       │ WORKER  │       │ WORKER  │
       │    1    │       │    2    │       │    3    │
       │ api.py  │       │display.py│      │weather.py│
       └─────────┘       └─────────┘       └─────────┘
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
│   └── tasks.json          # Shared task queue
├── api.py                  # API client (geocoding + weather)
├── display.py              # Output formatting
├── weather.py              # Main CLI entry point
└── README.md
```

---

## Installation and Usage

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-weather-cli.git
cd multi-agent-weather-cli
```

### Install Dependencies

```bash
pip3 install requests
```

### Run the CLI

```bash
python3 weather.py london
```

```bash
python3 weather.py tokyo
```

```bash
python3 weather.py "new york"
```

```bash
python3 weather.py paris
```

### Example Output

```
$ python3 weather.py london
London: 11.2°C / 52.2°F, Partly Cloudy, Wind: 15.3 km/h / 9.5 mph

$ python3 weather.py fakecity123
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
Result: tasks.json created with 3 tasks

### Sessions 2-4: Workers
```
Terminal$ claude
> [worker prompt]
> /exit
```
Result: Each worker completed one task (api.py, display.py, weather.py)

Workers can run **in parallel** by opening multiple terminal windows.

### Session 5: Judge
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

## API Reference

This project uses the free [Open-Meteo API](https://open-meteo.com/):

- **Geocoding:** `https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1`
- **Weather:** `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`

No API key required.

---

## License

MIT
