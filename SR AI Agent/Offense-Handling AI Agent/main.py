import random


class OffenseHandlingAgent:
    def __init__(self):
        self.offensive_words = self.generate_offensive_words()

    def handle_offense(self, message):
        """
        Checks if a message contains offensive words and responds accordingly.
        """
        words = message.lower().split()
        if any(word in words for word in self.offensive_words):
            return self.calming_response()
        return "Thank you for keeping the chat positive! 😊"
    
    def generate_offensive_words(self):
        """
        Generates a list of offensive words based on the dataset.
        (you can expand this by adding more words to the dataset file)
        """
        with open('dataset', 'r') as file:
            offensive_words = [line.strip().lower() for line in file.readlines()]

        return offensive_words
    
    def calming_response(self):
        """
        Returns a random calming response.
        """
        # Predefined calming responses
        calming_responses = [
            "Let's keep things positive! 😊",
            "Everyone deserves respect. Let's be kind!",
            "I understand, but let's try to stay calm.",
            "Words can hurt, so let's use them wisely.",
            "Let's take a deep breath and be kind!",
            "Let's focus on positivity and kindness.",
            "Please be kind to each other. 😊",
            "Let's keep the conversation respectful and positive.",
            "Kindness goes a long way. Let's spread it!",
            "Let's focus on what unites us, not what divides us.",
            "Let's be the change we want to see in the world.",
            "Let's keep the chat positive and uplifting!",
            "Let's be kind and understanding towards each other.",
            "Be kind or you will be banned",
        ]
        return random.choice(calming_responses)
    
    def run(self):
        """
        Runs an interactive loop where the user can input messages and the agent responds.
        """
        while True:
            message = input("Enter a message: ")
            if message.lower() == 'exit':
                break
            response = self.handle_offense(message)
            print(f"AI Agent: {response}")
            print("\n")

        print("Exiting the program.")


if __name__ == "__main__":
    agent = OffenseHandlingAgent()
    agent.run()