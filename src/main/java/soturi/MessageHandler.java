package soturi;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.util.Str;

/**
 * @author qanazoga
 * @version 5/18/2017
 */
public class MessageHandler {	

	public MessageHandler(MessageReceivedEvent e) {
		String msg = e.getMessage().getContent().toLowerCase();
		
		if (Str.containsAll(msg, "press", "f", "to", "pay", "respects"))
			e.getMessage().addReaction("🇫").complete();
		
	}	
}
