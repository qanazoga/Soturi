using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Formats.Jpeg;
using SixLabors.ImageSharp.Processing;
using SixLabors.Primitives;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;

namespace Soturi4.Commands
{
    class MiscCommands
    {

        [Command("invite")]
        [Description("Responds with this bots invite URL."), RequireOwner]
        public async Task Invite(CommandContext ctx)
        {
            await ctx.RespondAsync("https://discordapp.com/api/oauth2/authorize?client_id=241113397935079424&scope=bot");
        }

        [Command("mfw")]
        [Description("Posts a random reaction picture.")]
        public async Task MFW(CommandContext ctx, [RemainingText] params string[] when)
        {
            var rand = new Random();
            var path = "data/img/mfw";
            await ctx.TriggerTypingAsync();
            try
            {
                List<string> files = new List<string>();
                files.AddRange(Directory.GetFiles(path, "*.jpg"));
                files.AddRange(Directory.GetFiles(path, "*.jpeg"));
                files.AddRange(Directory.GetFiles(path, "*.png"));
                files.AddRange(Directory.GetFiles(path, "*.gif"));

                await ctx.RespondWithFileAsync(files[rand.Next(files.Count)]);
            }
            catch (DirectoryNotFoundException)
            {
                await ctx.RespondAsync($"I'm configured wrong, `{path}` isn't a real directory ;~;");
            }
            catch (Exception)
            {
                await ctx.RespondAsync("mfw I can't find my pics ;~;");
            }
        }

        [Command("choose")]
        [Aliases("choice")]
        [Description(
            "Selects a random value from a list of choices.\n" +
            "Seperate your choices by spaces, if your thing has spaces in it, surround it with quotes.\n" +
            "ie `>choose \"Go to bed\" \"Stay up all night again, nothing really matters anyway...\"`")]
        public async Task Choose(CommandContext ctx, [Description("Array of possible choices")] params string[] choices)
        {
            var rand = new Random();
            await ctx.RespondAsync(choices[rand.Next(choices.Length)]);
        }

        [Command("avatar")]
        [Description("Returns the avatar from any User(s)")]
        public async Task AvatarAsync(CommandContext ctx, [Description("<target> user(s)")]params DiscordUser[] Users)
        {
            if (!Users.Any())
            {
                await ctx.RespondAsync("You have to select a target!");
                return;
            }
            string avatars = string.Join("\n", Users.Select(x => x.AvatarUrl));
            await ctx.RespondAsync(avatars);
        }

        [Command("8ball"), Aliases("eightball", "magic-conch", "eight-ball")]
        [Description("Returns an answer from the magic 8 ball")]
        public async Task EightBall(CommandContext ctx, [RemainingText] params string[] question)
        {
            Random rand = new Random();
            string[] responses =
            {
                "It is certain",
                "It is decidedly so",
                "Without a doubt",
                "Yes definitely",
                "You may rely on it",
                "As I see it, yes",
                "Most likely",
                "Outlook good",
                "Yes",
                "Signs point to yes",
                "Reply hazy try again",
                "Ask again later",
                "Better not tell you now",
                "Cannot predict now",
                "Concentrate and ask again",
                "Don't count on it",
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful"
            };

            await ctx.RespondAsync($":8ball: **{responses[rand.Next(responses.Count())]}**");
        }

        // Taken & slightly modified from Emzi for 4.0 & readability
        [Command("needsmorejpeg"), Aliases("jpeg", "jpg", "morejpeg", "jaypeg"), Description("Returns an image with more JPEG.")]
        public async Task JpegAsync(CommandContext ctx, [RemainingText] string url = null)
        { 
            HttpClient http = new HttpClient();

            if (string.IsNullOrWhiteSpace(url))
                url = ctx.Message.Attachments.FirstOrDefault()?.Url;
            if (string.IsNullOrWhiteSpace(url))
                throw new ArgumentException("You need to specify an image URL or attach an image.");
            await ctx.TriggerTypingAsync();

            var uri = new Uri(url);
            var response = await http.GetAsync(uri);
            var content = await response.Content.ReadAsByteArrayAsync();

            using (var img = Image.Load<Rgba32>(content))
            using (var ms = new MemoryStream())
            {
                if (img.Width > 400 || img.Height > 400)
                    img.Mutate(x => x.Resize(new ResizeOptions { Mode = ResizeMode.Max, Size = new Size(400, 400) }));
                img.SaveAsJpeg(ms, new JpegEncoder { Quality = 2 });
                ms.Position = 0;
                await ctx.RespondWithFileAsync("jaypeg.jpg", ms,  $"Do I look like I know what a jay-peg is, {ctx.Member.Mention}?");
                await ctx.Message.DeleteAsync();
            }

            http.Dispose();
        }
    }

}
