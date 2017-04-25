package soturi.commands;

import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import java.util.Random;

/**
 * @author qanazoga
 * @version 4/24/2017
 */
public class KYSCommand implements Command {
	Random rand = new Random();
	
    @Override
    public String help() {
        return "<Optional:USER ID> Give a user the final solution.";
    }
    
    @Override
    public void action(MessageReceivedEvent e) {
    	
    	String message = "";
        
    	if (!e.getMessage().getMentionedUsers().isEmpty()) {
            message += "Hey, ";
            for (User u : e.getMessage().getMentionedUsers()) {
                message += u.getAsMention() + ", ";
            }
            message += "here's some free advice.\n";
        }
        
        String[] URLs = {"https://youtu.be/ByC8sRdL-Ro", "https://youtu.be/2dbR2JZmlWo"};        
        message += URLs[rand.nextInt(URLs.length)];
        
        e.getChannel().sendMessage(message).queue();
    }
}