# Thanks @dev for dis plug <3

import logging
from git import Repo
import git
import asyncio 
import os
import heroku3
from system.Config import Variable
from system.Config.utils import language
from system import (  app,
  g,
  bot,
  a,
  HNDLR,
  COMMAND_HELP,
  REPO,
  API_KEY,
  APP_NAME,
  BRANCH )
import io
import sys
from system.plugins import light
@light.on(["update", "update now", "upd", "u"])
async def updater(client, message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote('ub', REPO)
        origin.fetch()
        repo.create_head('rebirth', origin.refs.rebirth)
        repo.heads.rebirth.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != 'rebirth':
        await message.edit(
            f"**{language('You are using custom branch fill')} {BRANCH} name {language('if u want updates')}!".format(branch_name=active_branch_name)
        )
        return

    try:
        repo.create_remote('ub', REPO)
    except Exception as e:
        logging.error(f"ERROR WHILE UPDATING \n{e}")
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in repo.iter_commits():
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    
    upstream = repo.remote(REPO)


    
    upstream.fetch(BRANCH)

    out_put_str = ""
    d_form = "%d/%m/%y"

    for repo_change in repo.iter_commits():
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    await message.edit(f"AVAILABLE UPDATES\n\n{out_put_str}")

    if  not out_put_str:
        await message.edit(f"{('`No Update AvaiLAbLe from')} BLACK LIGHTNING CHECK OUT CHANNEL @lightning_support_channel`")
        return
        

    if len(out_put_str) > 4095:
        with io.BytesIO(str.encode(out_put_str)) as file:
          file.name = "updates.txt"
        await app.send_document (
            message.chat.id, document="updates.txt", caption='UPDATES'
        )
    if out_put_str:
        with open("updates.txt") as f:
            f.write("Available")
    if not out_put_str:
        reading_file = open("updates.txt", "r")
        new_file_content = ""
        for line in reading_file:
          stripped_line = line.strip()
          new_line = stripped_line.replace("Available", "Nope")
          new_file_content += new_line +"\n"
        reading_file.close()
        writing_file = open("updates.txt", "w")
        writing_file.write(new_file_content)
        writing_file.close()
    else:
    
       upstream.fetch('rebirth')
       repo.git.reset("--hard", "FETCH_HEAD")
    heroku = heroku3.from_key(Variable.HEROKU_API_KEY)
    heroku_applications = heroku.apps()
    if len(heroku_applications) >= 1:
        if APP_NAME is not None & API_KEY is not None:
            heroku_app = None
            for i in heroku_applications:
                if i.name == APP_NAME:
                    heroku_app = i
            heroku_git_url = heroku_app.git_url.replace(
                "https://", "https://api:" + APP_NAME + "@"
            )
            remote = repo.create_remote("heroku", heroku_git_url)
            if "heroku" in repo.remotes:
                remote = repo.remote("heroku")
                remote.set_url(heroku_git_url)
            else:
                #  remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop(
                    strt(message, "HEAD:refs/heads/rebirth",  remote)
            )
       
            
    else:
        await message.edit(f"HEROKU_APP_NAME {language('not found')} :/, {language('now will not update your userbot')} XoX")

    
    
    def func():
        
    
        func.str = out_put_str

async def strt(message, refspec, remote):
    up=language(f"{language('UPDATING! KINDLY WAIT TILL BOT IS RE_DEPLOYED')}")
    await message.edit(
        f"**{up}**\n\n__{language('How much time it will take?')}__: **{language('Well depends upong your heroku internet ping')}**"
    )
    await remote.push(refspec=refspec)
    await app.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)


COMMAND_HELP.update({
    f"git": f"`{HNDLR}update",
    "git's help" : "**USE**: __{language('Updates userbot')}__",
    "git's type": "updater"
})
