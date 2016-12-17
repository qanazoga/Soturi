package soturi.commands;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 12/17/2016
 */
public class KMSCommand implements Command{
    
    @Override
    public String help() {
        return "use when you've got no options left";
    }

    @Override
    public void action(MessageReceivedEvent event) {
        event.getChannel().sendMessage("Will someone please put " + event.getAuthor().getAsMention() + " out of their misery? \n" +
        "<https://youtu.be/LTnq268y2ms?t=13s>").queue();
    }
}