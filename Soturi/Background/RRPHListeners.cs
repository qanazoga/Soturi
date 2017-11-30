using DSharpPlus;
using DSharpPlus.Entities;
using Soturi4.Utils;
using System;
using Newtonsoft.Json;
using System.IO;

namespace Soturi4.Background
{
    class RRPHListeners
    {
        public RRPHListeners(DiscordClient client)
        {
            Bot.LogMessage("Registering additional listeners...");
            var librarian = new ImageLibrarian(client);
            var freeGameNewsMod = new FreeGameNewsMod(client);
            var roleSignupSys = new RoleSignupSystem(client);
            Bot.LogMessage("Successfully registered all aditional listeners.");
        }
    }
}
