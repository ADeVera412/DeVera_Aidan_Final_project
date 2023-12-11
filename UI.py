import pygame as pg
import sys
import openai

WIDTH = 800
HEIGHT = 600

pg.init()
openai.api_key = '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'  # Replace with your OpenAI API key

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class UI:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.font.init()
        self.input_text = ""
        self.messages = []

        self.BACKGROUND_COLOR = BLACK
        self.TEXT_COLOR = WHITE
        self.FONT_SIZE = 19

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Chatbot UI")

    def get_chatbot_response(self, user_input):
        try:
            # Call OpenAI GPT-3.5-turbo for a response
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                temperature=0.7,
                max_tokens=150,
                n=1
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}"

    def run(self):
        clock = pg.time.Clock()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        # Append input_text to messages when Enter key is pressed
                        user_input = self.input_text
                        self.messages.append(f"You: {user_input}")

                        # Get response from the chatbot
                        bot_response = self.get_chatbot_response(user_input)
                        self.messages.append(f"Bot: {bot_response}")

                        self.input_text = ""

                    elif event.key == pg.K_BACKSPACE:
                        # Remove the last character from input_text when Backspace key is pressed
                        self.input_text = self.input_text[:-1]
                    elif event.unicode.isprintable():
                        # Append the pressed character to input_text
                        self.input_text += event.unicode

            # Draw background
            self.screen.fill(self.BACKGROUND_COLOR)

            # Draw messages
            y = 10
            for message in self.messages:
                text_surface = pg.font.Font(None, self.FONT_SIZE).render(message, True, self.TEXT_COLOR)
                self.screen.blit(text_surface, (10, y))
                y += self.FONT_SIZE + 5

            # Draw input text
            input_surface = pg.font.Font(None, self.FONT_SIZE).render(self.input_text, True, self.TEXT_COLOR)
            self.screen.blit(input_surface, (10, HEIGHT - 30))

            # Update the display
            pg.display.flip()

            # Cap the frame rate
            clock.tick(30)

if __name__ == "__main__":
    ui = UI()
    ui.run()