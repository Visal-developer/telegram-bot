from telethon import TelegramClient, events
from telethon.tl.types import PeerUser

# ✅ Telegram API
api_id = 28210729
api_hash = '0dfa6e40e5da54025b30219bf9c15cdf'

# ✅ Session name must match .session file
client = TelegramClient('bot_session', api_id, api_hash)

# ✅ Keyword-based Khmer reply function
def get_keyword_reply(message):
    msg = message.lower().strip()

    if any(word in msg for word in ["hi", "hii", "hiii"]):
        return "Hi 😊"
    if "hello" in msg:
        return "Hello 🙏"
    if "hey" in msg:
        return "Hah 🤨"
    if "sal" in msg or "ah sal" in msg:
        return "Ey ke 😏"
    if msg == "b" or "bart" in msg:
        return "Bart o 🕶️"
    if "bong" in msg:
        return "Bart o 🔥"
    if "how are you" in msg or "sok sabay" in msg:
        return "ខ្ញុំសុខសប្បាយ! អរគុណចំពោះការសួរ 😄"
    if "topup" in msg or "top-up" in msg:
        return "យើងមានសេវា top-up MLBB, Free Fire, PUBG 💎 តម្លៃសមរម្យ!"
    if "mlbb" in msg:
        return "MLBB មាន 86, 172, 257 Diamonds។ តើអ្នកចង់យកប៉ុន្មាន?"
    if "free fire" in msg or "ff" in msg:
        return "FF package: 100, 210, 530 Diamonds។"
    if "pubg" in msg or "uc" in msg:
        return "PUBG UC: 60, 325, 660, 1800UC ✈️"
    if "tiktok" in msg:
        return "TikTok coins top-up មានតម្លៃសមរម្យ និងលឿន ⏱️"
    if "price" in msg or "how much" in msg or "rate" in msg:
        return "តម្លៃអាស្រ័យលើ package ដែលអ្នកជ្រើស 💰"
    if "payment" in msg or "pay" in msg or "wing" in msg or "bakong" in msg or "aba" in msg:
        return "ទទួលទូទាត់តាម Wing, ABA, Bakong, TrueMoney ✅"
    if "thank" in msg or "thanks" in msg or "អរគុណ" in msg:
        return "សូមអរគុណដែលបានជឿជាក់ និងប្រើសេវារបស់យើង ❤️"
    if "admin" in msg or "contact" in msg:
        return "សូមទំនាក់ទំនង Admin @YourAdminUser ✉️"
    if "ប៉ុន្មាន" in msg or "តម្លៃ" in msg:
        return "តម្លៃសម្រាប់ package តាម game ដែលអ្នកចង់បាន។ សូមប្រាប់បន្ថែម។"
    if "buy" in msg or "purchase" in msg:
        return "តើអ្នកចង់ទិញ game ណាមួយ? MLBB, FF, PUBG ឬ TikTok?"

    return "សួស្តី! ខ្ញុំមិនយល់សាររបស់អ្នកទេ។ សូមពិពណ៌នាថ្មី 🧐"

# ✅ Respond only to personal chats
@client.on(events.NewMessage(incoming=True))
async def auto_reply_handler(event):
    if not isinstance(event.message.peer_id, PeerUser):
        return  # Ignore groups/channels

    user_msg = event.raw_text
    print(f"📩 Message: {user_msg}")
    reply = get_keyword_reply(user_msg)
    await event.reply(reply)
    print(f"✅ Replied: {reply}")

# ✅ Run the bot
with client:
    print("🤖 Khmer Smart Reply Bot is running...")
    client.run_until_disconnected()
