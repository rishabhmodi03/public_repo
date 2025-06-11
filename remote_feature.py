
from interaction_generator import generate_response
from utils_for_lambda import send_followup_message

def my_slash_command(interaction_data):
    token = interaction_data["token"]
    app_id = interaction_data["application_id"]
    send_followup_message(token, content="Follow-up from remote!", ephemeral=True)
    return generate_response(content="Hello from remote slash!", ephemeral=True)

def my_button_handler(interaction_data):
    return generate_response(content="Remote button clicked!", ephemeral=True)

FEATURE_ADD_HANDLER = {
    "slash_commands": {
        "remote_hello": "my_slash_command"
    },
    "button_interactions": {
        "remote_btn_": "my_button_handler"
    }
}
