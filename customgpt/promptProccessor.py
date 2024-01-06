import google.generativeai as genai
from .CONSTANTS import SAFETY_SETTINGS,GENERATION_CONFIG, ERROR_HTML_MESSAGE, FINISH_REASONS
import markdown

genai.configure(api_key="AIzaSyDJh8_wuIZgIxXPqV3qXq7uKNzmptDfAOU")

# Set up the model
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=GENERATION_CONFIG,
                              safety_settings=SAFETY_SETTINGS)


def evaluateFinishReason(finishReasonCode):
    if finishReasonCode == 1:
        return True
    else:
        return False
    
def returnFinishReasonAbruptionText(finishReasonCode):
    ERROR_HTML = ERROR_HTML_MESSAGE
    ERROR_HTML = ERROR_HTML.replace("Here comes error message",FINISH_REASONS[finishReasonCode])
    return ERROR_HTML

    
def processPromptInput(prompt):
    response = model.generate_content(prompt)
    if(evaluateFinishReason(response.candidates[0].finish_reason)):
        responseJSON = {"message" : markdown.markdown(response.text)}
    else:
        responseJSON = {"message" :returnFinishReasonAbruptionText(response.candidates[0].finish_reason)}
    return responseJSON


print(processPromptInput("Provide me santhosakke song lyrics"))

