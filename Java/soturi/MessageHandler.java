package soturi;

import java.io.File;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.Tokens.*;

/**
 * @author qanazoga
 * @version 5/18/2017
 */
public class MessageHandler {
	Random rand = new Random();
	String lcMessage;
	public MessageHandler(MessageReceivedEvent e) {
		lcMessage = e.getMessage().getContent().toLowerCase();
		
		if (
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
			e.getChannel().sendMessage("fuck u").queue();
			
		}
		
		if (
			lcMessage.contains("fuck off")
			) {
			e.getChannel().sendMessage("fuck in ( ͡° ͜ʖ ͡°)").queue();	
		}
		
		if (
				e.getAuthor().getId().equals(Tokens.fucbois.get(Fucbois.CHANDLER))&&
				(lcMessage.contains("melly") || lcMessage.contains("mel")) &&
				(lcMessage.contains("need") || lcMessage.contains("want") || lcMessage.contains("asked")) || lcMessage.contains("snug") || lcMessage.contains("hug")
			) e.getChannel().sendMessage("\\*whip cracks*").queue();
		
		if (
				e.getAuthor().getId().equals(Tokens.fucbois.get(Fucbois.BILLY))&&
				lcMessage.contains("@everyone")
				) try {
				e.getChannel().sendFile(new File("data/img/billy.png"), null).queue();
			} catch (Exception ex) {
				System.out.println("[ERROR] Something goofed when Billy mentioned @everyone!");
				ex.printStackTrace();
			}
		
		if ( 
				lcMessage.contains("what") 
				&& (lcMessage.contains("you") || lcMessage.contains(" ur "))
				&& lcMessage.contains("name")
			) {
			e.getChannel().sendMessage("My real name is " + Tokens.realName).queue();
		}
		
		if (lcMessage.contains("member when") || lcMessage.contains("member wen") || (lcMessage.contains("member") && lcMessage.contains("?"))) {			
			String[] responses = {"Ooh, I 'member!", "Yeah, I 'member!"};			
	        e.getChannel().sendMessage(responses[rand.nextInt(responses.length)]).queue();
		}
				
	}
}
