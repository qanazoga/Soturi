using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Soturi.Commands
{
    interface ICommandContainer
    {
        List<Task> GetCommands();
    }
}
