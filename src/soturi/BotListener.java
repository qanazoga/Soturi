package soturi;

import java.util.Map;
import net.dv8tion.jda.core.events.ReadyEvent;
import net.dv8tion.jda.core.events.guild.member.GuildMemberJoinEvent;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
import soturi.commands.*;
import soturi.Tokens.*;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class BotListener extends ListenerAdapter {

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        Boolean noCommand = true;
        
        // Make sure the bot isn't the author before you do anything else.
        if (event.getAuthor().getId() != event.getJDA().getSelfUser().getId()) {
        	// Logs the message.
            System.out.println(">>> " + event.getAuthor().getName() + ": " + event.getMessage().getContent());
            
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
    public void onGuildMemberJoin(GuildMemberJoinEvent event) {
    	// Gives fucbois basic permissions in RRPH
    	if (event.getGuild().getId().equals(Tokens.guilds.get(Guilds.RRPH))) {
    		System.out.println("[A USER HAS JOINED RRPH]");
    		for (String id : Tokens.fucbois.values()) {
    			if (id.equals(event.getMember().getUser().getId())) {
    				System.out.println("[JOINED USER IS A FUCBOI]");
    				event.getGuild().getController().addRolesToMember(event.getMember(), event.getGuild().getRoleById("145992439977476097")).queue();
    			}
    		}
    	}
    }
    
    @Override
    public void onReady(ReadyEvent event) {
        System.out.println("Successfully logged in as " + event.getJDA().getSelfUser().getName());
    }
}