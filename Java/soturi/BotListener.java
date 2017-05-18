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
 * @version 5/18/2017
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
    		for (String id : Tokens.fucbois.values()) {
    			if (id.equals(e.getMember().getUser().getId())) {
    				System.out.println("[The user is a @fucboi!\n]");
    				e.getGuild().getController().addRolesToMember(e.getMember(), e.getGuild().getRoleById("145992439977476097")).queue();
    			}
    		}
    	}
    }
    
    @Override
    public void onReady(ReadyEvent e) {
        System.out.println("Successfully logged in as " + e.getJDA().getSelfUser().getName());
    }
}