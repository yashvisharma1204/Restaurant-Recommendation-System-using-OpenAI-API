# Restaurant Recommendation System

This project demonstrates how to extract structured information from unstructured text data and generate restaurant suggestions using OpenAI's GPT-3.5 Turbo API. It combines text processing, data extraction, and AI-based suggestions to create a personalized restaurant recommendation system.

## Table of Contents
- [Background](#background)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Background

The aim of this project is to build a system that suggests restaurants to users based on their favorite food, restaurant, and city. We utilize OpenAI's GPT-3.5 Turbo model to extract information from raw text data and generate relevant restaurant suggestions.

## Project Structure

- `Food Data.txt`: A text file containing raw food-related information.
- `extract_data.py`: Python script to extract structured data from raw text.
- `generate_suggestions.py`: Python script to generate restaurant suggestions based on extracted information.
- `requirements.txt`: File with a list of Python packages required for this project.
- `README.md`: This documentation file.

## Installation and Setup

### Prerequisites

Ensure that you have Python 3.7 or higher installed on your system. Also, you need an OpenAI account with access to the GPT-3.5 Turbo API and an API key.

### Installing Dependencies

To install the required Python packages, use the following command:

```bash
pip install -r requirements.txt
```

### API Key Configuration

Before running the scripts, make sure to configure your OpenAI API key. You can set it as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Alternatively, you can hard-code the key in the script files (not recommended for security reasons).

## Usage

### Data Extraction

To extract structured data from the text file, run `extract_data.py`:

```bash
python extract_data.py
```

This script reads the raw text data, extracts information like name, favorite food, favorite restaurant, city, and monthly spending, and outputs a structured DataFrame.

### Generate Suggestions

To generate restaurant suggestions based on the extracted data, run `generate_suggestions.py`:

```bash
python generate_suggestions.py
```

This script uses OpenAI's GPT-3.5 Turbo model to generate suggestions for each row in the DataFrame and appends the suggestions to the DataFrame.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvement or additional features, please create a pull request or open an issue on GitHub.

### Guidelines

- Please follow standard GitHub conventions for pull requests.
- Include appropriate comments and documentation with your code changes.
- Ensure that your code passes any linting or test checks.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software, provided that you include the original license text.
