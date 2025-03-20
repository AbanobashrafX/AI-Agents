import pickle
import random
from time import time


class OffenseHandlingAgent:
    """Offense Handling AI Agent"""

    def __init__(self):
        self.offensive_words = self.load_OW_dataset()
        self.calming_responses = self.load_responses()
        self.strikes = 0
        self.max_strikes = 3
        self.banned = False
        self.ban_duration = 24  # in hours
        self.ban_end_time = None

    def load_OW_dataset(self):
        """Loads offensive words from PKL dataset or default dataset"""
        try:
            # Fix the path to use forward slashes and relative path
            with open("datasets/offensive_words.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            # Fallback to default dataset if PKL file doesn't exist
            with open("datasets/default", "r", encoding="utf-8") as file:
                return [line.strip().lower() for line in file.readlines()]

    def load_responses(self):
        """Loads calming responses from text file"""
        with open("datasets/calm_response", "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    def ban(self, ban_reason):
        """
        Bans the user for a specified duration.
        """
        self.banned = True
        self.ban_end_time = time() + self.ban_duration * 3600
        ban_message = f"""
        You have been banned for {self.ban_duration} hours.
        Reason: {ban_reason}
        Please be aware that using {ban_reason} is not allowed.
        Please be respectful in future conversations.
        """
        return ban_message

    def handle_offense(self, message):
        """
        Checks if a message contains offensive words and responds accordingly.
        Now supports different character sets and word boundaries.
        """
        message = message.lower()
        # Handle different word boundaries
        for word in self.offensive_words:
            if word in message:
                self.strikes += 1
                if self.strikes >= self.max_strikes:
                    return self.ban(word)
                else:
                    return random.choice(self.calming_responses)
        return "Thank you for keeping the chat positive! 😊"

    def run(self):
        """
        Runs an interactive loop where the user can input messages and the agent responds.
        """
        while True:
            message = input("Enter a message: ")
            if message.lower() in ["exit", "quit"]:
                break
            if self.banned:
                print("You are banned. Please wait until the ban expires.")
                continue
            response = self.handle_offense(message)
            print(f"AI Agent: {response}")

        print("Exiting the program.")


if __name__ == "__main__":
    agent = OffenseHandlingAgent()
    agent.run()
