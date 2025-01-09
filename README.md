# Password Manager

## Video Demo

[Watch here](https://youtu.be/q9rLYTkUc1E)

## Description

The **Password Manager** is a lightweight and intuitive application designed to help users securely store and manage their credentials across various platforms. With the growing need for multiple accounts on different websites and services, keeping track of usernames and passwords can be challenging. This tool provides a centralized way to organize and retrieve credentials effortlessly, ensuring convenience and security.

### Key Features

- **Add New Credentials:**  
  Users can save usernames, passwords, and platform names securely in a local text file. The application ensures that duplicate entries are not added by validating against existing records.

- **Retrieve Specific Entries:**  
  Users can search for credentials by providing the associated username and platform name. The tool displays the corresponding password, making it easy to recover forgotten credentials.

- **List All Credentials:**  
  The application provides an option to view all stored username-password-platform combinations in a neatly formatted way. This feature is especially useful for reviewing all saved accounts at a glance.

- **Delete Credentials:**  
  Users can remove specific entries by providing the exact username, password, and platform name. This ensures that outdated or incorrect data can be easily managed.

### How It Works

1. **Graphical User Interface (GUI):**  
   The application uses Python's `tkinter` library to create an interactive and user-friendly GUI. Buttons and input fields are neatly organized, making the tool easy to navigate.

2. **Secure Data Storage:**  
   All credentials are stored in a local text file, with careful handling to avoid accidental overwrites or data loss. Duplicate checking prevents redundancy.

3. **Error Handling:**  
   The application displays informative messages when users attempt invalid operations, such as adding duplicate entries or trying to retrieve non-existent credentials.

4. **Cross-Platform Compatibility:**  
   Built in Python, the tool is compatible with multiple operating systems, including Windows, macOS, and Linux.

### Usage Scenarios

- **Personal Use:**  
  Keep track of login credentials for social media, email, and other accounts.

- **Workplace Applications:**  
  Store and organize passwords for internal tools and platforms securely.

- **Temporary Credential Management:**  
  Quickly save and retrieve temporary passwords for one-time use cases.

### Future Enhancements

- **Encryption:**  
  Add functionality to encrypt stored passwords for enhanced security.

- **Cloud Integration:**  
  Provide an option to sync credentials with cloud storage for access across multiple devices.

- **Advanced Search:**  
  Implement filters to search by partial usernames or platforms.

### Why Use This Tool?

In an age where digital accounts are ubiquitous, having a dedicated tool to manage passwords is essential. The **Password Manager** simplifies this process, offering a reliable solution for storing and retrieving credentials without relying on third-party services or subscription-based password managers.

---

**Note:** This project is a demonstration of how Python and `tkinter` can be used to build simple yet functional desktop applications. Users are advised to add encryption or other security measures if used for sensitive data.
