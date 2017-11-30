using DSharpPlus;
using DSharpPlus.Entities;
using Soturi4.Utils;

namespace Soturi4.Background
{
    class ImageLibrarian
    {
        public ImageLibrarian(DiscordClient client)
        {

            client.MessageCreated += async (e) =>
            {
                if (e.Channel.Id != 306250266234060802)
                    return;

                if (e.Message.Attachments.Count == 0)
                {
                    DiscordDmChannel dm = await client.CreateDmAsync(e.Author);
                    await e.Message.DeleteAsync();
                    await dm.SendMessageAsync("Your message was removed from `#soturi-image-library`!\nPlease only submit image files.");
                }
                else if (e.Message.Content.ToLower().Contains("delet"))
                {
                    await e.Message.CreateReactionAsync(DiscordEmoji.FromGuildEmote(client, 341681244867657753));
                    await e.Message.CreateReactionAsync(DiscordEmoji.FromGuildEmote(client, 341681253835210753));
                }
                else
                {
                    await e.Message.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
                    await e.Message.CreateReactionAsync(DiscordEmoji.FromUnicode("⬇"));
                }

            };


            Bot.LogMessage("\tImage Librarian successfully registered.");
        }
    }
}
