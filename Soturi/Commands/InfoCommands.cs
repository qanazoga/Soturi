using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Soturi4.Commands
{
    class InfoCommands
    {

        [Command("ping")]
        [Description("Gets websocket latency of this bot")]
        public async Task Ping(CommandContext ctx)
        {
            await ctx.RespondAsync($"WebSocket latency: {ctx.Client.Ping}");
        }

        [Command("uptime")]
        [Description("Returns the uptime of this bot")]
        public async Task Uptime(CommandContext ctx)
        {
            var uptime = DateTime.Now.Subtract(Program.StartTime);
            await ctx.RespondAsync((String.Format($"Current uptime: {uptime.ToString(@"dd")} days, {uptime.ToString(@"hh\:mm\:ss")}")));
        }

    }
}
