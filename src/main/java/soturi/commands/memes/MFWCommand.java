package soturi.commands.memes;

import java.io.File;
import java.util.ArrayList;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.commands.Command;

/**
 * 
 * @author qanazoga
 * @version 07/15/2017
 */
public class MFWCommand implements Command {
    @Override
    public String help() {
        return "mfw you don't know what this command does. -_-";
    }

    @Override
    public void action(MessageReceivedEvent e) {
        ArrayList<File> mfw = new ArrayList<>();
        ArrayList<File> nonImages = new ArrayList<>();
        try {
            File mfwFolder = new File("data/img/mfw");
            if (mfwFolder.exists()) {
                try {
                    for (File img : mfwFolder.listFiles()) {
                        mfw.add(img);
                    }
                    
                    // Remove all non-image files
                    for (File img : mfw) {
                    	if (
                    		img.getName().toLowerCase().endsWith(".jpeg") 
                    		|| img.getName().toLowerCase().endsWith(".jpg")
                    		|| img.getName().toLowerCase().endsWith(".png")
                    		|| img.getName().toLowerCase().endsWith(".gif")
                    		) {
                    		
                    	} else {
                    		nonImages.add(img);
                    	}
                    }
                } catch (Exception ex) {
                    System.out.println("[ERROR] mfw folder is empty!");
                    e.getChannel().sendMessage("mfw I can't find my pics ;~;").queue();
                }
                mfw.removeAll(nonImages);
                Random rand = new Random();
                e.getChannel().sendFile(mfw.get(rand.nextInt(mfw.size())), null).queue();
            } else {
            	System.out.println("[ERROR] reactions not found!");
                e.getChannel().sendMessage("mfw I can't find my pics ;~;").queue();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}