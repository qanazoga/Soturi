package soturi.commands;

import java.util.Map;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.Bot;

/**
 * @author qanazoga
 * @version 07/22/2017
 */
public class HelpCommand implements Command {
    
    @Override
    public String help() {
        return "Sends you this message.";
    }
    
    @Override
    public void action(MessageReceivedEvent e) {
        String allHelps = "Available Commands\n```\n"; 
        
        for (Map.Entry<String, Command> entry : Bot.getCommands().entrySet()) {
            allHelps += entry.getKey() + ": " +entry.getValue().help() + "\n";
        }
        
        allHelps += "```";
        
        final String compiledHelps = allHelps;
        
        e.getAuthor().openPrivateChannel().queue(c -> {
        	c.sendMessage(compiledHelps).queue();
        });
    }
}