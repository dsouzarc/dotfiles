import java.io.File;
import java.util.HashMap;
import java.util.Date;
import java.text.SimpleDateFormat;

public class ResetImageTimes {

    public static final SimpleDateFormat googleDateFormat = new SimpleDateFormat("yyyy-MM-dd");

    public static void main(String[] ryan) throws Exception {

        final File currentDirectory = new File(System.getProperty("user.dir"));
        final File[] directoryFiles = currentDirectory.listFiles();

        int numFileNamesChanged = 0;

        for(File directory : directoryFiles) {

            //We are only going to deal with directories
            if(directory.isDirectory()) {

                //Turn the directories name into a date/time
                final String directoryName = directory.getName();

                final Date pictureTakenDate = googleDateFormat.parse(directoryName);

                //All the images in the folder
                final File[] imagesInFolder = directory.listFiles();

                //Go through all of the images
                for(int i = 0; i < imagesInFolder.length; i++) {

                    final String fileExtension = getFileExtension(imagesInFolder[i].getName());

                    final File newFileName = new File(imagesInFolder[i].getAbsolutePath() + "/" + directoryName + "-" + i + fileExtension);

                    if(newFileName.exists()) {
                        System.out.println("DUPLICATE EXISTS: " + imagesInFolder[i].getName());
                    }

                    else {
                        numFileNamesChanged++;

                        final File newestFile = new File(directoryName + "/" + directoryName + "-" + i + fileExtension);
                        if(imagesInFolder[i].renameTo(newestFile)) {
                            System.out.println("Successfully changed name to: " + newFileName);

                            if(newestFile.setLastModified(pictureTakenDate.getTime())) {
                                System.out.println("SUCCESSFUL DATE MODIFICATION");
                            }
                            else {
                                System.out.println("UNSUCCESSFUL DATE MODIFICATION");
                            }
                        }
                        else {
                            System.out.println("PROBLEM CHANGING FILE NAME: " + imagesInFolder[i].getName());
                        }
                    }
                }
            }
        }

        System.out.println("CHANGED: " + numFileNamesChanged);
    }

    public static String getFileExtension(final String original) { 
        int lastPeriod = original.lastIndexOf(".");

        if(lastPeriod == -1) {
            return "";
        }

        return original.substring(lastPeriod);
    }

}
                
