using DSharpPlus;
using Newtonsoft.Json;
using Soturi.Utils;
using System;
using System.IO;

namespace Soturi.Background
{
    class RoleSignupSystem
    {
        public RoleSignupSystem(DiscordClient client)
        {
            client.MessageReactionAdded += async (e) =>
            {
                if (e.Channel.Id != 347916942335541248)
                    return;

                if (e.User.IsBot)
                    return;

                try
                {
                    var file = await System.IO.File.ReadAllTextAsync("data/config/roles.json");
                    var roles = JsonConvert.DeserializeObject<Role[]>(file);

                    foreach (Role r in roles)
                    {
                        if (e.Message.Id == r.Message_Id)
                        {
                            Bot.LogMessage($"[{e.User.Username}#{e.User.Discriminator}] has signed up for [{e.Channel.Guild.GetRole(r.Role_Id).Name}]");
                            var member = await e.Channel.Guild.GetMemberAsync(e.User.Id);
                            await member.GrantRoleAsync(
                                e.Channel.Guild.GetRole(r.Role_Id));
                            return;
                        }
                    }
                }
                catch (FileNotFoundException)
                {
                    Bot.LogError("The roles.json file could not be found!");
                    return;
                }
                catch (Exception err)
                {
                    Bot.LogError("I'm configured like shit");
                    Bot.LogError(err.Message);
                    return;
                }
            };

            client.MessageReactionRemoved += async (e) =>
            {
                if (e.Channel.Id != 347916942335541248)
                    return;

                if (e.User.IsBot)
                    return;

                try
                {
                    var file = await System.IO.File.ReadAllTextAsync("data/config/roles.json");
                    Role[] roles = JsonConvert.DeserializeObject<Role[]>(file);

                    foreach (Role r in roles)
                    {
                        if (e.Message.Id == r.Message_Id)
                        {
                            Bot.LogMessage($"[{e.User.Username}#{e.User.Discriminator}] has lost interest in [{e.Channel.Guild.GetRole(r.Role_Id).Name}]");
                            var member = await e.Channel.Guild.GetMemberAsync(e.User.Id);
                            await member.RevokeRoleAsync(
                                e.Channel.Guild.GetRole(r.Role_Id),
                                $"{e.User.Username}#{e.User.Discriminator} lost interest.");
                            return;
                        }
                    }
                }
                catch (FileNotFoundException)
                {
                    Bot.LogError("The roles.json file could not be found!");
                    return;
                }
                catch (Exception err)
                {
                    Bot.LogError("I'm configured like shit");
                    Bot.LogError(err.Message);
                    return;
                }
            };

            Bot.LogMessage("\tSoturi Role Signup System has been successfully registered.");
        }
    }

    partial class Role
    {
        [JsonProperty("message_id")]
        public ulong Message_Id { get; set; }

        [JsonProperty("role_id")]
        public ulong Role_Id { get; set; }
    }
}
