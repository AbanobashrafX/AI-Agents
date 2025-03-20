# Simple Offense Handling Agent (SOHA)

A Python-based Simple AI agent that monitors and responds to offensive language in chat messages, promoting a positive and respectful communication environment.

## Features
- Real-time message monitoring
- Offensive word detection using a customizable dataset
- Random selection of calming responses
- Interactive command-line interface
- Strike system with temporary banning mechanism
- Configurable ban duration and maximum strikes

## How It Works
The agent uses a simple yet effective approach:
1. Loads a predefined dataset of offensive words (supports both PKL and text formats)
2. Monitors incoming messages
3. Checks messages against the offensive words database
4. Tracks user strikes for repeated offenses
5. Issues temporary bans after maximum strikes are reached
6. Responds with appropriate calming messages when offensive content is detected

## Usage
```python
from offense_handling_agent import OffenseHandlingAgent

# Create an instance of the agent
agent = OffenseHandlingAgent()

# Run the interactive chat
agent.run()
```

## Customization
- Add or modify offensive words in `datasets/default` or create a custom PKL dataset
- Customize calming responses by modifying `datasets/calm_response`
- Adjust ban duration and maximum strikes in `main.py`

## File Structure
- `main.py`: Contains the core `OffenseHandlingAgent` class implementation
- `datasets/`
  - `default`: Text file containing the default list of offensive words
  - `calm_response`: Collection of calming responses
  - `offensive_words.pkl`: Optional PKL format dataset (if available)

## Configuration
Default settings in `OffenseHandlingAgent`:
- Maximum strikes: 3
- Ban duration: 24 hours
- Supports both PKL and text-based datasets

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
