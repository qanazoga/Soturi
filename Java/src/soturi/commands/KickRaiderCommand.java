package soturi.commands;

import net.dv8tion.jda.core.entities.Guild;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.MessageChannel;
import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class KickRaiderCommand implements Command{

    @Override
    public void action(MessageReceivedEvent event) {
        Guild guild = event.getGuild();
        Message message = event.getMessage();
        MessageChannel channel = event.getChannel();
        User author = event.getAuthor();        
        try {
            // Make sure the message was written by a fucboi.
        	if (guild.getMembersWithRoles(guild.getRoleById("145992439977476097")).contains(event.getMember())) {
                
                // Tell the fucboi that they need to target someone.
                if (message.getMentionedUsers().isEmpty()) channel.sendMessage("You need to target a raider!").queue();
                else {
                    for (User u : event.getMessage().getMentionedUsers()) {
                        
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
        } catch(Exception e) {
            channel.sendMessage("Either this server doesn't have a fucbois role, or I don't have proper permissions.\n" +
                                "This command only works in Rainbow Rumpus Party Hell").queue();            
        }
    }

    @Override
    public String help() {
        return "<raider ID>: Kick a raider from the server. Requires the @fucboi role to use.";
    }
}