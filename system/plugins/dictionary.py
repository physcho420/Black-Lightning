from system.Config.utils import Variable
from PyDictionary import PyDictionary
from pyrogram import filters
from system import light
from system import (
    app,
    COMMAND_HELP,
    HNDLR
)

import logging

@light.on(["dic", "define", "dictonary"])
async def dc(client, message):
    if  not message.text:
        await message.edit("**How could i define nothing?**")
        return
    txt = message.text.split()[1]
    # gramm = message.text.split()[2]
    meana = PyDictionary(txt)
    measn = ""

    no = 1
    c = 1
    mean = meana.getMeanings()
    # if  meaning
    mean = mean[txt]
    try: 

     mean = mean['Noun']
    except KeyError as e:
        await message.edit(f"**{e}**")
    first = f"{mean[0]}"

    for i in mean:
        measn +=  "\n\n" + f'{no} - ' +  f'`{i[c]}`'
        no += 1
        c += 1
    await app.send_message(message.chat.id, f"__Meaning__\n\n**{first}**\n\n🐱‍🚀**Alternate Meanings**{measn}\n")
   
COMMAND_HELP.update({
    "dictionary": f"`{HNDLR}dict or define or meaning ( word ) ( Nou`",
    "dictionary's help": "**Gets the meaning of that word from dictonary**"
})


