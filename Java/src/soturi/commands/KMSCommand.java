package soturi.commands;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 4/22/2017
 */
public class KMSCommand implements Command{
    
    @Override
    public String help() {
        return "use when you've got no options left";
    }

    @Override
    public void action(MessageReceivedEvent e) {
        e.getChannel().sendMessage("Will someone please put " + e.getAuthor().getAsMention() + " out of their misery? \n" +
        "<https://youtu.be/LTnq268y2ms?t=13s>").queue();
    }
}