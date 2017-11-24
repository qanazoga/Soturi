using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using System.Threading.Tasks;
using DSharpPlus.Entities;
using Soturi.Utils;
using System.Linq;
using DSharpPlus;
using System.Collections.Generic;

namespace Soturi.Commands
{

    // TODO: Like all of these can be automated.

    [Group("vote")]
    [Description("Commands based around diplomacy, mostly for use in RRPH.")]
    public class DiplomacyCommands
    {

        ulong diplomacyHell = 327563126340059147;
        ulong botdev = 343557447748812803;
        ulong fucbois = 145992439977476097;
        

        [Command(":")]
        [Aliases("on", "to")]
        [Description("Adds Up/Downvotes to your message") ]
        public async Task Vote(CommandContext ctx)
        {
            await ctx.Message.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
            await ctx.Message.CreateReactionAsync(DiscordEmoji.FromUnicode("⬇"));
        }

        [Command("kick")]
        [RequireRoles(RoleCheckMode.Any, "fucbois")]
        [Description("Starts a vote in `#diplomacy-hell` to kick target non-`fucboi` member.")]
        public async Task Kick(CommandContext ctx, DiscordMember target)
        {
            if (!Bot.InRRPH(ctx))
                return;

            if (target.Roles.Contains(ctx.Guild.GetRole(fucbois)))
            {
                await ctx.RespondAsync($"{target.Username} is a `fucboi`!");
                return;
            }

            DiscordMessage msg = await ctx.Client.SendMessageAsync(
                ctx.Guild.GetChannel(diplomacyHell),
                $"{ctx.Guild.GetRole(fucbois).Mention}:\n{ctx.Member.Username} wants to kick {target.Mention}");
            
            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬇"));
        }

        [Command("ban")]
        [RequireRoles(RoleCheckMode.Any, "fucbois")]
        [Description("Starts a vote in `#diplomacy-hell` to kick target non-`fucboi` member.")]
        public async Task Ban(CommandContext ctx, DiscordMember target)
        {
            if (!Bot.InRRPH(ctx))
                return;

            if (target.Roles.Contains(ctx.Guild.GetRole(fucbois)))
            {
                await ctx.RespondAsync($"{target.Username} is a `fucboi`!");
                return;
            }

            DiscordMessage msg = await ctx.Client.SendMessageAsync(
                ctx.Guild.GetChannel(diplomacyHell),
                $"{ctx.Guild.GetRole(fucbois).Mention}:\n{ctx.Member.Username} wants to ban {target.Mention}");

            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬇"));
        }

        [Command("promote")]
        [RequireRoles(RoleCheckMode.Any, "fucbois")]
        [Description("Starts a vote in `#diplomacy-hell` to promote target non-`fucboi` member to `fucboi` status.")]
        public async Task Promote(CommandContext ctx, DiscordMember target)
        {
            if (!Bot.InRRPH(ctx))
                return;

            if (target.Roles.Contains(ctx.Guild.GetRole(fucbois)))
            {
                await ctx.RespondAsync($"{target.Username} is already a `fucboi`!");
                return;
            }

            DiscordMessage msg = await ctx.Client.SendMessageAsync(
                ctx.Guild.GetChannel(diplomacyHell),
                $"{ctx.Guild.GetRole(fucbois).Mention}:\n{ctx.Member.Username} wants to promote {target.Mention} to be a `fucboi`");

            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬇"));
        }

        [Command("demote")]
        [RequireRoles(RoleCheckMode.Any, "fucbois")]
        [Description("Starts a vote in `#diplomacy-hell` to demote target `fucboi` to non-`fucboi` status.")]
        public async Task Demote(CommandContext ctx, DiscordMember target)
        {
            if (!Bot.InRRPH(ctx))
                return;

            if (!target.Roles.Contains(ctx.Guild.GetRole(fucbois)))
            {
                await ctx.RespondAsync($"{target.Username} isn't a `fucboi`!");
                return;
            }

            DiscordMessage msg = await ctx.Client.SendMessageAsync(
                ctx.Guild.GetChannel(diplomacyHell),
                $"{ctx.Guild.GetRole(fucbois).Mention}:\n{ctx.Member.Username} wants to demote {target.Mention} from `fucboi` status");

            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
            await msg.CreateReactionAsync(DiscordEmoji.FromUnicode("⬇"));
        }

        [Command("add-game")]
        [RequireRoles(RoleCheckMode.Any, "fucbois")]
        [Description("After enough interest, adds a game, private category, and channels to RRPH.")]
        public async Task AddGame(CommandContext ctx, [Description("The game to add.")]string game) 
        {
            if (!Bot.InRRPH(ctx))
                return;
            
            await ctx.Message.CreateReactionAsync(DiscordEmoji.FromUnicode("⬆"));
        }
    }
}
