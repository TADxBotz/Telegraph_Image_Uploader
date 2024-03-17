<h1>Telegram Image Uploader Bot</h1>

<p>This Telegram bot allows users to upload images, which are then automatically uploaded to Te.legra.ph, providing direct links to the uploaded images. The bot also welcomes users with a personalized message and an image when they start a chat.</p>

<h2>Table of Contents</h2>

<ul>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#dependencies">Dependencies</a></li>
  <li><a href="#heroku">Hosting on Heroku</a></li>
  <li><a href="#docker">Hosting on VPS with Docker</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#acknowledgements">Acknowledgements</a></li>
</ul>

<h2 id="installation">Installation</h2>

<p>To use this bot, follow these steps:</p>

<ol>
  <li>Clone this repository to your local machine:</li>
</ol>

<pre><code>git clone https://github.com/TADxBotz/Telegraph_Image_Uploader
</code></pre>

<ol start="2">
  <li>Install the required Python libraries:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="3">
  <li>Set up your Telegram bot token and image path in <code>config.py</code>.</li>
  <li>Run the bot script:</li>
</ol>

<pre><code>python main.py
</code></pre>

<h2 id="usage">Usage</h2>

<ul>
  <li>Start a chat with the bot on Telegram.</li>
  <li>Send an image to upload it to Telegraph.</li>
  <li>Receive direct links to the uploaded image.</li>
</ul>

<h2 id="features">Features</h2>

<ul>
  <li>Upload images to Telegraph and get direct links.</li>
  <li>Personalized welcome message with an image.</li>
  <li>Supports only image file types.</li>
</ul>

<h2 id="dependencies">Dependencies</h2>

<ul>
  <li><a href="https://github.com/eternnoir/pyTelegramBotAPI">Telebot</a>: Python library for interacting with the Telegram Bot API.</li>
  <li><a href="https://docs.python-requests.org/en/latest/">Requests</a>: HTTP library for making requests in Python.</li>
</ul>

<h2 id="heroku">Hosting on Heroku</h2>

<p>To host the bot on Heroku, follow these steps:</p>

<ol>
  <li>Create a Heroku account if you don't have one already.</li>
  <li>Install the Heroku CLI on your machine.</li>
  <li>Login to Heroku via the CLI using <code>heroku login</code>.</li>
  <li>Set up your project for deployment (e.g., create a Procfile, requirements.txt, etc.).</li>
  <li>Push your code to a Heroku Git remote.</li>
  <li>Scale your app using the Heroku dashboard or CLI.</li>
</ol>

<p>For detailed instructions, refer to the official <a href="https://devcenter.heroku.com/categories/deployment">Heroku Documentation</a> for deploying and scaling applications.</p>

<h2 id="docker">Hosting on VPS with Docker</h2>

<p>To host the bot on a VPS using Docker, follow these steps:</p>

<ol>
  <li>Install Docker on your VPS by following the official documentation for your operating system.</li>
  <li>SSH into your VPS and clone the bot repository:</li>
</ol>

<pre><code>git clone https://github.com/your-username/telegram-image-uploader-bot.git
</code></pre>

<ol start="3">
  <li>Build the Docker image:</li>
</ol>

<pre><code>docker build -t telegram-bot .
</code></pre>

<ol start="4">
  <li>Run the Docker container:</li>
</ol>

<pre><code>docker run -d --name telegram-bot-container telegram-bot
</code></pre>

<h2 id="contributing">Contributing</h2>

<p>Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.</p>

<h2 id="license">License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

<h2 id="acknowledgements">Acknowledgements</h2>

<p>Special thanks to the developers of Telebot and Requests for their excellent libraries.</p>
