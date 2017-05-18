package soturi.commands.RRPH;

import net.dv8tion.jda.core.entities.Guild;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.MessageChannel;
import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.commands.Command;

/**
 * @author qanazoga
 * @version 4/22/2017
 */
public class KickRaiderCommand implements Command{
	
	@Override
	public String help() {
		return "<raider ID>: Kick a raider from the server. Requires the @fucboi role to use.";
    }
	
	@Override
	public void action(MessageReceivedEvent e) {
		Guild guild = e.getGuild();
		Message message = e.getMessage();
		MessageChannel channel = e.getChannel();
		User author = e.getAuthor();
		
		try {
			// Make sure the message was written by a fucboi.
			if (guild.getMembersWithRoles(guild.getRoleById("145992439977476097")).contains(e.getMember())) {

				// Tell the fucboi that they need to target someone.
				if (message.getMentionedUsers().isEmpty()) {
					channel.sendMessage("You need to target a raider!").queue();
				} else {
					
					for (User u : e.getMessage().getMentionedUsers()) {
        
						// Tell the fucboi if their target is also a fucboi.
						if (guild.getMembersWithRoles(guild.getRoleById("145992439977476097")).contains(guild.getMember(u))) {
							channel.sendMessage(u.getName() + " is a fucboi").queue();
						} else { // Kick the raider
							channel.sendMessage("Now kicking " + u.getAsMention()).queue();
							guild.getController().kick(u.getId()).queue();
						}
						
					}					
				}
			} else channel.sendMessage(author.getAsMention() + ", you don't have permission to use this command!").queue();
		} catch(Exception ex) {
			channel.sendMessage("Either this server doesn't have a fucbois role, or I don't have proper permissions.\n" +
					"This command only works in Rainbow Rumpus Party Hell").queue();            
		}
	}
}