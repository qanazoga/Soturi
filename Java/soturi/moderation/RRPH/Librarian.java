package soturi.moderation.RRPH;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

/** 
 * @author qanazoga
 * @version 5/18/2017
 * 
 * A passive tool used to clear non-constructive messages from #soturi-image-library
 */
public class Librarian extends ListenerAdapter {

 	@Override
    public void onMessageReceived(MessageReceivedEvent e) {
		if (e.getChannel().getName().equals("soturi-image-library") && 
				(e.getMessage().getAttachments().isEmpty() || e.getAuthor().isBot()) 
						) {
			System.out.println("[Illegal message found]");
			try {
			e.getAuthor().getPrivateChannel().sendMessage(
					"Your message was removed from Soturi Image Library!\n"
					+ "Please only submit image files.").queue();
			} catch (Exception ex) {} //So Soturi doens't message itself.
			e.getMessage().delete().queue();
		}
	}
	
}
