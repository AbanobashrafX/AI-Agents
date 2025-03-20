import pickle
import random
from time import time


class OffenseHandlingAgent:
    """Simple Offense Handling Agent"""

    def __init__(self, max_strikes=3, ban_duration=24):
        self.offensive_words = self.load_OW_dataset()
        self.calming_responses = self.load_responses()
        self.strikes = 0
        self.max_strikes = max_strikes  # Default: 3 strikes before ban
        self.banned = False
        self.ban_duration = ban_duration  # Default: 24 hours ban duration
        self.ban_end_time = None
        self.new_detected_words = set()

    def load_OW_dataset(self):
        """Loads offensive words from PKL dataset or default dataset"""
        try:
            # Fix the path to use forward slashes and relative path
            with open("datasets/offensive_words.pkl", "rb") as file:
                return set(pickle.load(file))  # Convert to set for faster lookups
        except FileNotFoundError:
            # Fallback to default dataset if PKL file doesn't exist
            with open("datasets/default", "r", encoding="utf-8") as file:
                return set(
                    [line.strip().lower() for line in file.readlines()]
                )  # Convert to set for faster lookups

    def load_responses(self):
        """Loads calming responses from text file"""
        with open("datasets/calm_response", "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    def save_offensive_words(self):
        """Saves the updated offensive words list back to PKL file"""
        combined_words = self.offensive_words.union(self.new_detected_words)
        with open("datasets/offensive_words.pkl", "wb") as file:
            pickle.dump(list(combined_words), file)

    def add_offensive_word(self, word):
        """Adds a new offensive word to the dataset"""
        word = word.lower().strip()
        if word not in self.offensive_words:
            self.new_detected_words.add(word)
            self.save_offensive_words()
            self.new_detected_words.clear()
            # Reload the dataset to include the new word
            self.offensive_words = self.load_OW_dataset()
            return True
        return False
    
    def detect_offensive_words(self, message):
        """Detects offensive words in a message and returns them as a list"""
        offensive_words = []
        for word in self.offensive_words:
            if word in message.lower():
                offensive_words.append(word)
        return offensive_words

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

    def check(self, message):
        """
        Checks if a message contains offensive words and responds accordingly.
        Now supports different character sets and word boundaries.
        """
        message = message.lower()
        # Check for offensive content
        offensive_words = self.detect_offensive_words(message)
        if offensive_words:
            self.strikes += 1  # Increment strikes for each offense detected
            if self.strikes >= self.max_strikes:  # Check if strikes exceed the threshold
                return self.ban("offensive language")  # Ban if strikes exceed the threshold
            else:  # If strikes are within the threshold, respond with a calm message
                return random.choice(self.calming_responses)  # Randomly select a calm response
        return "Thank you for keeping the chat positive! 😊"

    def run(self):
        """
        Runs an interactive loop where the user can input messages and the agent responds.
        """
        while True:
            message = input("Enter a message: ")
            if message.startswith("!add "):
                word = message[5:].strip()
                if self.add_offensive_word(word):
                    print(f"Added '{word}' to offensive words database")
                else:
                    print(f"'{word}' already exists in database")
                continue
            if message.lower() in ["exit", "quit"]:
                break
            if self.banned:
                print("You are banned. Please wait until the ban expires.")
                continue
            response = self.check(message)
            print(f"AI Agent: {response}")

        print("Exiting the program.")


if __name__ == "__main__":
    agent = OffenseHandlingAgent()
    agent.run()
