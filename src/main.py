# Serves as the entry point of the application, invoking UI and handling primary workflow logic.
import ui_handler
import metadata_handler
import email_handler
import chatgpt_api

def main():
    # 1. Capture input
    category, note_text = ui_handler.get_user_input()

    # 2. Generate metadata and format note
    formatted_note = metadata_handler.format_note(category, note_text)
    
    # 3. [Optional] Interact with ChatGPT API
    # enhanced_note = chatgpt_api.enhance_note_with_gpt(formatted_note)
    # (The function enhance_note_with_gpt needs to be defined in chatgpt_api.py based on your needs)
    
    # 4. Confirm and send email
    if ui_handler.confirm_send_email(formatted_note):  # Or enhanced_note if step 3 is used
        email_handler.send_email(formatted_note)  # Or enhanced_note if step 3 is used
        print("Note sent!")
    else:
        print("Note discarded.")

if __name__ == "__main__":
    main()
