package soturi;

import java.io.File;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.Tokens.*;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class MessageHandler {
	String lcMessage;
	String response;
	public MessageHandler(MessageReceivedEvent event) {
		lcMessage = event.getMessage().getContent().toLowerCase();
		
		if(
			lcMessage.contains("fuck u") || 
            lcMessage.contains("fuk u") ||
            lcMessage.contains("fuq u") ||
            lcMessage.contains("fuc u") ||
            lcMessage.contains("fuck you") || 
            lcMessage.contains("fuk you") ||
            lcMessage.contains("fuq you") ||
            lcMessage.contains("fuc you")
		) {
			response = "fuck u";
			event.getChannel().sendMessage(response).queue();
			response = "";
		}
		
		if (
				event.getGuild().getMemberById(Tokens.fucbois.get(Fucbois.CHANDLER)) == event.getMember() &&
				(lcMessage.contains("melly") || lcMessage.contains("mel")) &&
				(lcMessage.contains("need") || lcMessage.contains("want") || lcMessage.contains("asked"))
			) event.getChannel().sendMessage("\\*whip cracks*").queue();
		
		if (
				event.getGuild().getMemberById(Tokens.fucbois.get(Fucbois.BILLY)) == event.getMember() &&
				lcMessage.contains("@everyone")
			) try {
				event.getChannel().sendFile(new File("src/billy.PNG"), null).queue();
			} catch (Exception e) {
				System.out.println("[ERROR] Something goofed when Billy mentioned @everyone!");
				e.printStackTrace();
			}
	}
}
