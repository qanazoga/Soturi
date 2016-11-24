package soturi.commands;

import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class KillUrselfCommand implements Command {
    @Override
    public String help() {
        return "<Optional:USER ID> Give a user the final solution.";
    }
    
    @Override
    public void action(MessageReceivedEvent event) {
        if (!event.getMessage().getMentionedUsers().isEmpty()) {
            String message = "Hey, ";
            for (User u : event.getMessage().getMentionedUsers()) {
                message += u.getAsMention() + ", ";
            }
            message += "you should really kill yourself.";
            event.getChannel().sendMessage(message).queue();
        }
        event.getTextChannel().sendMessage("<https://www.youtube.com/watch?v=2dbR2JZmlWo>").queue();
    }
}