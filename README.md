# MyDataScientistDays

Welcome to the Twitter data collection and processing project!

This project was created with the aim of collecting information on Terrorism in Northern Togo and processing it using data science techniques to extract the most useful keywords.

# Features

This project uses the `tweepy` library to collect tweets from Twitter. Tweets are stored in a JSON file and are processed using the `pandas` library.

Data processing includes the following steps:

Remove duplicate tweets

• `Tweets cleanup (removal of special characters, URLs, etc.)`

• `Sentiment analysis (using the textblob library)`

• `Extracting hashtags and mentions`

• `Results are stored in a CSV file for later use.`


# How to use this project

1. Clone the project on your computer:

`git clone https://github.com/your-username/data-science-twitter.git`

2. Install the required dependencies by running:

`pip install -r requirements.txt`

3. Create a config.py file containing the Twitter API keys:

`consumer_key = 'your_key'`

`consumer_secret = 'your_secret'`

`access_token = 'your_token'`

`access_token_secret = 'your_token_secret'`

4. Go to the file folder

`cd Twitter Data Gathering`

5. Run the `demo.py` file

`python demo.py` and follow the instructions.

The Tags used in this example are: `#togo#terrorism`

![Figure_1](https://user-images.githubusercontent.com/24190641/235856466-4064f517-e91f-4044-9894-0f36f9d50a79.png)

# Contributions

We are open to contributions and suggestions to improve this project. Feel free to create a pull request to add features or fix bugs.

# Licence

This project is licensed under the MIT license. See the LICENSE file for more details.


