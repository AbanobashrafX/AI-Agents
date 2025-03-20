## Offense-Handling AI Agent
A Python-based AI agent that monitors and responds to offensive language in chat messages, promoting a positive and respectful communication environment.
### Features
- Real-time message monitoring- Offensive word detection using a customizable dataset
- Random selection of calming responses- Interactive command-line interface
### How It Works
The agent uses a simple yet effective approach:
1. Loads a predefined dataset of offensive words
2. Monitors incoming messages3. Checks messages against the offensive words database
4. Responds with appropriate calming messages when offensive content is detected
### Usage
```python
from offense_handling_agent import OffenseHandlingAgent
# Create an instance of the agent
agent = OffenseHandlingAgent()
# Run the interactive chat
agent.run()
```
### Customization
- Add or modify offensive words in the `dataset` file- Customize calming responses by modifying the `calming_responses` list in `main.py`
### File Structure
- `main.py`: Contains the core `OffenseHandlingAgent` class implementation
- `dataset`: Text file containing the list of offensive words
### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.