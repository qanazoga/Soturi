package soturi.commands;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/** 
 * @author qanazoga
 * @version 11/20/2016
 */
public interface Command {
    public String help();
    public void action(MessageReceivedEvent e);
}