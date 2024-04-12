import json
from transformers import AutoModelForCausalLM, AutoTokenizer

class AIStoryManager:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        self.tokenizer = None

    def load_model(self):
        if self.model is None or self.tokenizer is None:
            try:
                self.model = AutoModelForCausalLM.from_pretrained(self.model_path)
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            except Exception as e:
                print(f"Error loading model: {e}")

    def generate_response(self, template, story_segments):
        self.load_model()  # Lazy loading of model and tokenizer
        if self.model is not None and self.tokenizer is not None:
            ai_response = template.format(
                description=self.generate_description(),
                sight_touch_feel=self.generate_sight_touch_feel(),
                **story_segments,
                option1=self.generate_option(),
                option2=self.generate_option(),
                option3=self.generate_option()
            )
            return ai_response

    def generate_sight_touch_feel(self):
        return "You can feel the cool breeze and hear the rustling leaves..."

    def generate_option(self):
        return "Action: Pro - ... Con - ..."

# mMdel path using 7b model rn
model_path = r'C:\Users\kasim\Documents\programs\mmoi\Wizard-Vicuna-7B-Uncensored-GPTQ'

# Initialize the ai story manager
ai_manager = AIStoryManager(model_path)

# Story data file path 
story_data_file = 'story_data.json'

# Load story data here
def load_story_data(story_data_file):
    try:
        with open(story_data_file, 'r') as file:
            story_data = json.load(file)
        return story_data
    except Exception as e:
        print(f"Error loading story data: {e}")
        return {}

# Template for ai to follow hopefully
template = (
    "<Description (2 paragraphs)>\n{description}\n\n"
    "<Sight, Touch and feel and other senses if need be for realism>\n{sight_touch_feel}\n\n"
    "<3 Options with a line of description and a pro and a con>\n{option1}\n{option2}\n{option3}\n\n"
    "<Gem System>\n{gem_system}\n\n"
    "<Status Window>\n{status_window}"
)


# Generate response
response = ai_manager.generate_response(template, story_segments)
print(response)
print("ran")