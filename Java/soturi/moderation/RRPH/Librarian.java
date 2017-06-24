package soturi.moderation.RRPH;

import net.dv8tion.jda.core.entities.User;
import net.dv8tion.jda.core.entities.Emote;
import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.entities.MessageReaction;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import net.dv8tion.jda.core.events.message.react.MessageReactionAddEvent;
import net.dv8tion.jda.core.events.message.react.MessageReactionRemoveEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

/**
 * @author qanazoga
 * @version 5/18/2017
 *
 * A passive tool used to clear non-constructive messages from #soturi-image-library
 */
public class Librarian extends ListenerAdapter {

	public int votes = 0;

 	@Override
    public void onMessageReceived(MessageReceivedEvent e) {

		if (e.getChannel().getName().equals("soturi-image-library")) {

				e.getMessage().addReaction("⬆").complete();
				e.getMessage().addReaction("⬇").complete();
				Message post = e.getMessage();

				if (post.getAttachments().isEmpty()) {
					removeIllegalMessage(e);
				}
			}
		}
 	}

	/**
 	public void buildFileMessage (MessageReceivedEvent e) {
 		String URL = e.getMessage().getAttachments().get(0).getProxyUrl();
 		int votes = 0;

 		String response = e.getAuthor().getName() + " wants to add this image!:\nCurrent Score: " + votes + "\n";
 		response += URL;

 		e.getChannel().sendMessage(response).complete();
 		e.getMessage().delete().queue();
 	}
	*/

 	// Use this if there are no pictures in the posted message.
 	public void removeIllegalMessage(MessageReceivedEvent e) {
 		System.out.println("[Illegal message found]");
		try {
		e.getAuthor().getPrivateChannel().sendMessage(
				"Your message was removed from Soturi Image Library!\n"
				+ "Please only submit image files.").queue();
		} catch (Exception ex) {} //So Soturi doesn't message itself.
		e.getMessage().delete().queue();
 	}

	/**
 	@Override
 	public void onMessageReactionAdd(MessageReactionAddEvent e) {
 		if (e.getChannel().getName().equals("soturi-image-library")) {
 			int votes = 0;
 	 		Message m = e.getChannel().getMessageById(e.getMessageId()).complete();

 	 		for (MessageReaction r : m.getReactions()) {
 	 			if (r.getEmote().equals("⬆")) {
 	 				votes++;
 	 			} else if (r.getEmote().equals("⬇")) {
 	 				votes--;
 	 			}
 	 		}

 	 		updateVotes(m, votes);
 		}
 	}

 	@Override
 	public void onMessageReactionRemove(MessageReactionRemoveEvent e) {
 		if (e.getChannel().getName().equals("soturi-image-library")) {
 			votes = 0;
 	 		Message m = e.getChannel().getMessageById(e.getMessageId()).complete();

 	 		for (MessageReaction r : m.getReactions()) {
 	 			if (r.getEmote().equals("⬆")) {
 	 				votes++;
 	 			} else if (r.getEmote().equals("⬇")) {
 	 				votes--;
 	 			}
 	 		}

 	 		updateVotes(m, votes);
 		}
 	}

 	public void updateVotes(Message message, int votes) {
 		String editedMessage = "";
 		String[] split = message.getContent().split("\\s+");
 		split[8] = "" + votes;
 		split[6] = "\nCurrent";

 		for (String s: split) {
 			editedMessage += s + " ";
 		}

 		message.editMessage(editedMessage).queue();

 	}
	*/
}
