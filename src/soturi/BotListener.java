package soturi;

import soturi.commands.*;

import java.util.Map;

import net.dv8tion.jda.core.events.ReadyEvent;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class BotListener extends ListenerAdapter {

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        Boolean noCommand = true;
        // Logs the message.
        System.out.println(">>> " + event.getAuthor().getName() + ": " + event.getMessage().getContent());
        
        // Make sure the bot isn't the author before you do anything else.
        if (event.getAuthor().getId() != event.getJDA().getSelfUser().getId()) {
      
            // Looks for commands in the message.
            for (Map.Entry<String, Command> entry : Bot.getCommands().entrySet()) {
                if (event.getMessage().getContent().toLowerCase().contains(entry.getKey().toString())) {
                    noCommand = false;
                	entry.getValue().action(event);
                }
            }
            
            // Forwards the message to the non-command message handler.
            if (noCommand) {
            	new MessageHandler(event);
            }            
        }
    }
    
    @Override
    public void onReady(ReadyEvent e) {
        System.out.println("Successfully logged in as " + e.getJDA().getSelfUser().getName());
    }
}