using System.Threading.Tasks;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using Soturi.Utils;
using System;
using System.Threading;

namespace Soturi.Commands
{
    class AdminCommands
    {

        [Command("rrphsudo"), RequireOwner]
        [Aliases("aboosemode", "sudo")]
        [Description("Use if you're qanazoga and you need to aboose some chats.")]
        public async Task AbooseMode(CommandContext ctx)
        {
            if (!Bot.InRRPH(ctx))
                return;

            Bot.LogMessage($"Toggling aboosemode on {ctx.Message.Author.Mention}.\n");

            DiscordRole admin = ctx.Guild.GetRole(151020651438800896);
            await Bot.ToggleRoleForMember(admin, ctx.Member);
        }

        [Group("clean", CanInvokeWithoutSubcommand = true), RequireOwner]
        public class Clean
        {
            
            [Description("Removes `x` messages from the current channel.")]
            public async Task ExecuteGroupAsync(CommandContext ctx, [Description("The number of messages to remove")] int x)
            {
                if (!Bot.InRRPH(ctx))
                    return;

                Thread.Sleep(100);

                if (x <= 0)
                {
                    await ctx.RespondAsync($"Okay, removing {x} messages :p");
                    return;
                }

                Bot.LogMessage($"Removing {x+1} messages from {ctx.Channel.Name}...");

                await ctx.Channel.DeleteMessagesAsync(await ctx.Channel.GetMessagesAsync(x+1));
                
                Bot.LogMessage($"Done removing messages.");
            }

            [Command("until"), RequireOwner]
            [Description("Removes messages from the current channel until it deletes the target message.")]
            public async Task CleanUntil(CommandContext ctx, [Description("The ID of the target message")] ulong x)
            {
                if (!Bot.InRRPH(ctx))
                    return;

                var messageFound = false;
                var counter = 0;

                foreach (DiscordMessage message in await ctx.Channel.GetMessagesAsync()) 
                {
                    counter++;
                    if (message.Id == x)
                    {
                        messageFound = true;
                        break;
                    }
                        
                }

                if (messageFound)
                {
                    Bot.LogMessage($"Removing {counter} messages from {ctx.Channel.Name}...");
                    await ctx.Channel.DeleteMessagesAsync(await ctx.Channel.GetMessagesAsync(counter));
                    Bot.LogMessage($"Done removing messages");
                }
                else
                {
                    await ctx.RespondAsync("That message couldn't be found within the last 100 messages in this channel (try again after `clean 100`?)");
                }


            }
        }



        [Command("shutdown"), RequireOwner]
        [Description("Gracefully shutdown this bot, and all connections")]
        public async Task ShutDown(CommandContext ctx)
        {
            await ctx.RespondAsync("Gracefully shutting down...");
            await ctx.Client.DisconnectAsync();
            Environment.Exit(0);
        }

    }
}

