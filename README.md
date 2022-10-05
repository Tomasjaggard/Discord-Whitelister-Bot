# Discord Whitelister Bot
This bot is designed to allow users to call a "/whitelist" command to privately enter and store their wallet address in a csv file, accessible by the bot host.

## Setup & Installation

### Setting up the bot
To create the bot which you intend to utilise the code, head to the [Discord Developer Portal](https://discord.com/developers/) and create a new application.
Set the desired **Name**, **Image** and **Description**.

![image](https://user-images.githubusercontent.com/81049049/194106712-01729fe7-5ad9-40b6-b7c7-a9cf2a3791e2.png)

Go to **OAuth2->URL Generator** setting and enable **Bot** in the upper section & **Send messages** in the lower section. This will generate a link at the bottom of the page, enter this into your browser and you'll receive a prompt to add the bot to your server.

![image](https://user-images.githubusercontent.com/81049049/194107526-cd9a9c81-d667-4155-9801-131e8ccd259d.png)

Now that the bot is in your server, go to the **Bot** setting and generate a token. Save this as it will be used later on. **(Do not share this token, as anyone who has access to it can control your bot.)**

![image](https://user-images.githubusercontent.com/81049049/194106812-0ca8ae24-142c-414d-81eb-e0d3270136cf.png)

### Hosting the bot
Head to [Replit](https://replit.com/) and create an account, then hit the **+** in the top right corner and create a new python bot (type "Python" in Template). Once created, create both "main.py" and "webserver.py" in the files section, and copy across the code from both relevant files in this repository. Your files should look like this:

![image](https://user-images.githubusercontent.com/81049049/194103217-7d94ab2b-7f8d-459a-abee-d175047948ed.png)

On the left hand side, go to **"Secrets"** which is represented by a lock symbol. Create a new secret called **"DISCORD_BOT_SECRET"** and add the previously generated token.

![image](https://user-images.githubusercontent.com/81049049/194107887-39ad7d0e-4798-4813-a81e-b7d94f0d5370.png)

Add a new file called **"data.csv"** and by default add "Username, Wallet address" as the first line. **(NOTE: Current version requires 1 entry into the csv file to work).**
Once completed press "Run" at the top of the page, this will set up the bot and you should see the bot go from Offline to Online in your server.

### Hosting the bot 24/7

To easily host your bot 24/7, create an account on [UptimeRobot](https://uptimerobot.com/), once created add a new monitor using the "Add New Monitor" button in the top left of the page.

![image](https://user-images.githubusercontent.com/81049049/194108586-b8edbec6-d6d9-4915-88f4-80af819f6477.png)

Select the Monitor type as "HTTP(s)" and then to get the URL, go back to your Replit application and copy the URL that it generates in the Webview tab. Once those are selected, press "Create Monitor" (There may be a popup about free/paid versions).

![image](https://user-images.githubusercontent.com/81049049/194109382-8d6ddd80-f267-4194-9d33-d0ba1628cb23.png)

## Future implementation

-allow users to edit their wallet address inside the csv file to reduce administration time.

-allow users to check their wallet address inside the csv file.
