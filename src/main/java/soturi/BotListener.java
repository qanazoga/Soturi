package soturi;

import java.util.Map;
import net.dv8tion.jda.core.events.ReadyEvent;
import net.dv8tion.jda.core.events.guild.member.GuildMemberJoinEvent;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
import soturi.commands.*;
import soturi.Tokens.*;

/**
 * 
 * @author qanazoga
 * @version 07/15/2017
 */
public class BotListener extends ListenerAdapter {

    @Override
    public void onMessageReceived(MessageReceivedEvent e) {
        Boolean noCommand = true;
        
        // Make sure the bot isn't the author before you do anything else.
        if (!e.getAuthor().getId().equals(e.getJDA().getSelfUser().getId())) {
        	// Logs the message.
            System.out.println(e.getAuthor().getName() + ":\n" + e.getMessage().getContent() + "\n");
            
            // Looks for commands in the message.
            for (Map.Entry<String, Command> entry : Bot.getCommands().entrySet()) {
                if (e.getMessage().getContent().toLowerCase().contains(entry.getKey().toString())) {
                    noCommand = false;
                	entry.getValue().action(e);
                }
            }
            
            // Forwards the message to the non-command message handler.
            if (noCommand) {
            	new MessageHandler(e);
            }            
        }
    }
    
    @Override
    public void onGuildMemberJoin(GuildMemberJoinEvent e) {
    	// Gives fucbois basic permissions in RRPH
    	if (e.getGuild().getId().equals(Tokens.guilds.get(Guilds.RRPH))) {
    		System.out.println("[A user has joined RRPH!]");
    		if (Tokens.fucbois.values().contains(e.getMember().getUser().getId())) {
    			System.out.println("[User is a fucboi!]");
    			e.getGuild().getController().addRolesToMember(e.getMember(), e.getGuild().getRolesByName("fucbois", true).get(0)).queue();
    			e.getGuild().getTextChannelsByName("memehell", true).get(0).sendMessage(e.getMember().getEffectiveName() + " has returned to the server.").queue();
    		} else { 
    			e.getGuild().getController().addRolesToMember(e.getMember(), e.getGuild().getRolesByName("guests", true).get(0)).queue();
    			e.getGuild().getTextChannelsByName("memehell", true).get(0).sendMessage(e.getMember().getEffectiveName() + " has joined the server.").queue();
    		}
    		
    	}
    }
    
    @Override
    public void onReady(ReadyEvent e) {
        System.out.println("Successfully logged in as " + e.getJDA().getSelfUser().getName());
    }
}