using DSharpPlus;
using DSharpPlus.Entities;
using DSharpPlus.EventArgs;
using Soturi4.Background;
using Soturi4.Commands;
using Soturi4.Commands.Warframe;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Soturi4.Utils
{
    class ExtendedListener
    {
        public ExtendedListener(DiscordClient client)
        {
            client.Ready += async (e) =>
            {
                Bot.LogMessage("Successfully Connected");

                Bot.LogMessage("Registering Commands...");
                Bot.RegisterAllCommands(
                    Program.Commands,
                    new AdminCommands(),
                    new DiplomacyCommands(),
                    new InfoCommands(),
                    new MiscCommands(),
                    new StyxCommands(),
                    new WarframeCommands()
                    );
                Bot.LogMessage($"Successfully registerd {Program.Commands.RegisteredCommands.Count} commands:");
                foreach (String command in Program.Commands.RegisteredCommands.Keys)
                    Bot.LogMessage($"\t{command}");

                var listeners = new RRPHListeners(Program.Client);

                await client.UpdateStatusAsync(new DiscordActivity(">help"));

                Program.StartTime = DateTime.Now;

                Bot.LogMessage("Setup Complete.");
            };

            client.MessageCreated += async (e) =>
            {
                client.DebugLogger.LogMessage(
                    LogLevel.Info,
                    e.Author.Username,
                    (e.Message.Attachments.Count > 0 ? LogMessageWithFiles(e) : "") + $"{e.Message.Content}",
                    DateTime.Now);

                await Task.Yield();
            };

            client.ClientErrored += async (e) =>
            {
                client.DebugLogger.LogMessage(
                    LogLevel.Error,
                    "ERROR",
                    e.Exception.Message,
                    DateTime.Now);

                Console.WriteLine(e.Exception.StackTrace);

                await Task.Yield();
            };

            
        }

        public string LogMessageWithFiles(MessageCreateEventArgs e)
        {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < e.Message.Attachments.Count; i++)
                sb.Append($"[File:{e.Message.Attachments[i].FileName}] ");

            return sb.ToString();
        }
    }
}
