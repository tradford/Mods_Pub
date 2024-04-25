from logMessage import logMessage as lm
import requests
import json

def msteam(channel, message, names):
    # Generate email and mentions for all names
    mentions = []
    mentions_text = ""
    for name in names:
     
        lname = name.split(" ")[1]
        fname = name.split(" ")[0]
        email = fname[0] + lname + "@domain.com"
        mention = {
            "type": "mention",
            "text": f"<at>{fname} UPN</at>",
            "mentioned": {
                "id": email,
                "name": name
            }
        }
        mentions.append(mention)
        mentions_text += f"<at>{fname} UPN</at>, "

    # Trim the trailing comma and space
    mentions_text = mentions_text[:-2]

    team = f"{channel}"
    payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "Medium",
                            "weight": "Bolder",
                            "text": "Scheduled Task Automated Alert!",
                            "wrap": True
                        },
                        {
                            "type": "TextBlock",
                            "text": f"Hi {mentions_text}, {message}",
                            "wrap": True
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.0",
                    "msteams": {
                        "entities": mentions
                    }
                }
            }]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(team, headers=headers, data=json.dumps(payload))
    lm(r'path', f"MS Teams response: {response.status_code} {response.reason}")
    lm(r'path', f"{message} \n")

# # Example usage with multiple names
# msteam('webhook', 'This is a test message', ['Name MkNamerson', 'Namey Lasters' ])