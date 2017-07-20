package soturi.moderation.RRPH;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
import soturi.Tokens;
import soturi.Tokens.Guilds;

/** 
 * @author qanazoga
 * @version 5/18/2017
 * 
 * Written for use in RRPH but can be modified for other servers as well.
 * If this listener receives a set amount of messages from the same user, marked by Int tolerance, one of two things will happen:
 * If they have the @fucbois role, it will be stripped, and they will be unable to send messages, they will also have a red @silenced tag added.
 * If they have the @Raider role, they will be banned from the server immediately.
 * 
 * Either way, Soturi will send them a message about why they have recieved this punishment.
 * 
 */
public class AutoMod extends ListenerAdapter {
	
	int mentioncount = 0;
	int tolerance = 7;
	
	@Override
    public void onMessageReceived(MessageReceivedEvent e) {
		
		if ((!e.getAuthor().equals(e.getJDA().getSelfUser()))  && e.getGuild().getId().equals(Tokens.guilds.get(Guilds.RRPH))) {
			
			if (!e.getMessage().getMentionedUsers().isEmpty()) {
				mentioncount++;
			}else{
				mentioncount = 0;
			}
			
			if (mentioncount == 3) {
				e.getChannel().sendMessage("Nobody likes Mention Spamming, " + e.getAuthor().getAsMention()).queue();
			}
			
			if (mentioncount == tolerance) {
				if (e.getMember().getRoles().contains(e.getGuild().getRolesByName("fucbois", true).get(0))) {
					Silence(e);
				}
				
				if (e.getMember().getRoles().contains(e.getGuild().getRolesByName("Raiders", true).get(0))) {
					Ban(e);
				}
				mentioncount = 0;
			}
		}
		
	}
	
	
	public static void Silence(MessageReceivedEvent e) {
		e.getGuild().getController().modifyMemberRoles(
				e.getMember(), 
				e.getGuild().getRolesByName("Silenced", true),
				e.getGuild().getRolesByName("fucbois", true)).complete();
				
		e.getAuthor().openPrivateChannel().complete();
		e.getAuthor().getPrivateChannel().sendMessage(
				"Mention spamming will not be tollerated in Rainbow Rumpus Party Hell\n" +
				"You have been silenced until further notice.").complete();
		
		e.getChannel().sendMessage("[Soturi AutoMod now silencing " + e.getAuthor().getAsMention() + " for mention spamming]").queue();
	}
	
	
	public static void Ban(MessageReceivedEvent e) {
		e.getAuthor().openPrivateChannel().complete();
		e.getAuthor().getPrivateChannel().sendMessage(
				"Mention spamming will not be tollerated in Rainbow Rumpus Party Hell\n" +
				"You have been banned.").queue();
		
		e.getChannel().sendMessage("[Soturi AutoMod now banning " + e.getAuthor().getAsMention() + " for mention spamming]").queue();
		e.getGuild().getController().ban(e.getMember(), 0).queue();
	}
}



