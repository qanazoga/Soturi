using DSharpPlus;
using DSharpPlus.Entities;
using Soturi4.Utils;

namespace Soturi4.Background
{
    class FreeGameNewsMod
    {
        public FreeGameNewsMod(DiscordClient client)
        {
            client.MessageCreated += async (e) =>
            {
                if (e.Channel.Id != 360580447517933570)
                    return;

                if (!e.Message.Content.Contains("http") || !e.Message.Content.Contains(e.Guild.GetRole(360580064934494208).Mention))
                {
                    DiscordDmChannel dm = await client.CreateDmAsync(e.Author);
                    await dm.SendMessageAsync("Your message was removed from `#free-game-news`!\nPlease remember to tag `@free-game-news` and include a link to the game.");
                    await e.Message.DeleteAsync();
                }
            };

            Bot.LogMessage("\tFree Game News mod successfully registered");
        }
    }
}
