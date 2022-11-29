from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pygismeteo import Gismeteo

async def temperature(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = update.message.text
    city = city.split(" ")
    city = list(filter(lambda x: not "/temp" in x, city[1:]))
    city = " ".join(city)
    gismeteo = Gismeteo()
    search_results = gismeteo.search.by_query(city)
    city_id = search_results[0].id
    current = gismeteo.current.by_id(city_id)
    print(f"В городе {city} сейчас {current.temperature.air.c} *С")
    await update.message.reply_text(f"В городе {city} сейчас {current.temperature.air.c} *С")


app = ApplicationBuilder().token("5581913275:AAEUjI5oarlQ0kQDnZR_UgHb5pc_NxkAlC8").build()
app.add_handler(CommandHandler("temp", temperature))
print("сервер запустился")
app.run_polling()
