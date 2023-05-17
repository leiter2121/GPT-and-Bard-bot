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

## Get an OpenAI API Key

Step 1: Go to the OpenAI Website
Open your preferred web browser and navigate to the OpenAI website. You can visit the official website by entering the following URL into the browser's address bar: https://www.openai.com/

Step 2: Sign in or Sign up
If you already have an OpenAI account, click on the "Sign In" button in the top-right corner of the OpenAI website and enter your credentials (email address and password) to sign in. Otherwise, click on the "Get started" button or the "Sign up" link to create a new account. Follow the instructions provided to complete the signup process.

Step 3: Navigate to the API section
Once you have signed in to your OpenAI account, navigate to the API section. You can typically find it in the main navigation menu or by searching for "API" on the OpenAI website.

Step 4: Review API Documentation
Before obtaining an API key, it's recommended to review the OpenAI API documentation. Familiarize yourself with the available endpoints, capabilities, and any associated usage guidelines or pricing details. This information will help you make the most of the API.

Step 5: Apply for OpenAI API Access
To use the OpenAI API, you may need to apply for access. Some services, such as the GPT-3.5 language model, might require specific permissions or enrollment. Follow the instructions on the API page to apply for the necessary access.

Step 6: Obtain your API Key
Once your application for API access has been approved, you will receive an API key. This key is unique to your OpenAI account and allows you to authenticate and make requests to the OpenAI API. Typically, the API key is provided in your account settings or sent to you via email. Make sure to keep your API key secure and avoid sharing it publicly.

Step 7: Start Using OpenAI API
With your API key in hand, you can now integrate OpenAI's language models and services into your applications. Consult the OpenAI API documentation for details on how to authenticate requests and utilize the available endpoints.

Step 8: Optional - GitHub Integration
If you plan to use the OpenAI API with GitHub repositories, you can create a new repository or navigate to an existing repository on GitHub. Follow the appropriate GitHub documentation to set up your repository and integrate OpenAI functionality into your codebase.

Step9: Plug in your OpenAI API Key into the test_fight.py script.

Additional Notes:

OpenAI provides comprehensive documentation, including code examples and guides, to help you get started with their API. Make sure to refer to the official OpenAI documentation for detailed instructions and best practices.
Familiarize yourself with OpenAI's usage policies and any rate limits associated with your API key to ensure compliance and avoid unexpected charges.
If you encounter any issues during the API key acquisition process or while using the OpenAI API, refer to the OpenAI documentation or contact OpenAI support for assistance.
Disclaimer:
This README file serves as a general guide for obtaining an OpenAI API key. The process may change over time, so it's always recommended to refer to the official OpenAI documentation and resources for the most up-to-date instructions.

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

Step 9: Insert your AWS ID, AWS Region, and AWS Seceret Keys into the speak_text.py, and speak_text2.py.

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

5. Set your AWS Keys by replace the vaules in the `speak_text.py` and `speak_text2.py` scripts.

6. Run the script using the following command:

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
