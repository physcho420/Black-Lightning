# Copyright (C) 2021 KeinShin@Github.

from system.Config.utils import Variable
from system import light




from system import *
@light.on(["send"])
async def send(client, message):
    try:
        txt=message.text
    except IndexError:
        await message.edit(f"**Syntax**: __{HNDLR}send (file name)__\n\n@lightning_support_grup")
    if not " " in message.text:
        await message.edit(f"**Syntax**: __{HNDLR}send (file name)__\n\n@lightning_support_grup")
        return
    txt=message.text.split()[1]

    if  Path(f'system/plugins/{txt}.py').is_file():
        path = f"system/plugins/{txt}.py"
        try:
            caption =  f"**PLUGINS** - __{txt}__\n**COMMAND** - {COMMAND_HELP[txt]}\n\n@lightning_support_grup"
        except KeyError:
            caption =  f"**PLUGINS** - __{txt}__\n\n@lightning_support_grup"
        await app.send_document(message.chat.id, document=path, caption=caption, force_document=True)
    elif "sqlite" in message.text:
        if not Path(f'system/datas_sqlite/{txt}.py').is_file():
            await message.edit("**SQL DOES NOT EXSISTS!**")
        else:
           path = f"system/datas_sqlite/{txt}.py"
           await app.send_document(message.chat.id, document=path, caption=f"**SQL-FILE** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    elif "requirements" in message.text:
        path = f"{txt}.txt"
        line =  len(open(path).readlines())

        await app.send_document(message.chat.id, document=path, caption=f"**REQUIREMENTS-FILE** \n**Black Lightning is using {line} libraries** - __{txt}__\n\n@lightning_support_grup", force_document=True)
    else:
        await message.edit("**{} does not exsists! (make sure name is correct :/)**".format(txt))


COMMAND_HELP.update({
    "send": f"`{HNDLR}send` __(file name)__",
    "send's help": f"\n\n**USE**: __sends the given command/requirements/sql file__"
})