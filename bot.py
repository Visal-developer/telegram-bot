from telethon import TelegramClient, events
from telethon.tl.types import PeerUser

# Telegram API credentials
api_id = 28210729
api_hash = '0dfa6e40e5da54025b30219bf9c15cdf'

client = TelegramClient('bot_session', api_id, api_hash)

def get_reply(msg):
    msg = msg.lower().strip()

    if "hi" in msg or "hello" in msg:
        return "Hi there!"
    if "sal" in msg or "ah sal" in msg:
        return "Ey ke"
    if "bong" in msg or "b" == msg or "bart" in msg:
        return "Bart o"
    if "price" in msg:
        return "Please tell me the game and package you're interested in!"

    return "Sorry, I didn't understand. Please rephrase."

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not isinstance(event.message.peer_id, PeerUser):
        return
    text = event.raw_text
    reply = get_reply(text)
    await event.reply(reply)
    print(f"✅ {text} → {reply}")

with client:
    print("🤖 Bot is running...")
    client.run_until_disconnected()
