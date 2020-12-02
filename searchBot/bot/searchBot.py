import discord

from utils import save_keyword, search_api_call, get_db_search_results

BOT_TOKEN = 'NzgzNTY5ODM2ODIyNjI2MzQ0.X8cqRw.e9NFUu2T49M_SYl5lBLn5huTk_o'

client = discord.Client()

@client.event
async def on_message(message):
    """
    Reply to messages
    :param message:
    :return:
    """
    message.content = message.content.lower()

    if message.author == client.user:
        return

    if message.content.startswith("hi"):
        await message.channel.send("hey")

    if message.content.startswith("!google"):
        keyword = message.content[8:]

        # save keyword to used for search functionality
        save_keyword(message.author, keyword)

        # send top 5 search results from api search api response
        search_results = search_api_call(keyword)
        if search_results:
            for res in search_results:
                await message.channel.send(res)
        else:
            msg = f"Your search - {keyword} - did not match any documents."
            await message.channel.send(msg)

    # if message.content.startswith("!recent"):
    #     keyword = message.content[8:]
    #     db_results = get_db_search_results(keyword)
    #     if db_results:
    #         for res in db_results:
    #             await message.channel.send(res.keyword)
    #     else:
    #         msg = f"No previous search for {keyword}"
    #         await message.channel.send(msg)

client.run(BOT_TOKEN)
