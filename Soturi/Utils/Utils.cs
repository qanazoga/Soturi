using System;
using System.Threading.Tasks;
using DSharpPlus.CommandsNext;
using DSharpPlus.Entities;
using System.Linq;

namespace Soturi.Utils
{
    class Bot
    {
        /// <summary>
        /// A simple check to see if a command is taking place in RainbowRumpusPartyHell.
        /// </summary>
        /// <param name="ctx">The CommandContext of the command.</param>
        /// <returns></returns>
        public static Boolean InRRPH(CommandContext ctx)
        {
            return ctx.Channel.GuildId == 138687693193347073;
        }

        /// <summary>
        /// Used to toggle a role a role from from a member in a given guild.
        /// </summary>
        /// <param name="role">The role to toggle.</param>
        /// <param name="member">The member to toggle the role from.</param>
        /// <param name="guild">The guild that contains the role.</param>
        /// <returns></returns>
        public static async Task ToggleRoleForMember(DiscordRole role, DiscordMember member)
        {
            if (member.Roles.Contains(role))
                await member.RevokeRoleAsync(role);
            else
                await member.GrantRoleAsync(role);
        }

        public static void LogMessage(String message)
        {
            Program.Client.DebugLogger.LogMessage(
                DSharpPlus.LogLevel.Info,
                "Soturi",
                message,
                DateTime.Now);
        }

        public static void LogError(String error)
        {
            Program.Client.DebugLogger.LogMessage(
                DSharpPlus.LogLevel.Error,
                "Soturi",
                error,
                DateTime.Now);
        }
        
        /// <summary>
        /// A simple solution for regisering a bunch of Commands at once.
        /// </summary>
        /// <param name="extension">The CommandNextModle of your bot</param>
        /// <param name="commandContainers">a list of new instances of the classes that contain commands. Since they all have different types, they are all brought in as Object.</param>
        public static void RegisterAllCommands(CommandsNextExtension extension, params Object[] commandContainers)
        {
            foreach (Object cc in commandContainers)
                extension.RegisterCommands(cc.GetType());
        }
    }
}

