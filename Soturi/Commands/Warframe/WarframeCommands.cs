using DSharpPlus.CommandsNext.Attributes;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Soturi4.Commands.Warframe
{
    [Group("warframe")]
    public class WarframeCommands
    {

        [Group("time")]
        public class TimeCommands
        {
            
            [Command("cetus")]
            public async Task Cetus()
            {

            }

        }

    }
}
