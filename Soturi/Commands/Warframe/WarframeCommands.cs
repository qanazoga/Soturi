using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Soturi4.Commands.Warframe
{
    //TODO: these

    [Group("warframe"), RequireRoles(RoleCheckMode.Any, "warframe")]
    [Description("Various commands for Warframe\n NONE OF THESE ARE DONE")]
    public class WarframeCommands
    {

        [Group("alerts")]
        [Description("Commands related to the in-game alert system, and the `warframe-alerts` channel")]
        public class AlertCommands
        {

            [Command("subscribe"), Aliases("sub")]
            [Description(
                "Subscribes you to be notified about any alerts that include `<item>`\n" +
                "This can include things like `nitain` `\"dera vandal\", or even phrases like `\"gift of the lotus\"`")]
            public async Task Subscribe(CommandContext ctx, [Description("The items you want to be notified about")] params string[] items)
            {
                if (items.Count() < 1)
                    return;

                StringBuilder response = new StringBuilder();
                response.Append("Subscribing you to the following items:\n");
                foreach (string item in items)
                {
                    response.Append($"{item}\n");
                }
                await ctx.RespondAsync(response.ToString());
            }

            [Command("unsubscribe"), Aliases("unsub")]
            [Description("Unsubscribes you from alerts for a given <item>")]
            public async Task Unsubscribe(CommandContext ctx, [Description("The items you want to no longer to be notified about")] params string[] items)
            {
                if (items.Count() < 1)
                    return;

                StringBuilder response = new StringBuilder();
                response.Append("Unsubscribing you from the following items:\n");
                foreach (string item in items)
                {
                    response.Append($"{item}\n");
                }
                await ctx.RespondAsync(response.ToString());
            }

        }

        [Group("time")]
        [Description("Commands related to the in-game time system")]
        public class TimeCommands
        {
            
            [Command("cetus")]
            [Description("Shows the the current time on Cetus (day/night) and how much longer is left in that cycle")]
            public async Task Cetus(CommandContext ctx)
            {

            }

            [Command("earth")]
            [Description("Shows the the current time on Earth (day/night) and how much longer is left in that cycle")]
            public async Task Earth(CommandContext ctx)
            {

            }

        }

    }
}
