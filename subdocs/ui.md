## Intro
Welcome to the documentation of the UI add-on! 🎩

UIs are very important when you want to satisfy your
bot's users. They not only look good, but they also
prove you're a professional, and that you have style ✨.

Here's an example script to get you going:
```py
import dotenv, os
from wokkichat import Bot, ctx
from wokkichat.addons import ui

dotenv.load_dotenv()
bot = Bot(os.environ["TOKEN"])

@bot.command()
async def embed(c: ctx):
    view = ui.View()
    embed = ui.Embed(
        "Cool title",
        "this is a description",
        footer="look at this footer!"
        )
    button = ui.Button("Click me")

    embed.add_component(button)
    view.add_embed(embed)

    await c.reply(view=view)

bot.connect()
```
Try out `/embed` and see what happens!

---
## Docs
