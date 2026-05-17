# Python Automation and Mini Projects

This repository contains a collection of beginner-friendly Python scripts. The projects cover command-line programs, games, file hashing, API usage, computer vision, audio recording, and simple automation.

## Projects

| File | Description | Main Technology / Libraries |
| --- | --- | --- |
| `checking_two_pdfs_are_same.py` | Compares two PDF files by generating SHA-256 hashes and checking whether both hashes match. | Python standard library, `hashlib` |
| `expense_tracker.py` | A command-line expense tracker that lets users add expenses, view all expenses, and calculate the total amount. | Python basics, lists, tuples, loops, user input |
| `hiding_treasure_game.py` | A small grid-based treasure hiding game where the user selects a position and the script marks it with `x`. | Python lists, indexing, string handling |
| `love_calculator_game.py` | Calculates a fun compatibility score by counting letters from the words `TRUE` and `LOVE` in two names. | Python strings, conditionals, input handling |
| `motion_detection_camera.py` | Uses the webcam to detect motion by comparing video frames and drawing rectangles around moving areas. | `opencv-python` / `cv2`, computer vision |
| `password_generator.py` | Generates a random password using letters, digits, and punctuation based on the length entered by the user. | Python standard library, `random`, `string` |
| `pizza_delivery_system.py` | Simple command-line pizza ordering system that calculates the total price based on pizza type and quantity. | Python conditionals, arithmetic, input handling |
| `rock_paper_scissors.py` | Rock-paper-scissors game where the user plays against the computer. | Python standard library, `random` |
| `voice_recorder.py` | Records audio for 5 seconds and saves it as WAV files. | `sounddevice`, `scipy`, `wavio` |
| `weather_app.py` | Fetches current weather details for a city using the OpenWeatherMap API. | `requests`, REST API, JSON |
| `whatsapp_birthdaybot.py` | Schedules WhatsApp birthday messages for saved contacts. | `pywhatkit`, `time`, automation |

## Technologies Used

- **Python**: Core programming language used for all scripts.
- **Command-line input/output**: Most scripts use `input()` and `print()` for user interaction.
- **File handling**: Used in the PDF comparison script to read files in binary mode.
- **Hashing**: `hashlib` is used to generate SHA-256 hashes for PDF comparison.
- **Randomization**: `random` is used for password generation and game logic.
- **String handling**: Used in games, password generation, and user input processing.
- **Computer vision**: `opencv-python` is used for webcam-based motion detection.
- **Audio recording**: `sounddevice`, `scipy`, and `wavio` are used to record and save audio.
- **API integration**: `requests` is used to call the OpenWeatherMap API.
- **Automation**: `pywhatkit` is used to schedule WhatsApp messages.

## Requirements

Python 3 is required.

Install the external libraries with:

```bash
pip install opencv-python requests sounddevice scipy wavio pywhatkit
```

The following modules are part of Python's standard library and do not need separate installation:

- `hashlib`
- `random`
- `string`
- `time`

## How to Run

Run any script with Python:

```bash
python filename.py
```

Examples:

```bash
python password_generator.py
python expense_tracker.py
python weather_app.py
```

## Notes

- `weather_app.py` requires an OpenWeatherMap API key. Replace `YOUR_API_KEY` with your actual API key before running it.
- `motion_detection_camera.py` requires webcam access.
- `voice_recorder.py` requires microphone access.
- `whatsapp_birthdaybot.py` requires WhatsApp Web login and valid phone numbers.
- `checking_two_pdfs_are_same.py` expects files named `pd1.pdf` and `pd2.pdf` in the same folder.
- `rock_paper_scissors.py` currently references `rock`, `paper`, and `scissors` variables, so these should be defined before running the game successfully.

## Future Improvements

- Add GUI versions using Tkinter.
- Improve the project structure by grouping related scripts into folders.
- Add database integration for projects such as the expense tracker.
- Deploy selected projects online.
- Add error handling and input validation.
- Add screenshots and sample outputs for each project.

## Screenshots

Screenshots can be added later for:

- Motion detector output
- Weather app output
- WhatsApp birthday bot output

## Repository Purpose

This repository showcases Python projects focused on automation, APIs, computer vision, and problem-solving.

## Author

Nirmal Roy  
B.Tech Computer Science Engineering Student  
GitHub: [github.com/nirmalroy123](https://github.com/nirmalroy123)
