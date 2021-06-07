from system.plugins import light
from system import app, HNDLR, COMMAND_HELP

@light.on(["cloud"])
async def cld(client, message):


    ok = message.text 
    if ok is None:
        await message.edit(f"**Syntax**: __{HNDLR}cloud password hint ( your desired email for protection if forgot password ) __")
    try:
      passo = ok.split()[1]
  
      mail = ok.split()[3]
      hint = ok.split()[2]
      await app.enable_cloud_password(passo, hint=hint, email=mail)
      await app.send_message("me", "Cloud password enabled!")

    except IndexError as e:
        await message.edit("ERROR!, " + e)
    except BaseException as e:
      await message.edit(f"**{e}**")