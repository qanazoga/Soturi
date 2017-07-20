package soturi.commands;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/** 
 * @author qanazoga
 * @version 4/22/2017
 */
public interface Command {
    public String help();
    public void action(MessageReceivedEvent e);
}