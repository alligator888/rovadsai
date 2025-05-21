from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes 
import os

TOKEN = '7693613629:AAFbQ61u76LjprsLw6jiMli6otOm5p41UYc'  # Bot tokenınızı daxil edin

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Butonlar
    buttons = [
        [InlineKeyboardButton("📲İndi Sifariş Et", url="https://t.me/telmanrov", callback_data='buton1')],
        [InlineKeyboardButton("📈Ətraflı Məlumat", url="https://t.me/rovads", callback_data='buton2')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    caption = (
    "Sadə interfeys – ControllerBot-dan daha asandır, daha sürətlidir.\n"
    "Post altına buton əlavə etmək – bir neçə addımda ||Sifariş et|| və ya istədiyin linkli buton yarada bilərsən.\n"
    "Vaxt təyin etmə funksiyası – postu avtomatik olaraq təyin etdiyin vaxtda paylaşır."
)

    mp4_path = 'content.mp4'  # MP4 fayl yolu

    # MP4 animasiyasını göndər
    with open(mp4_path, 'rb') as video:
        await context.bot.send_animation(
            chat_id=chat_id,
            animation=video,
            caption=caption,
            reply_markup=reply_markup
        )
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    PORT = int(os.environ.get("PORT", 8000))
    WEBHOOK_URL = f"https://worker.up.railway.app/{TOKEN}"  # Railway-dəki URL-ni buraya yaz

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=WEBHOOK_URL
    )