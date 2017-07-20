package soturi.moderation.RRPH;

import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

/**
 * 
 * @author qanazoga
 * @version 07/15/2017
 */
public class Librarian extends ListenerAdapter {

	public int votes = 0;

 	@Override
    public void onMessageReceived(MessageReceivedEvent e) {

		if (e.getChannel().getName().equals("soturi-image-library")) {

			Message post = e.getMessage();
			
			if (post.getAttachments().isEmpty()) {
				removeIllegalMessage(e);
			} else {
			
				post.addReaction("⬆").complete();
				post.addReaction("⬇").complete();
				
			}	
		}
	}

 	// Use this if there are no pictures in the posted message.
 	public void removeIllegalMessage(MessageReceivedEvent e) {
 		System.out.println("[Illegal message found]");
		try {
		e.getAuthor().openPrivateChannel().complete();
		e.getAuthor().getPrivateChannel().sendMessage(
				"Your message was removed from Soturi Image Library!\n"
				+ "Please only submit image files.").queue();
		} catch (Exception ex) {} //So Soturi doesn't message itself.
		e.getMessage().delete().queue();
 	}
}
