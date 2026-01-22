## Intro
Welcome to the documentation of the Python SDK for [Wokki Chat](https://chat.wokki20.nl/)! 📖

*✏️ Want to help us write the docs?
Read [CONTRIBUTING.md](https://github.com/levkris/Wokki-Chat-Python-SDK/blob/wokkichat/CONTRIBUTING.md)*

Everyone knows a chat platform without bots is dull and boring,
but not Wokki Chat! The contributors to this library have worked
hard to make the most amazing yet simplistic library for you,
so enjoy!

```
BLEEP-BLOOP, ENJOY MAKING BOTS! 🤖
- Bjarnos
```

---

## Example
We know how hard it is to get started with a
library you know nothing about,
so here's an example script to get you going:
```py
import dotenv, os
from wokkichat import Bot, ctx

dotenv.load_dotenv()
bot = Bot(os.environ["TOKEN"])

@bot.command()
async def echo(c: ctx, text: str):
    await c.reply(f"Echoed: {text}")

bot.connect()
```
After installing `python-dotenv` with pip,
and running the code, try out `/echo` and see what happens!

---
## Docs
