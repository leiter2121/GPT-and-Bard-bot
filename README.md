# Powerful Conversation Bot

This powerful conversation bot script combines the cutting-edge capabilities of GPT-3.5 with the intelligent responses of Google Bard. Get ready to engage in dynamic and impressive conversations on any topic you desire!

## Features

- Integration with the state-of-the-art GPT-3.5 model for generating high-quality responses.
- Utilizes the sophisticated Google Bard API to obtain authoritative answers.
- Voice support for both GPT and Bard responses using Amazon Polly.
- Keyboard interrupt feature to gracefully exit the conversation.


## Requirements

Before using this script, please ensure you have the following:

- Python 3.7 or higher installed
- The `pickle` library
- The `bardapi` library
- The `openai` library
- The `keyboard` library
- The `speak_text` library
- The `speak_text2` library

## Get a Bard API Key
1. Go to this site, and follow the instructions. https://medium.datadriveninvestor.com/access-google-bard-easily-with-python-package-bard-api-6de77b39cd04
2. Insert the API Key into the test_fight.py script.

## Setup Amazon AWS Account for Polly Speech

Step 1: Go to the Amazon Polly Website
Open your preferred web browser and navigate to the Amazon Polly website. You can visit the official website by entering the following URL into the browser's address bar: https://aws.amazon.com/polly/

Step 2: Sign in to the AWS Management Console
To create an Amazon Polly account, you need to sign in to the AWS Management Console. If you already have an AWS account, enter your credentials (email address and password) and sign in. Otherwise, click on the "Create a new AWS account" button and follow the instructions to create a new account.

Step 3: Access the Amazon Polly Service
Once you have successfully signed in to the AWS Management Console, search for "Polly" in the search bar at the top of the page. Click on the "Amazon Polly" result to access the Polly service.

Step 4: Create a New Amazon Polly Account
On the Amazon Polly console, click on the "Get started with Amazon Polly" button or the "Try Amazon Polly Free" button to start the account creation process.

Step 5: Configure Account Settings
Follow the on-screen instructions to configure your Amazon Polly account. Provide the necessary details, such as your account name, contact information, and payment method. Review the terms and conditions, and click on the "Create Account and Continue" button.

Step 6: Verify Your Identity
As part of the account setup process, you may be required to verify your identity. This could involve providing additional information or entering a verification code sent to your registered email address or phone number.

Step 7: Complete the Setup
After verifying your identity, you'll need to review your account details and make any necessary changes. Once you're satisfied, click on the "Complete Account Setup" button to finalize the process.

Step 8: Start Using Amazon Polly
Congratulations! You have successfully created an Amazon Polly account. You can now start exploring the various features and capabilities of Amazon Polly. Refer to the official Amazon Polly documentation for more information on how to use the service and integrate it into your applications.

Additional Notes:

Amazon Polly offers a Free Tier that allows you to try the service with certain limitations. Make sure to review the Free Tier details and any associated costs on the Amazon Polly pricing page.
Remember to secure your Amazon Polly credentials and access keys to prevent unauthorized access to your account.
If you encounter any issues during the account setup process or while using Amazon Polly, refer to the official Amazon Polly documentation or contact Amazon Web Services support for assistance.
Disclaimer:
This README file is provided as a general guide for creating an Amazon Polly account. The process may vary or change over time, so it's always recommended to refer to the official documentation and AWS resources for the most up-to-date instructions.

## Setup

1. Clone this repository or download the script directly.

2. Install the required libraries by running the following command:

```shell
pip install pickle bardapi openai keyboard
```

3. Set the Bard API key by replacing the value of `os.environ['_BARD_API_KEY']` in the script with your own Bard API key.

4. Set your OpenAI API key by replacing the value of `openai.api_key` in the script with your own OpenAI API key.

5. Run the script using the following command:

```shell
test_fight.py
```

## Usage

1. After running the script, you will be prompted to enter a topic for the conversation bots.

2. Once you enter the topic, the powerful conversation bot will start generating impressive responses.

3. The conversation bot will initiate the conversation by presenting its opinion on the topic and the reasons behind it.

4. Engage in an aggressive conversation by listening to the bots converse with each other.

5. To interrupt the conversation and exit gracefully, press the 'q' key on your keyboard.

6. The bots will eventually change topic on their own.

## Limitations

- The power of this conversation bot depends on the quality of the responses generated by GPT-3.5 and the accuracy of information provided by Google Bard.

- The bot's responses might occasionally be biased or lack context, as it relies on pre-trained models and external data sources.

- It is recommended to review and verify the generated responses for critical and sensitive topics before accepting them as accurate information.

## Conclusion

Engage in dynamic and impressive conversations with the powerful conversation bot, powered by the fusion of GPT-3.5 and Google Bard. Explore a wide range of topics, challenge opinions, and delve into thought-provoking discussions. Let the bot ignite your curiosity and provide you with authoritative answers while experiencing the convenience of voice support and the ability to switch topics seamlessly. Get ready to immerse yourself in the world of intelligent conversation with this impressive script.
