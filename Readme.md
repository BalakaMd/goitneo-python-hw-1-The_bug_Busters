# Simple Contact Manager

This project is a simple assistant bot for managing your contact list via the command line. You can add, change, and retrieve phone numbers of your contacts.

## Usage

1. **Add a contact:**
   ```bash
   add <name> <phone number>
   ```
   Example:
   ```bash
   add John Doe 123-456-7890
   ```

2. **Change a contact:**
   ```bash
   change <name> <new phone number>
   ```
   Example:
   ```bash
   change John Doe 987-654-3210
   ```

3. **Get a phone number:**
   ```bash
   phone <name>
   ```
   Example:
   ```bash
   phone John Doe
   ```

4. **Get all phone numbers:**
   ```bash
   all
   ```

5. **Exit the program:**
   ```bash
   close
   ```
   Or
   ```bash
   exit
   ```

6. **Help:**
   ```bash
   help
   ```

## Dependencies

- Python 3.x

## How to Run

```bash
python assistant_bot.py
```

__________
__________
__________
# Birthday Reminder

This simple Python script helps you keep track of upcoming birthdays. It takes a list of users with their names and birthdays, then prints a list of people who have birthdays in the next week, grouped by day.

## Usage

1. **Define Users:**
   Modify the `users_dict` list in the script to include the names and birthdays of the people you want to track.

   Example:
   ```python
   users_dict = [
       {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
       {"name": "Tom Cruise", "birthday": datetime(1962, 7, 3)},
       {"name": "Robert John Downey Jr.", "birthday": datetime(1965, 12, 4)},
       {"name": "Tom Hanks", "birthday": datetime(1965, 12, 3)}
   ]
   ```

2. **Run the Script:**
   Execute the script to see upcoming birthdays for the next week.

   ```bash
   python birthday_reminder.py
   ```

## Output

The script prints a list of people who have birthdays in the next week, grouped by day.

Example:
```
Monday ['03/12-->Robert John Downey Jr.', '03/12-->Tom Hanks']
Wednesday ['28/10-->Bill Gates']
Thursday ['04/07-->Tom Cruise']
```

## Dependencies

- Python 3.x

## Notes

- Ensure that the `datetime` module is available in your Python environment.

GitHub: [BalakaMd](https://github.com/BalakaMd)
