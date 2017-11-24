using DSharpPlus;
using DSharpPlus.Entities;
using Soturi.Utils;
using System;
using Newtonsoft.Json;
using System.IO;

namespace Soturi.Background
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
