import java.io.File;
import java.util.HashMap;
import java.util.HashSet;

public class MergeDirectories {

    public static void main(String[] ryan) throws Exception {

        final File folderWithAllFiles = new File(System.getProperty("user.dir"));
        final File[] allFiles = folderWithAllFiles.listFiles();

        final HashSet<String> directoryNames = new HashSet<String>();
        //Store all the directories in the hashset
        for(File file : allFiles) {
            if(file.isDirectory()) { 
                directoryNames.add(file.getName());
            }
        }

        int counter = 0;

        //Go through our directories
        for(String directoryName : directoryNames) { 

            if(counter < 2) {
                if(directoryName.length() > 10 && directoryNames.contains(directoryName.substring(0, 10))) {
                    System.out.println(directoryName);
                    moveFiles(new File(directoryName), new File(directoryName.substring(0, 10)));
                }
            }
        }
    }

    public static void moveFiles(final File directoryToMoveFrom, final File directoryToMoveTo) {

        //All the files names in the second directory
        final HashSet<String> alreadyFiles = new HashSet<String>();
        final File[] allFiles = directoryToMoveTo.listFiles();
        for(File file : allFiles) { 
            alreadyFiles.add(file.getName());
        }

        //Go through all the files we need to move
        final File[] toMove = directoryToMoveFrom.listFiles();
        for(File move : toMove) { 

            final String newFileName;
            if(alreadyFiles.contains(move.getName())) {
                //Append a random string
                newFileName = System.currentTimeMillis() + move.getName();
            }
            else {
                newFileName = move.getName();
            }

            //Move the file
            if(move.renameTo(new File(directoryToMoveTo.getAbsolutePath() + "/" + newFileName))) {
                //System.out.println("Successful relocation: " + newFileName);
            }
            else {
                System.out.println("PROBLEM");
            }
        }

        if(directoryToMoveFrom.listFiles().length == 0) { 
            final String name = directoryToMoveFrom.getName();
            if(directoryToMoveFrom.delete()) {
                System.out.println("SUCCESSFULLY EMPTIED AND DELETED: " + name);
            }
            else {
                System.out.println("PROBLEM DELETING: " + name);
            }
        }
        else {
            System.out.println("FILES LEFT");
        }
    }

}

