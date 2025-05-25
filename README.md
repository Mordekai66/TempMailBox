# Temporary Mail App

Temporary Mail App is a Python application that provides disposable email addresses with a user-friendly Tkinter GUI. It allows users to generate temporary email accounts and receive emails.

## Features

- Generate temporary email addresses instantly
- Receive emails in real-time
- Clean and intuitive GUI interface
- View email content directly in the app
- Simple setup and easy to use

## How It Works

1. The user clicks "Generate New Email" to create a temporary email address
2. The application connects to the MailTM service to register the new address
3. When "Start Listening" is clicked, the app begins monitoring for incoming emails
4. Received emails are displayed in the activity log
5. The user can view email contents directly in the application

## Usage

1. Run `main.py` to launch the application
2. Click "Generate New Email" to create a temporary address
3. Use this address to receive emails from any service
4. Click "Start Listening" to begin receiving emails
5. View incoming emails in the activity log

## Future Plans

- Add support for email attachments handling
- Implement email forwarding capabilities
- Add email composition functionality
- Support for multiple temporary email accounts
- Include email filtering options
- Add notification system for new emails

## Requirements

- Python 3.x
- Required packages:
  - `mailtm`
  - `tkinter`

Install requirements with:
```python
pip install mailtm
```

## Repository Structure
```bash
TempMailApp/
├── main.py              # Main application launcher
├── README.md            # This documentation file
├── mail_logic.py        # Core email handling functionality
├── LICENSE              # LICENSE
└── gui.py               # Tkinter GUI implementation

```

## Contribution
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting
If you encounter issues:

Ensure you have an active internet connection

Verify all required packages are installed

Confirm the MailTM service is operational
