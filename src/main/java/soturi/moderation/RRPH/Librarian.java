package soturi.moderation.RRPH;

import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
import soturi.util.Str;

/**
 * 
 * @author qanazoga
 * @version 07/15/2017
 */
public class Librarian extends ListenerAdapter {
	String channelName;
 	@Override
    public void onMessageReceived(MessageReceivedEvent e) {		
 		channelName = e.getChannel().getName();
 		Message post = e.getMessage();
 		
		if (channelName.equals("soturi-image-library")) {
			
			if (post.getAttachments().isEmpty()) {
				removeIllegalMessage(e);
			} else if (e.getMessage().getContent().toLowerCase().contains("delet")) { // delet this.
				post.addReaction(e.getJDA().getEmoteById("341681244867657753")).complete(); // Keep emote.
				post.addReaction(e.getJDA().getEmoteById("341681253835210753")).complete(); // Delete emote.
			} else {
				post.addReaction("⬆").complete();
				post.addReaction("⬇").complete();	
			}			
			
		} else if (channelName.equals("free-game-news")) {
			if (!Str.containsAll(post.getContent().toLowerCase(), "@free-game-news", "http")) 
				removeIllegalMessage(e);
		}		
	}
	

 	// Use this if there are no pictures in the posted message.
 	public void removeIllegalMessage(MessageReceivedEvent e) {
 		System.out.println("[Illegal message found]");
		try {
			e.getAuthor().openPrivateChannel().queue(c -> { 
				String message = 
						channelName.equals("soturi-image-library") ? 
						"Your message was removed from #soturi-image-library!\nPlease only submit image files." :
						"Your message was removed from #free-game-news!\nPlease remember to tag @free-game-news and include a link to the game.";
				c.sendMessage(message).queue();
			});
				
		} catch (Exception ex) {} //So Soturi doesn't message itself.
		e.getMessage().delete().queue();
 	}
}
