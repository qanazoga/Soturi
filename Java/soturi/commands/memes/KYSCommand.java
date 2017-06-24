package soturi.commands.memes;

import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.commands.Command;

import java.util.Random;

/** HOW OFFENSIVE CAN WE GET? LET'S FIND OUT!
 * @author qanazoga
 * @version 5/18/2017
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
        
        String[] URLs = {
    		"https://youtu.be/ByC8sRdL-Ro", "https://youtu.be/2dbR2JZmlWo",
    		"https://youtu.be/p-zZ6G-23Yg", "http://i.imgur.com/2aSJFFv.jpg",
    		"https://i.redd.it/hcjksye2fhxy.jpg", "http://www.kysexpress.com/wp-content/uploads/2015/10/KYS-LOGO.png"
        };
        
        message += URLs[rand.nextInt(URLs.length)];
        
        e.getChannel().sendMessage(message).queue();
    }
}