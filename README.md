# 🚀 Dynamics 365 Reverse Engineering Tool 🚀

This tool helps you reverse engineer the Dynamics 365 APIs to find endpoints and their respective parameters. This is particularly useful for debugging, development, or security purposes, as it allows you to trace all possible endpoints that contain a specified parameter.

## 🔧 Features

- **Data Fetching**: Extract data from the API based on certain parameters.
- **Blacklist Management**: Maintain a list of URLs to be ignored during data extraction.
- **Multi-threaded Request Processing**: Optimizes data extraction by sending multiple requests simultaneously.

## 🕹️ How It Works

### Using the Blacklist (Optional)

Populate a blacklist by using the `refill_blacklist` function. This function requires the API URL and Cookie, which are used to reduce search time in most scenarios.

### Finding Endpoints

Input a search parameter to find all possible endpoints. For example, if you input 'User' as the search parameter, you'll find all endpoints that contain 'User' (NOTE: It is case sensitive) , like:

- `https://yourcompany.sandbox.operations.eu.dynamics.com/Users`
- `https://yourcompany.sandbox.operations.eu.dynamics.com/UsersSetting`
- `https://yourcompany.sandbox.operations.eu.dynamics.com/BusinessUsers`

...and more.

### Searching Parameters in the Found Entities

Search for a specific parameter within each found endpoint. If the parameter is found inside the URL, it will save the URL under `/result`.

<img src="https://github.com/RokZ999/Dynamics-365-API-Reverse-Engineering-Tool/assets/71169333/d08a61de-479e-4915-ba33-ce39bc532a46" width="800" height="1000" />

## 🔧 Setup

Provide the following details:

1. **API URL:** The base URL for the Dynamics 365 API endpoints.
2. **Cookie:** A valid cookie for accessing the API.
3. **Search Param:** The string that will be searched for within the endpoints.
4. **Search Param in every found entity:** The string that will be searched for within each found entity.


## 🚀 Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### 📋 Prerequisites

You'll need to have the following installed:
- Python (version 3.11 or higher)

### 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/Dynamics-365-Reverse-Engineering-Tool.git
```
2. pip install -r requirements.txt
```bash
pip install -r requirements.txt
```
3. Run the program
```bash
python gui.py
```

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/Dynamics-365-Reverse-Engineering-Tool/issues). 


## 🌟 Show your support

Give a ⭐️ if this project helped you!
