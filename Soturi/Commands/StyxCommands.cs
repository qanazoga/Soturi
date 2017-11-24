using Soturi.Utils;
using DSharpPlus.CommandsNext;
using System.Threading.Tasks;
using DSharpPlus.Entities;
using DSharpPlus.CommandsNext.Attributes;

namespace Soturi
{
    public class StyxCommands
    {
        [Command("styx")]
        [Description("Adds the `styx-user` role to a `member`.\nRequires Role: `styx-admin`."), RequireRoles(RoleCheckMode.Any, "styx-admin")] 
        public async Task Styx(CommandContext ctx, [Description("The `member` who needs the `styx-user` role added/removed.")] DiscordMember member)
        {
            if (!Bot.InRRPH(ctx))
                return;

            DiscordRole styxuser = ctx.Guild.GetRole(376461381702254613);
            Bot.LogMessage($"Toggling styx-user role for {member.Mention}\n");
            await Bot.ToggleRoleForMember(styxuser, member);
        }
    }
}



