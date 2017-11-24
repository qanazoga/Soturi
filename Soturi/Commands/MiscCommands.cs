using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace Soturi.Commands
{
    class MiscCommands
    {

        [Command("ping"), Hidden]
        [Description("Gets websocket latency of this bot")]
        public async Task Ping(CommandContext ctx)
        {
            await ctx.RespondAsync($"WebSocket latency: {ctx.Client.Ping}");
        }


        [Command("invite")]
        [Description("Responds with this bots invite URL."), RequireOwner]
        public async Task Invite(CommandContext ctx)
        {
            await ctx.RespondAsync("https://discordapp.com/api/oauth2/authorize?client_id=241113397935079424&scope=bot");
        }

        [Command("mfw")]
        [Description("Posts a random reaction picture.")]
        public async Task MFW(CommandContext ctx, [RemainingText] params string[] when)
        {
            var rand = new Random();
            var path = "data/img/mfw";
            await ctx.TriggerTypingAsync();
            try
            {
                List<string> files = new List<string>();
                files.AddRange(Directory.GetFiles(path, "*.jpg"));
                files.AddRange(Directory.GetFiles(path, "*.jpeg"));
                files.AddRange(Directory.GetFiles(path, "*.png"));
                files.AddRange(Directory.GetFiles(path, "*.gif"));

                await ctx.RespondWithFileAsync(files[rand.Next(files.Count)]);
            }
            catch (DirectoryNotFoundException)
            {
                await ctx.RespondAsync($"I'm configured wrong, `{path}` isn't a real directory ;~;");
            }
            catch (Exception)
            {
                await ctx.RespondAsync("mfw I can't find my pics ;~;");
            }
        }

        [Command("choose")]
        [Aliases("choice")]
        [Description(
            "Selects a random value from a list of choices.\n" +
            "Seperate your choices by spaces, if your thing has spaces in it, surround it with quotes.\n" +
            "ie `>choose \"Go to bed\" \"Stay up all night again, nothing really matters anyway...\"`")]
        public async Task Choose(CommandContext ctx, [Description("Array of possible choices")] params string[] choices)
        {
            var rand = new Random();
            await ctx.RespondAsync(choices[rand.Next(choices.Length)]);
        }
    }
}
