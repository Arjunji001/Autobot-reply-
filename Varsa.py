{
    "name": "Nursing Nation Bot",
    "description": "Conversation Bot.",
    "logo": "",
    "keywords": [
        "telegram",
        "Conversation Bot",
        "bot"
    ],
    "repository": "https://github.com/Arjunji001",
    "website": "",
    "success_url": "https://t.me/Nursing_Nation_bot",
    "env": {
        "API_HASH": {
            "description": "Your API HASH from my.telegram.org",
            "value": ""
        },
        "API_ID": {
            "description": "Your API ID from my.telegram.org",
            "value": ""
        },
        "BOT_TOKEN": {
            "description": "Bot token, get it from @BotFather.",
            "value": ""
        },
        "SESSION": {
            "description": "Pyrogram string session.",
            "value": ""
        },
        "AUTH": {
            "description": "User ID of Bot owner.",
            "value": ""
        },
        "FORCESUB": {
            "description": "Username name of public channel without using '@'.",
            "value": "https://t.me/testbotdrive"
        }
    },
    "buildpacks": [
        {
            "url": "heroku/python"
        },
        {
            "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git"
        }
    ]
}
