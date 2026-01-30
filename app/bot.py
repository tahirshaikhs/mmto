from telegram.ext import ApplicationBuilder, CommandHandler
from .instagram import fetch_posts
from .config import BOT_TOKEN, CHANNEL

async def fetch(update, context):
    if not context.args:
        await update.message.reply_text("Usage: /fetch mountain")
        return

    keyword = context.args[0]
    try:
        fetch_posts(keyword)
    except Exception as e:
        await update.message.reply_text(
            f"❌ Cannot fetch Instagram posts.\nReason:\n{e}"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("fetch", fetch))
    app.run_polling()

if __name__ == "__main__":
    main()
