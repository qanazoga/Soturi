package soturi.commands.memes;

import java.io.File;
import java.util.ArrayList;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.commands.Command;

/**
 * @author qanazoga
 * @version 4/26/2017
 */
public class PepeCommand implements Command {
    @Override
    public String help() {
        return "posts a pepe";
    }

    @Override
    public void action(MessageReceivedEvent e) {
        ArrayList<File> pepes = new ArrayList<>();
        Random rand = new Random();
        
        try {
            File pepeFolder = new File("data/img/pepe");
            if (pepeFolder.exists()) {
                try {
                    for (File pepe : pepeFolder.listFiles()) {
                        pepes.add(pepe);
                    }
                } catch (Exception ex) {
                    System.out.println("[ERROR] Pepes folder is empty!");
                    e.getChannel().sendMessage("I can't find my pics ;~;").queue();
                }
                e.getChannel().sendFile(pepes.get(rand.nextInt(pepes.size())), null).queue();
            } else {
            	System.out.println("[ERROR] reactions not found!");
                e.getChannel().sendMessage("I can't find my pics ;~;").queue();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}