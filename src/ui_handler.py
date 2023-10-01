# Manages all UI-related functionalities, such as input forms, display screens, and user interactions (using Tkinter or other relevant libraries).
def get_user_input():
    """
    Fetches user inputs: category and note text.

    :return: tuple (str, str), containing the category and note text
    """
    print("Select a category:")
    print("1 - Story Ideas")
    print("2 - Garden Observations")
    print("3 - Beeper Ideas")
    print("4 - Workout Observations")
    
    category_mapping = {
        "1": "Story Ideas",
        "2": "Garden Observations",
        "3": "Beeper Ideas",
        "4": "Workout Observations",
    }

    category_option = input("Enter the number associated with a category: ")
    category = category_mapping.get(category_option, "Uncategorized")
    
    note_text = input("Enter your note: ")

    return category, note_text

def confirm_send_email(formatted_note):
    """
    Displays the formatted note for user confirmation before sending the email.

    :param formatted_note: str, the formatted note text
    :return: bool, True if user confirms, False otherwise
    """
    print("\n--- Preview Note ---")
    print(formatted_note)
    print("--------------------")

    while True:
        user_confirm = input("Send this note? (yes/no): ").strip().lower()
        if user_confirm in ['yes', 'no']:
            return user_confirm == 'yes'

# Example Usage
if __name__ == "__main__":
    category, note_text = get_user_input()
    # Simulate a formatted note for demo
    formatted_note = f"Category: {category}\nNote: {note_text}\nTimestamp: 2023-09-30 15:45:00\n"
    
    if confirm_send_email(formatted_note):
        print("Confirmed! Note will be sent.")
    else:
        print("Cancelled. Note will not be sent.")
