Objective This Python project allows users to generate secure, random passwords based on customizable criteria, such as: • Desired password length • Inclusion of letters, digits, and special characters • Number of passwords to generate • Optionally saving passwords to a file

Tools & Libraries Used random-Random selection of characters string-Predefined sets of letters, digits, symbols datetime-Timestamped file naming

Steps Performed

User Input o Takes the desired password length. o Asks whether to include:  Letters (a-z, A-Z)  Digits (0-9)  Special characters (e.g., @#$%^&*) o Asks how many passwords to generate. o Option to save generated passwords to a text file.
Password Generation o Ensures at least one character from each selected type is included. o Randomly fills the remaining length from the combined pool. o Shuffles characters for enhanced randomness.
File Saving (Optional) o If opted in, saves passwords to a uniquely named .txt file using current date and time.
Displays Results o All generated passwords are displayed in the terminal.
Outcome • Dynamically generates strong, customizable passwords. • Guarantees character diversity per user choices. • Provides option to export passwords for future use.

Sample Output:

==== Password Generator==== Enter password length: 10

Select characters types to include: Include letters? (y/n): y Include digits? (y/n): y Include numbers? (y/n): y How many password to generate?: 3 Save passwords? (y/n): y Generated Password(s): d8&TgM9@3q L7^fN!2bZ9 #4RcD8v@Pq Passwords saved to passwords_20250613_145012.txt
