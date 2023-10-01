# Manages the creation, handling, and formatting of metadata for notes and emails.
from datetime import datetime

def get_current_timestamp():
    """
    Returns the current date and time as a formatted string.

    Example: "2023-09-30 15:45:00"
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def format_note(category, note_text):
    """
    Formats the note with metadata.

    :param category: str, category of the note
    :param note_text: str, user's input note
    :return: str, formatted note with metadata
    """
    timestamp = get_current_timestamp()
    formatted_note = f"Category: {category}\nTimestamp: {timestamp}\nNote: {note_text}\n"
    return formatted_note

# Example Usage
if __name__ == "__main__":
    # Sample category and note
    sample_category = "Story Ideas"
    sample_note = "Explore the concept of time travel in the next sci-fi short story."

    formatted_note = format_note(sample_category, sample_note)
    print(formatted_note)
