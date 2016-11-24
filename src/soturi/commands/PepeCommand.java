package soturi.commands;

import java.io.File;
import java.util.ArrayList;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class PepeCommand implements Command {
    @Override
    public String help() {
        return "posts a pepe";
    }

    @Override
    public void action(MessageReceivedEvent e) {
        ArrayList<File> pepes = new ArrayList<>();
        try {
            File pepeFolder = new File("src/pepes");
            if (pepeFolder.exists()) {
                try {
                    for (File pepe : pepeFolder.listFiles()) {
                        pepes.add(pepe);
                    }
                } catch (Exception ex) {
                    System.out.println("[ERROR] Pepes not found!");
                }
                Random rand = new Random();
                e.getChannel().sendFile(pepes.get(rand.nextInt(pepes.size())), null).queue();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}