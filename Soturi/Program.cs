using DSharpPlus;
using DSharpPlus.CommandsNext;
using Newtonsoft.Json;
using Soturi.Utils;
using System;
using System.IO;
using System.Text;
using System.Threading.Tasks;

namespace Soturi
{
    class Program
    {
        
        public static DiscordClient Client { get; set; }
        public static ExtendedListener Logger { get; set; }
        public static CommandsNextExtension Commands { get; set; }
        public static Config Config { get; set; }

        static void Main(string[] args)
        {
            Console.Title = "Soturi";
            Console.OutputEncoding = Encoding.UTF8;
            MainAsync(args).ConfigureAwait(false).GetAwaiter().GetResult();
        }


        static async Task MainAsync(string[] args)
        {
            
            var file = await System.IO.File.ReadAllTextAsync("data/config/config.json");
            Config = JsonConvert.DeserializeObject<Config>(file);

            Client = new DiscordClient(new DiscordConfiguration
            {
                Token = Config.Token,
                UseInternalLogHandler = true,
                LogLevel = LogLevel.Info
            });

            Logger = new ExtendedListener(Client);

            Commands = Client.UseCommandsNext(new CommandsNextConfiguration
            {
                StringPrefix = Config.Prefix,
                CaseSensitive = false
            });

            await Client.ConnectAsync();
            await Task.Delay(-1);
        }
    }

    partial class Config
    {
        [JsonProperty("token")]
        public string Token { get; set; }

        [JsonProperty("prefix")]
        public string Prefix { get; set; }
    }
}

