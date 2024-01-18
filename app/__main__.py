from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from app.bot import flip_coin, show_stats, start

if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("6819127169:AAEcm_AcfVo-v0bsDlUsa72tOZ3ZxJNh13s")
        .build()
    )

    flip_coin_handler = MessageHandler(filters.TEXT & filters.Regex(r"Бросить Монетку"), flip_coin)
    stats_handler = MessageHandler(filters.TEXT & filters.Regex(r"История"), show_stats)
    start_handler = CommandHandler("start", start)

    application.add_handler(flip_coin_handler)
    application.add_handler(stats_handler)
    application.add_handler(start_handler)

    application.run_polling()
