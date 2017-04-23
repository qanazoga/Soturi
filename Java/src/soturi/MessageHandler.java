package soturi;

import java.io.File;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.Tokens.*;

/**
 * @author qanazoga
 * @version 4/22/2017
 */
public class MessageHandler {
	Random rand = new Random();
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
            lcMessage.contains("fuc you") ||
            lcMessage.contains("hh q") ||
            lcMessage.contains("fh q")
		) {
			response = "fuck u";
			event.getChannel().sendMessage(response).queue();
			response = "";
		}
		
		if (
				event.getAuthor().getId().equals(Tokens.fucbois.get(Fucbois.CHANDLER))&&
				(lcMessage.contains("melly") || lcMessage.contains("mel")) &&
				(lcMessage.contains("need") || lcMessage.contains("want") || lcMessage.contains("asked")) || lcMessage.contains("snug") || lcMessage.contains("hug")
			) event.getChannel().sendMessage("\\*whip cracks*").queue();
		
		if (
				event.getAuthor().getId().equals(Tokens.fucbois.get(Fucbois.BILLY))&&
				lcMessage.contains("@everyone")
				) try {
				event.getChannel().sendFile(new File("data/img/billy.png"), null).queue();
			} catch (Exception e) {
				System.out.println("[ERROR] Something goofed when Billy mentioned @everyone!");
				e.printStackTrace();
			}
		
		if ( 
				lcMessage.contains("what") 
				&& (lcMessage.contains("you") || lcMessage.contains(" ur "))
				&& lcMessage.contains("name")
			) {
			event.getChannel().sendMessage("My real name is " + Tokens.realName).queue();
		}
		
		if (lcMessage.contains("member when") || lcMessage.contains("member wen") || (lcMessage.contains("member") && lcMessage.contains("?"))) {
			event.getChannel().sendMessage("Ooh, I 'member!").queue();
		}
				
	}
}
